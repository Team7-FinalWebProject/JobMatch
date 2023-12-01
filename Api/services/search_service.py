from data.database import read_query, update_query, insert_query
from data.models.company import Company, Company_Slim
from data.models.professional import Professional, Professional_Slim
from data.models.offer import CompanyOffer, ProfessionalOffer
from data.readers import reader_one, reader_many
from psycopg2.extras import Json
from common.utils.calc import apply_salary_threshold
from fastapi import Response

# --view company
def get_company_by_id(id: int, approved=True):
    data = read_query(
        '''SELECT c.id, u.username, c.name, c.description, c.address
            FROM companies c
            LEFT JOIN users u
            ON c.user_id=u.id
            WHERE c.id = %s
            AND c.approved = %s''',
        (id,approved,))
    if not data:
        return Response(status_code=404)
    return reader_one(Company_Slim, data)

# --view all companies (+filters)
def get_companies(approved=True):
    data = read_query(
        '''SELECT c.id, u.username, c.name, c.description, c.address
            FROM companies c
            LEFT JOIN users u
            ON c.user_id=u.id
            WHERE c.approved = %s''',
        (approved,))
    return reader_many(Company_Slim, data)

# --view professional
def get_professional_by_id(id: int, approved=True):
    data = read_query(
        '''SELECT p.id, u.username, p.default_offer_id, p.first_name, p.last_name, p.summary, p.address, p.status 
            FROM professionals p
            LEFT JOIN users u
            ON p.user_id=u.id
            WHERE p.id = %s
            AND p.approved = %s''',
        (id,approved,))
    if not data:
        return Response(status_code=404)
    return reader_one(Professional_Slim, data)

# --view all professionals (+filters)
def get_professionals(approved=True):
    data = read_query(
        '''SELECT p.id, u.username, p.default_offer_id, p.first_name, p.last_name, p.summary, p.address, p.status 
            FROM professionals p
            LEFT JOIN users u
            ON p.user_id=u.id
            WHERE p.approved = %s''',
        (approved,))
    return reader_many(Professional_Slim, data)


# --view company offer
def get_company_offer_by_id(id: int, company_id: int | None = None, approved=True, active=True):
    status = 'active' if active else None
    data = read_query(
        '''SELECT co.id, co.company_id, co.chosen_professional_offer_id, co.status, co.requirements, co.min_salary, co.max_salary 
            FROM company_offers co
            LEFT JOIN companies c
            ON co.company_id=c.id
            WHERE co.id = %s
            AND c.approved = %s
            AND co.status = COALESCE(%s, co.status)
            AND c.id = COALESCE(%s, c.id)''',
        (id, approved, status, company_id))
    if not data:
        return Response(status_code=404)
    return reader_one(CompanyOffer, data)

# --view all company offers (+filters, filters: active/inactive, salary, requirements, ++)
def get_company_offers(
        min_salary: int = 0,
        max_salary: int = 2147483647,
        filter_distance_from_latest: int | None = None,
        salary_threshold_pct: int = 0,
        allowed_missing_skills: int = 0,
        user_id: int | None = None,
        company_id: int | None = None,
        approved = True,
        active = True):
    status = 'active' if active else None
    min_filter, max_filter = apply_salary_threshold(min_salary, max_salary, salary_threshold_pct)
    user_id = user_id if filter_distance_from_latest is not None else None
    limit, offset = 1, 0 + (filter_distance_from_latest if filter_distance_from_latest else 0)
    data = read_query(
         '''WITH filter_skills AS
                (SELECT COALESCE
                    ((SELECT filter FROM web_filters WHERE user_id = %s ORDER BY id desc LIMIT %s OFFSET %s),
                %s)::jsonb AS skills)
            SELECT co.id, co.company_id, co.chosen_professional_offer_id, co.status, co.requirements, co.min_salary, co.max_salary
            FROM company_offers co
            CROSS JOIN filter_skills fs
            LEFT JOIN companies c
            ON co.company_id=c.id
            WHERE c.approved = %s
            AND co.status = COALESCE(%s, co.status)
            AND co.min_salary <= %s
            AND co.max_salary >= %s
            AND GREATEST(
		        (SELECT COUNT(*) - %s FROM jsonb_object_keys(fs.skills)),
		        0) <=
            COALESCE(
                (SELECT COUNT(*) FROM jsonb_object_keys(fs.skills) key
                WHERE (co.requirements->key->>0)::int >= (fs.skills->key)::int),
                0)
            AND c.id = COALESCE(%s, c.id)
         ;''',
         (user_id, limit, offset, Json({}), approved, status, max_filter, min_filter, allowed_missing_skills, company_id))
    
    return reader_many(CompanyOffer, data)

