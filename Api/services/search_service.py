from data.database import read_query
from data.models.company import Company, Company_Username
from data.models.professional import Professional, Professional_Username
from data.models.offer import CompanyOffer, ProfessionalOffer
from data.readers import reader_one, reader_many
from psycopg2.extras import Json


def apply_salary_threshold(min_salary, max_salary, threshold):
    try:
        min_salary,max_salary, threshold = float(min_salary),float(max_salary), float(threshold)
    except:
        try:
            min_salary,max_salary, threshold = sum(map(ord, min_salary)),sum(map(ord, max_salary)), sum(map(ord, threshold))
        except:
            return 0, 0

    fraction = threshold / 100
    multiplyer = fraction + 1

    swap = lambda mi,ma : (ma,mi) if mi > ma else (mi,ma)
    min_salary, max_salary = swap(min_salary, max_salary)

    def decay(min_salary, multi):
        decayed_salary = (min_salary / multi) if multi > 0 else 0
        return max(0,min(2147483647,int(round(decayed_salary))))

    def growth(max_salary, multi):
        growed_salary = (max_salary * multi) if multi < 2147483647 else 2147483647
        return max(0,min(2147483647,int(round(growed_salary))))

    modified_min_salary = decay(min_salary, multiplyer) 
    modified_max_salary = growth(max_salary, multiplyer)

    modified_min_salary, modified_max_salary = swap(modified_min_salary, modified_max_salary)

    return modified_min_salary, modified_max_salary

##TODO: Abstract?
_APPROVED_COMPANY_Q = 'WHERE c.approved = True'
_APPROVED_PROFESSIONAL_Q = 'WHERE p.approved = True'

# --view company
def get_approved_company_by_id(id: int):
    data = read_query(
        '''SELECT c.id, u.username, c.name, c.description, c.address, c.picture
            FROM companies c
            LEFT JOIN users u
            ON c.user_id=u.id
            WHERE c.id = %s
            AND c.approved = %s''',
        (id,True,))
    return reader_one(Company_Username, data)

def get_unapproved_company_by_id(id: int):
    data = read_query(
        '''SELECT c.id, u.username, c.name, c.description, c.address, c.picture
            FROM companies c
            LEFT JOIN users u
            ON c.user_id=u.id
            WHERE c.id = %s
            AND c.approved = %s''',
        (id,False,))
    return reader_one(Company_Username, data)

# --view all companies (+filters)
def get_approved_companies():
    data = read_query(
        '''SELECT c.id, u.username, c.name, c.description, c.address, c.picture
            FROM companies c
            LEFT JOIN users u
            ON c.user_id=u.id
            WHERE c.approved = %s''',
        (True,))
    return reader_many(Company_Username, data)

def get_unapproved_companies():
    data = read_query(
        '''SELECT c.id, u.username, c.name, c.description, c.address, c.picture
            FROM companies c
            LEFT JOIN users u
            ON c.user_id=u.id
            WHERE c.approved = %s''',
        (False,))
    return reader_many(Company_Username, data)

# --view professional
def get_approved_professional_by_id(id: int):
    data = read_query(
        '''SELECT p.id, u.username, p.default_offer_id, p.first_name, p.last_name, p.summary, p.address, p.picture 
            FROM professionals p
            LEFT JOIN users u
            ON p.user_id=u.id
            WHERE p.id = %s
            AND p.approved = %s''',
        (id,True,))
    return reader_one(Professional_Username, data)

def get_unapproved_professional_by_id(id: int):
    data = read_query(
        '''SELECT p.id, u.username, p.default_offer_id, p.first_name, p.last_name, p.summary, p.address, p.picture 
            FROM professionals p
            LEFT JOIN users u
            ON p.user_id=u.id
            WHERE p.id = %s
            AND p.approved = %s''',
        (id,False,))
    return reader_one(Professional_Username, data)

# --view all professionals (+filters)
def get_approved_professionals():
    data = read_query(
        '''SELECT p.id, u.username, p.default_offer_id, p.first_name, p.last_name, p.summary, p.address, p.picture 
            FROM professionals p
            LEFT JOIN users u
            ON p.user_id=u.id
            WHERE p.approved = %s''',
        (True,))
    return reader_many(Professional_Username, data)

def get_unapproved_professionals():
    data = read_query(
        '''SELECT p.id, u.username, p.default_offer_id, p.first_name, p.last_name, p.summary, p.address, p.picture 
            FROM professionals p
            LEFT JOIN users u
            ON p.user_id=u.id
            WHERE p.approved = %s''',
        (False,))
    return reader_many(Professional_Username, data)

# --view company offer
def get_approved_active_company_offer_by_id(id: int):
    data = read_query(
        '''SELECT co.id, co.company_id, co.chosen_professional_id, co.status, co.requirements, co.min_salary, co.max_salary 
            FROM company_offers co
            LEFT JOIN companies c
            ON co.company_id=c.id
            WHERE co.id = %s
            AND c.approved = %s
            AND co.status = %s''',
        (id, True, 'active'))
    return reader_one(CompanyOffer, data)

