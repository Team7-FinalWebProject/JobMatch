from data.database import read_query, insert_queries_trasnaction
from data.models.user import User
from data.models.register import RegisterProfessionalData, RegisterCompanyData
from data.models.professional import Professional
from data.models.company import Company
from hashlib import sha256
from psycopg2 import IntegrityError


def _hash_password(password: str):
    return sha256(password.encode('utf-8')).hexdigest()


def create_professional(user: RegisterProfessionalData):
    password = _hash_password(user.password)

    queries = (
        '''INSERT INTO users(username, approved, admin, password) 
           VALUES (?, ?, ?, ?)''',
        
        '''INSERT INTO professionals(
           first_name, last_name, address, user_id, summary, 
           default_offer_id, picture, approved)
           VALUES (?, ?, ?, ?, ?, ?, ?, ?)'''
    )
    params = ((user.username, user.approved, user.admin, password),
              (user.first_name, user.last_name, user.address, user.user_id,
               user.summary, user.default_offer_id, user.picture, user.approved))
    try:
        generated_id = insert_queries_trasnaction(queries, params)
        
        curr_user = User(
            id=generated_id, username=user.username, 
            approved=user.approved, admin=user.admin)
        
        prof = Professional(
            id=generated_id, user_id=curr_user.id, 
            first_name=user.first_name, last_name=user.last_name, 
            address=user.address, summary=user.summary, 
            default_offer_id=user.default_offer_id, picture=user.picture, 
            approved=user.approved)
        
        return curr_user, prof
    except IntegrityError:
        return None
    

def create_company(company_data: RegisterCompanyData):
    password = _hash_password(company_data.password)

    queries = (
        '''INSERT INTO users(username, approved, admin, password) 
           VALUES (?, ?, ?, ?)''',
        
        '''INSERT INTO companies(name, description, address, 
           picture, approved, user_id)
           VALUES (?, ?, ?, ?, ?, ?)''')
    
    params = ((company_data.username, company_data.approved, 
               company_data.admin, password),
              (company_data.company_name, company_data.description, 
               company_data.address,company_data.picture, 
               company_data.approved, company_data.user_id))
    try:
        generated_id = insert_queries_trasnaction(queries, params)
        
        curr_user = User(
            id=generated_id, username=company_data.username, 
            approved=company_data.approved, admin=company_data.admin)
        
        company = Company(
            id=generated_id, user_id=curr_user.id, name=company_data.company_name,
            description=company_data.description, address=company_data.address,
            picture=company_data.picture)
        
        return curr_user, company
    except IntegrityError:
        return None
    

def check_user_exist(nickname:str) -> bool:
    return any(read_query(
        "SELECT * FROM users WHERE username = ?",
        (nickname,)))


def prof_response_object(user: User, professional: Professional):
    return {
        "user_id": professional.user_id,
        "username": user.username,
        "first_name": professional.first_name,
        "last_name": professional.last_name,
        "summary": professional.summary,
    }


def company_response_object(user: User, company: Company):
    return {
        "user_id": company.user_id,
        "username": user.username,
        "company_name": company.name,
        "description": company.description,
        "address": company.address 
    }








# discontinued for now.

# def create_professional(professional: Professional):
#     try:
#         generated_id = insert_query(
#             '''INSERT INTO professionals(
#             first_name, last_name, address, user_id, summary, default_offer_id, picture, approved)
#             VALUES (?, ?, ?, ?, ?, ?, ?, ?)''',
#             (professional.first_name, professional.last_name, professional.address, 
#                 professional.user_id, professional.summary, professional.default_offer_id, 
#                 professional.picture, professional.approved))
        
#         return Professional(id=generated_id, first_name=professional.first_name,
#                             last_name=professional.last_name, address=professional.address,
#                             user_id=professional.user_id, summary=professional.summary,
#                             default_offer_id=professional.default_offer_id, 
#                             picture=professional.picture, approved=professional.approved)
#     except IntegrityError:
#         return None