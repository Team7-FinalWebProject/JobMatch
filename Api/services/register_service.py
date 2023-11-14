from data.database import read_query, insert_query, update_query, update_queries_transaction
from data.models.user import User
from data.models.company import Company
from data.models.professional import Professional
from hashlib import sha256
from secrets import compare_digest


def _hash_password(password: str):
    return sha256(password.encode('utf-8')).hexdigest()


def create_user(username: str, approved: bool, password: str):
        password = _hash_password(password)
        generated_id = insert_query(
            '''INSERT INTO users(username, approved, password) 
             VALUES (?, ?, ?)''',
            (username, approved, password))

        return User(id=generated_id, username=username, approved=approved)


def create_company(username: str, company_name:str, password: str) -> Company | None:
        generated_id = insert_query(
            'INSERT INTO companies(username, company_name, password) VALUES (?, ?, ?)',
            (username, company_name, password))

        return Company(id=generated_id, username=username, company_name=company_name)


def check_user_exist(nickname:str) -> bool:
    return any(read_query(
        "SELECT * FROM users WHERE username = ?",
        (nickname,)))
