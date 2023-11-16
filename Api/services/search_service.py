from data.database import read_query
from data.models.company import Company, Company_Username
from data.models.professional import Professional, Professional_Username
from data.models.offer import CompanyOffer, ProfessionalOffer
from data.readers import reader_one, reader_many

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
        '''SELECT c.id, u.username, c.name, c.description, c.address, c.picture, c.approved 
            FROM companies c
            LEFT JOIN users u
            ON c.user_id=u.id
            WHERE c.approved = %s''',
        (True,))
    return reader_many(Company_Username, data)

def get_unapproved_companies():
    data = read_query(
        '''SELECT c.id, u.username, c.name, c.description, c.address, c.picture, c.approved 
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
def get_approved_company_offer_by_id(id: int):
    data = read_query(
        '''SELECT co.id, co.company_id, co.status, co.chosen_professional_id, co.requirements, co.min_salary, co.max_salary 
            FROM company_offers co
            LEFT JOIN companies c
            ON co.company_id=c.id
            WHERE co.id = %s
            AND c.approved = %s''',
        (id, True,))
    return reader_one(CompanyOffer, data)

# --view all company offers (+filters, filters: active/inactive, salary, requirements, ++)
def get_company_offers():
    data = read_query(
        '''SELECT co.id, co.company_id, co.status, co.chosen_professional_id, co.requirements, co.min_salary, co.max_salary 
            FROM company_offers co
            LEFT JOIN companies c
            ON co.company_id=c.id
            WHERE c.approved = %s''',
        (True,))
    return reader_many(CompanyOffer, data)

# --view professional offer (hide hidden)
def get_professional_offer_by_id(id: int):
    pass

# --view all professional offers (self, self=professional, filters: active/inactive)
# --view all professional offers (hide inactive, private and hidden) (+filters salary, requirements, ++)
def get_professional_offers():
    pass