# --view professional offer (hide hidden)
def get_professional_offer_by_id(id: int, professional_id: int | None = None, approved=True, active=True):
    status1 = 'active' if active else None
    status2 = 'private' if active else None
    data = read_query(
        '''SELECT po.id, po.professional_id, po.chosen_company_offer_id, po.description, po.status, po.skills, po.min_salary, po.max_salary 
            FROM professional_offers po
            LEFT JOIN professionals p
            ON po.professional_id=p.id
            WHERE po.id = %s
            AND p.approved = %s
            AND (po.status = COALESCE(%s, po.status) OR po.status = COALESCE(%s, po.status))
            AND p.id = COALESCE(%s, p.id)''',
        (id, approved, status1, status2, professional_id))
    if not data:
        return Response(status_code=404)
    return reader_one(ProfessionalOffer, data)

# --view all professional offers (self, self=professional, filters: active/inactive)
# --view all professional offers (hide inactive, private and hidden) (+filters salary, requirements, ++)
def get_professional_offers(
        min_salary: int = 0,
        max_salary: int = 2147483647,
        filter_distance_from_latest: int | None = None,
        salary_threshold_pct: int = 0,
        allowed_missing_skills: int = 0,
        user_id: int | None = None,
        professional_id: int | None = None,
        approved = True,
        active = True):
    status = 'active' if active else None
    min_filter, max_filter = apply_salary_threshold(min_salary, max_salary, salary_threshold_pct)
    user_id = user_id if filter_distance_from_latest is not None else None
    limit, offset = 1, 0 + (filter_distance_from_latest if filter_distance_from_latest else 0)
    data = read_query(
         '''WITH filter_skills AS
            (SELECT COALESCE
                ((SELECT filter FROM web_filters WHERE user_id = %s ORDER BY id desc LIMIT %s OFFSET %s),
            %s)::jsonb AS skills)
                SELECT po.id, po.professional_id, po.chosen_company_offer_id, po.description, po.status, po.skills, po.min_salary, po.max_salary 
                FROM professional_offers po
                CROSS JOIN filter_skills fs
                LEFT JOIN professionals p
                ON po.professional_id=p.id
                WHERE p.approved = %s
                AND po.status = COALESCE(%s, po.status)
                AND po.min_salary <= %s
                AND po.max_salary >= %s
                AND GREATEST(
                    (SELECT COUNT(*) - %s FROM jsonb_object_keys(fs.skills)),
                    0) <=
                COALESCE(
                    (SELECT COUNT(*) FROM jsonb_object_keys(fs.skills) key
                    WHERE (po.skills->key->>0)::int >= (fs.skills->key)::int),
                    0)
                AND p.id = COALESCE(%s, p.id)
         ;''',
         (user_id, limit, offset, Json({}), approved, status, max_filter, min_filter, allowed_missing_skills, professional_id))
    return reader_many(ProfessionalOffer, data)


def propose_new_skills(skills):
    result = update_query(
        '''UPDATE config
        SET pending_approval_skills = pending_approval_skills || %s
        WHERE lock = %s''', (Json(skills),'X',))
    ##TODO: check result and remodel
    return result

def add_webfilter(id, filters):
    result = insert_query(
        '''INSERT INTO web_filters (filter, user_id) VALUES (%s, %s) RETURNING id''',
        (Json(filters), id))
    ##TODO: check result and remodel
    return result