def get_approved_archived_company_offer_by_id(id: int):
    data = read_query(
        '''SELECT co.id, co.company_id, co.chosen_professional_id, co.status, co.requirements, co.min_salary, co.max_salary 
            FROM company_offers co
            LEFT JOIN companies c
            ON co.company_id=c.id
            WHERE co.id = %s
            AND c.approved = %s''',
        (id, True))
    return reader_one(CompanyOffer, data)

# --view all company offers (+filters, filters: active/inactive, salary, requirements, ++)
def get_approved_active_company_offers(
        min_salary: int = 0,
        max_salary: int = 2147483647,
        requirements: dict = {},
        salary_threshold_pct: int = 0,
        allowed_missing_skills: int = 0):
    
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
            AND co.status = %s
            AND co.min_salary <= %s
            AND co.max_salary >= %s
            AND GREATEST(
		        (SELECT COUNT(*) - %s FROM jsonb_object_keys(fs.skills)),
		        0) <=
            COALESCE(
                (SELECT COUNT(*) FROM jsonb_object_keys(fs.skills) key
                WHERE (co.requirements->key->>0)::int >= (fs.skills->key)::int),
                0)
         ;''',
         (Json(requirements), True, 'active', max_filter, min_filter, allowed_missing_skills))
    
    return reader_many(CompanyOffer, data)

def get_approved_archived_company_offers():
    data = read_query(
        '''SELECT co.id, co.company_id, co.chosen_professional_id, co.status, co.requirements, co.min_salary, co.max_salary 
            FROM company_offers co
            LEFT JOIN companies c
            ON co.company_id=c.id
            WHERE c.approved = %s''',
        (True,))
    return reader_many(CompanyOffer, data)

# --view professional offer (hide hidden)
def get_approved_active_professional_offer_by_id(id: int):
    data = read_query(
        '''SELECT po.id, po.professional_id, po.chosen_company_offer_id, po.description, po.status, po.skills, po.min_salary, po.max_salary 
            FROM professional_offers po
            LEFT JOIN professionals p
            ON po.professional_id=p.id
            WHERE po.id = %s
            AND p.approved = %s
            AND (po.status = %s OR po.status = %s)''',
        (id, True, 'active', 'private'))
    return reader_one(ProfessionalOffer, data)

def get_approved_hidden_professional_offer_by_id(id: int):
    data = read_query(
        '''SELECT po.id, po.professional_id, po.chosen_company_offer_id, po.description, po.status, po.skills, po.min_salary, po.max_salary 
            FROM professional_offers po
            LEFT JOIN professionals p
            ON po.professional_id=p.id
            WHERE po.id = %s
            AND p.approved = %s''',
        (id, True))
    return reader_one(ProfessionalOffer, data)

# --view all professional offers (self, self=professional, filters: active/inactive)
# --view all professional offers (hide inactive, private and hidden) (+filters salary, requirements, ++)
def get_approved_active_professional_offers(
        min_salary: int = 0,
        max_salary: int = 2147483647,
        requirements: dict = {},
        salary_threshold_pct: int = 0,
        allowed_missing_skills: int = 0):
    
    min_filter, max_filter = apply_salary_threshold(min_salary, max_salary, salary_threshold_pct)
    print(min_filter,max_filter)
    
    data = read_query(
         '''WITH filter_skills AS (
                SELECT %s::jsonb AS skills)
            SELECT po.id, po.professional_id, po.chosen_company_offer_id, po.description, po.status, po.skills, po.min_salary, po.max_salary 
            FROM professional_offers po
            CROSS JOIN filter_skills fs
            LEFT JOIN professionals p
            ON po.professional_id=p.id
            WHERE p.approved = %s
            AND po.status = %s
            AND po.min_salary <= %s
            AND po.max_salary >= %s
            AND GREATEST(
		        (SELECT COUNT(*) - %s FROM jsonb_object_keys(fs.skills)),
		        0) <=
            COALESCE(
                (SELECT COUNT(*) FROM jsonb_object_keys(fs.skills) key
                WHERE (po.skills->key->>0)::int >= (fs.skills->key)::int),
                0)
         ;''',
         (Json(requirements), True, 'active', max_filter, min_filter, allowed_missing_skills))
    
    return reader_many(ProfessionalOffer, data)

def get_approved_hidden_professional_offers():
    data = read_query(
        '''SELECT po.id, po.professional_id, po.chosen_company_offer_id, po.description, po.status, po.skills, po.min_salary, po.max_salary 
            FROM professional_offers po
            LEFT JOIN professionals p
            ON po.professional_id=p.id
            WHERE p.approved = %s''',
        (True,))
    return reader_many(ProfessionalOffer, data)
