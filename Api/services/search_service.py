from data.database import read_query
from data.models.company import Company, Company_Username
from data.models.professional import Professional, Professional_Username
from data.models.offer import CompanyOffer, ProfessionalOffer
from data.readers import reader_one, reader_many
from psycopg2.extras import Json
from common.utils.calc import apply_salary_threshold

##TODO: SELF functionality (id filter)

#########Interface:
# ####Professional:
def professional_get_self_info(professional_id):
    return _get_professional_by_id(professional_id)

def professional_get_self_offer_by_id(id, professional_id):
    return _get_professional_offer_by_id(id=id, professional_id=professional_id, active=False)#id from token)

def professional_get_self_offers(professional_id):
    return _get_professional_offers(professional_id=professional_id, active=False)#id from token

def professional_get_company_offer_by_id(id: int):
    return _get_company_offer_by_id(id=id)

def professional_get_company_offers(*filters):
    return _get_company_offers(*filters)


# ####Company:
def company_get_self_info(company_id):
    return _get_company_by_id(company_id)

def company_get_self_offer_by_id(id, company_id):
    return _get_company_offer_by_id(id=id, company_id=company_id, active=False) #id from token

def company_get_self_offers(company_id):
    return _get_company_offers(company_id=company_id, active=False) #id from token

def company_get_professional_offer_by_id(id: int):
    return _get_professional_offer_by_id(id=id)

def company_get_professional_offers(*filters):
    return _get_professional_offers(*filters)


# ####ADMIN:
def admin_get_unapproved_company_by_id(id: int):
    return _get_company_by_id(id=id, approved=False)

def admin_get_unapproved_companies():
    return _get_companies(approved=False)

def admin_get_unapproved_professional_by_id(id: int):
    return _get_professional_by_id(id=id, approved=False)

def admin_get_unapproved_professionals():
    return _get_professionals(approved=False)

# ####SEARCH:
def search_get_company_by_id(id: int):
    return _get_company_by_id(id=id)

def search_get_companies():
    return _get_companies(approved=True)

def search_get_professional_by_id(id: int):
    return _get_professional_by_id(id=id)

def search_get_professionals():
    return _get_professionals()

def search_get_company_offer_by_id(id: int):
    return _get_company_offer_by_id(id=id)

def search_get_company_offers(*filters):
    return _get_company_offers(*filters)

def search_get_professional_offer_by_id(id: int):
    return _get_professional_offer_by_id(id=id)

def search_get_professional_offers(*filters):
    return _get_professional_offers(*filters)


# --view company
def _get_company_by_id(id: int, approved=True):
    data = read_query(
        '''SELECT c.id, u.username, c.name, c.description, c.address, c.picture
            FROM companies c
            LEFT JOIN users u
            ON c.user_id=u.id
            WHERE c.id = %s
            AND c.approved = %s''',
        (id,approved,))
    return reader_one(Company_Username, data)

# --view all companies (+filters)
def _get_companies(approved=True):
    data = read_query(
        '''SELECT c.id, u.username, c.name, c.description, c.address, c.picture
            FROM companies c
            LEFT JOIN users u
            ON c.user_id=u.id
            WHERE c.approved = %s''',
        (approved,))
    return reader_many(Company_Username, data)

# --view professional
def _get_professional_by_id(id: int, approved=True):
    data = read_query(
        '''SELECT p.id, u.username, p.default_offer_id, p.first_name, p.last_name, p.summary, p.address, p.picture 
            FROM professionals p
            LEFT JOIN users u
            ON p.user_id=u.id
            WHERE p.id = %s
            AND p.approved = %s''',
        (id,approved,))
    return reader_one(Professional_Username, data)

# --view all professionals (+filters)
def _get_professionals(approved=True):
    data = read_query(
        '''SELECT p.id, u.username, p.default_offer_id, p.first_name, p.last_name, p.summary, p.address, p.picture 
            FROM professionals p
            LEFT JOIN users u
            ON p.user_id=u.id
            WHERE p.approved = %s''',
        (approved,))
    return reader_many(Professional_Username, data)


# --view company offer
def _get_company_offer_by_id(id: int, company_id: int | None = None, approved=True, active=True):
    status = 'active' if active else None
    data = read_query(
        '''SELECT co.id, co.company_id, co.chosen_professional_id, co.status, co.requirements, co.min_salary, co.max_salary 
            FROM company_offers co
            LEFT JOIN companies c
            ON co.company_id=c.id
            WHERE co.id = %s
            AND c.approved = %s
            AND co.status = COALESCE(%s, co.status)
            AND c.id = COALESCE(%s, c.id)''',
        (id, approved, status, company_id))
    return reader_one(CompanyOffer, data)

# --view all company offers (+filters, filters: active/inactive, salary, requirements, ++)
def _get_company_offers(
        min_salary: int = 0,
        max_salary: int = 2147483647,
        filter_skills: dict = {},
        salary_threshold_pct: int = 0,
        allowed_missing_skills: int = 0,
        company_id: int | None = None,
        approved = True,
        active = True):
    status = 'active' if active else None
    min_filter, max_filter = apply_salary_threshold(min_salary, max_salary, salary_threshold_pct)
    data = read_query(
         '''WITH filter_skills AS (
                SELECT %s::jsonb AS skills)
            SELECT co.id, co.company_id, co.chosen_professional_id, co.status, co.requirements, co.min_salary, co.max_salary
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
         (Json(filter_skills), approved, status, max_filter, min_filter, allowed_missing_skills, company_id))
    
    return reader_many(CompanyOffer, data)

# --view professional offer (hide hidden)
def _get_professional_offer_by_id(id: int, professional_id: int | None = None, approved=True, active=True):
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
    return reader_one(ProfessionalOffer, data)

# --view all professional offers (self, self=professional, filters: active/inactive)
# --view all professional offers (hide inactive, private and hidden) (+filters salary, requirements, ++)
def _get_professional_offers(
        min_salary: int = 0,
        max_salary: int = 2147483647,
        filter_skills: dict = {},
        salary_threshold_pct: int = 0,
        allowed_missing_skills: int = 0,
        professional_id: int | None = None,
        approved = True,
        active = True):
    status = 'active' if active else None
    min_filter, max_filter = apply_salary_threshold(min_salary, max_salary, salary_threshold_pct)
    data = read_query(
         '''WITH filter_skills AS (
                SELECT %s::jsonb AS skills)
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
         (Json(filter_skills), approved, status, max_filter, min_filter, allowed_missing_skills, professional_id))
    return reader_many(ProfessionalOffer, data)