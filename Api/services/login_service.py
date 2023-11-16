from data.database import read_query
from data.models.professional import Professional
from data.models.company import Company
from data.models.user import User
from services.register_service import _hash_password
from secrets import compare_digest



def try_login_as_prof(username: str, password: str):
    password1, user = find_prof_by_username(username)
    password_check = _hash_password(password)
    return user if compare_digest(password1, password_check) else None


def try_login_as_company(username: str, password: str):
    password1, user = find_company_by_username(username)
    password_check = _hash_password(password)
    return user if compare_digest(password1, password_check) else None


def find_prof_by_username(username: str, fuser=False, fpassword=False):
    data = read_query(
        '''SELECT u.id, u.username, p.*, u.password 
           FROM users AS u
           JOIN professionals AS p ON u.id = p.user_id
           WHERE u.username = %s''', (username,))
    
    if data and ~(fuser ^ fpassword):
        return data[0][-1].decode('utf-8'), next(
            (Professional.from_query_result(*row[2:-1]) for row in data), None)
    else:
        return None, None
    

def find_company_by_username(username: str, fuser=False, fpassword=False):
    data = read_query(
        '''SELECT u.id, u.username, c.*, u.password
           FROM users AS u
           JOIN companies AS c ON u.id = c.user_id
           WHERE u.username = %s''', (username,))
    
    if data and ~(fuser ^ fpassword):
        return data[0][-1].decode('utf-8'), next(
            (Company.from_query_result(*row[2:-1]) for row in data), None)
    else:
        return None, None





# DICONTINUED


# def find_by_username(nickname: str, fuser=False, fpassword=False):
#     data = read_query(
#         '''SELECT u.id, u.username, u.approved, u.admin, u.password 
#            FROM users u WHERE username = ?''',
#         (nickname,))

#     if data and ~(fuser ^ fpassword): #TODO: See if this could be achieved without negation
#         return data[0][-1].decode('utf-8'), next(
#             (User.from_query_result(*row[:-1]) for row in data), None)
#     else:
#         return None, None
