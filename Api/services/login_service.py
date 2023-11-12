from data.database import read_query, insert_query, update_query, update_queries_transaction
from data.models import Professional, Company


def try_login_as_professional(username: str, password: str) -> Professional | None:
    user = find_professional_by_username(username)

    return user if user and user.password == password else None


def try_login_as_company(username: str, password: str) -> Company | None:
    user = find_company_by_username(username)

    return user if user and user.password == password else None


def find_professional_by_username(nickname: str) -> Professional | None:
    data = read_query(
        'SELECT * FROM professionals WHERE username = %s',
        (nickname,))

    return next((Professional.from_query_result(*row) for row in data), None)



def find_company_by_username(nickname: str) -> Company | None:
    data = read_query(
        'SELECT * FROM companies WHERE username = %s',
        (nickname,))

    return next((Company.from_query_result(*row) for row in data), None)
