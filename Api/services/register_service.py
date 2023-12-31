from data.database import read_query, insert_query
from data.models.register import RegisterProfessionalData, RegisterCompanyData
from data.models.professional import Professional
from data.models.company import Company
from hashlib import sha256


def _hash_password(password: str):
    return sha256(password.encode('utf-8')).hexdigest()


def create_professional(user: RegisterProfessionalData, password: str):
    curr_pass = _hash_password(password)

    user_id = insert_query(
        '''INSERT INTO users(username, password) 
           VALUES (%s, %s) RETURNING id''', (user.username, curr_pass))
    
    prof_id = insert_query(
        '''INSERT INTO professionals(
           first_name, last_name, address, user_id, summary)
           VALUES (%s, %s, %s, %s, %s) RETURNING id''', 
           (user.first_name, user.last_name, 
           user.address, user_id, user.summary))
    
    return Professional(
        id=prof_id, user_id=user_id,
        first_name=user.first_name, last_name=user.last_name, 
        address=user.address, summary=user.summary)
    

def create_company(company_data: RegisterCompanyData, password: str):
    curr_pass = _hash_password(password)

    user_id = insert_query(
        '''INSERT INTO users(username, password) 
           VALUES (%s, %s) RETURNING id''', 
           (company_data.username, curr_pass))

    company_id = insert_query(
        '''INSERT INTO companies(name, description, address, user_id)
           VALUES (%s, %s, %s, %s) RETURNING id''', 
           (company_data.company_name, company_data.description,
            company_data.address, user_id))
    
    return Company(
        id=company_id, user_id=user_id, name=company_data.company_name,
        description=company_data.description, address=company_data.address)
    

def check_user_exist(nickname:str) -> bool:
    return any(read_query(
        "SELECT * FROM users WHERE username = %s",
        (nickname,)))


def prof_response_object(user, professional: Professional):
    return {
        "id": professional.id,
        "user_id": professional.user_id,
        "username": user.username,
        "first_name": professional.first_name,
        "last_name": professional.last_name,
        "summary": professional.summary
    }


def company_response_object(user, company: Company):
    return {
        "id": company.id,
        "user_id": company.user_id,
        "username": user.username,
        "company_name": company.name,
        "description": company.description,
        "address": company.address 
    }


def random_pass_response(user: Professional | Company, password: str):
    pass_msg = f'Please save this password {password}'
    if isinstance(user, Professional):
        return {
            "id": user.id,
            "user_id": user.user_id,
            "full_name": f'{user.first_name} {user.last_name}',
            "summary": user.summary,
            "password": pass_msg
        }
    elif isinstance(user, Company):
        return {
            "id": user.id,
            "user_id": user.user_id,
            "company_name": user.name,
            "description": user.description,
            "address": user.address,
            "password": pass_msg
        }


def generate_random_password(registation_data: RegisterCompanyData | RegisterProfessionalData):
    import random
    import string

    max_length = 20

    lower_case = string.ascii_lowercase
    upper_case = string.ascii_uppercase
    numbers = string.digits
    special_chars = "@$!%*?&"

    password_set = (
            random.choice(lower_case) +
            random.choice(upper_case) +
            random.choice(numbers) +
            random.choice(special_chars))

    valid = registation_data.validate_password(password_set)
    if valid:
        password_set += ''.join(
            random.choice(string.ascii_letters + string.digits + special_chars)
            for _ in range(max_length - len(password_set)))

    password_list = list(password_set)
    random.shuffle(password_list)
    return ''.join(password_list)