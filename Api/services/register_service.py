from data.database import read_query, insert_query, update_query, update_queries_transaction
from data.models.user import User
from data.models.professional import Professional
from data.models.company import Company
from hashlib import sha256
from psycopg2 import IntegrityError


def _hash_password(password: str):
    return sha256(password.encode('utf-8')).hexdigest()


def create_user(username: str, approved: bool, admin: bool, password: str):
    password = _hash_password(password)
    generated_id = insert_query(
        '''INSERT INTO users(username, approved, admin, password) 
        VALUES (?, ?, ?, ?)''',
        (username, approved, admin, password))

    return User(id=generated_id, username=username, approved=approved, admin= admin)


def create_professional(professional: Professional):
    try:
        generated_id = insert_query(
            '''INSERT INTO professionals(
            first_name, last_name, address, user_id, summary, default_offer_id, picture, approved)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)''',
            (professional.first_name, professional.last_name, professional.address, 
                professional.user_id, professional.summary, professional.default_offer_id, 
                professional.picture, professional.approved))
        
        return Professional(id=generated_id, first_name=professional.first_name,
                            last_name=professional.last_name, address=professional.address,
                            user_id=professional.user_id, summary=professional.summary,
                            default_offer_id=professional.default_offer_id, 
                            picture=professional.picture, approved=professional.approved)
    except IntegrityError:
        return None
    

def create_company(company: Company) -> Company:
    try:
        generated_id = insert_query(
            '''INSERT INTO companies(name, description, address, picture, approved) 
               VALUES (?, ?, ?, ?, ?)''',
            (company.name, company.description, 
             company.address, company.picture, company.approved))

        return Company(id=generated_id, name=company.name, description=company.description,
                       address=company.address, picture=company.picture, approved=company.approved)
    except IntegrityError:
        return None
    

def check_user_exist(nickname:str) -> bool:
    return any(read_query(
        "SELECT * FROM users WHERE username = ?",
        (nickname,)))
