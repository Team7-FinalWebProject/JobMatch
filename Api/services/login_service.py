from data.database import read_query
from data.models.professional import Professional
from data.models.company import Company
from data.models.user import User
from services.register_service import _hash_password
from secrets import compare_digest



def try_login(username: str, password: str):
    password1, user = find_by_username(username)
    password_check = _hash_password(password)
    return user if compare_digest(password1, password_check) else None


def find_by_username(nickname: str, fuser=False, fpassword=False):
    data = read_query(
        '''SELECT u.id, u.username, u.approved, u.admin, u.password 
           FROM users u WHERE username = ?''',
        (nickname,))

    if data and ~(fuser ^ fpassword): #TODO: See if this could be achieved without negation
        return data[0][-1].decode('utf-8'), next(
            (User.from_query_result(*row[:-1]) for row in data), None)
    else:
        return None, None
















# CURRENTLY NOT IN USE DUE TO User entity in db

# def find_company_by_username(nickname: str) -> Company | None:
#     data = read_query(
#         'SELECT * FROM companies WHERE username = ?',
#         (nickname,))

#     return next((Company.from_query_result(*row) for row in data), None)

# def try_login_as_professional(username: str, password: str) -> Professional | None:
#     user = find_professional_by_username(username)
#     password_2 = _hash_password(password)
#     return user if compare_digest(user.password, password_2) else None


# def try_login_as_company(username: str, password: str) -> Company | None:
#     user = find_company_by_username(username)
#     password_2 = _hash_password(password)
#     return user if compare_digest(user.password, password_2) else None