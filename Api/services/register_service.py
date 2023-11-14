from data.database import read_query, insert_query, update_query, update_queries_transaction
from data.models import Professional, Company
from hashlib import sha256
from secrets import compare_digest


def _hash_password(password: str):
    return sha256(password.encode('utf-8')).hexdigest()


def create_professional(username: str, first_name:str, last_name:str, password: str) -> Professional | None:
        password = _hash_password(password)
        generated_id = insert_query(
            'INSERT INTO professionals(username, first_name, last_name, password) VALUES (?, ?, ?, ?)',
            (username, first_name, last_name, password))

        return Professional(id=generated_id, username=username, first_name=first_name, last_name=last_name)


def create_company(username: str, company_name:str, password: str) -> Company | None:
        password = _hash_password(password)
        generated_id = insert_query(
            'INSERT INTO companies(username, company_name, password) VALUES (?, ?, ?)',
            (username, company_name, password))

        return Company(id=generated_id, username=username, company_name=company_name)


def check_professional_exist(nickname:str) -> bool:

    data = read_query(
        "SELECT username FROM professionals WHERE username = %s",
        (nickname,)
    )

    return bool(data)


def check_company_exist(company_name:str) -> bool:

    data = read_query(
        "SELECT username FROM companies WHERE username = %s",
        (company_name,)
    )

    return bool(data)