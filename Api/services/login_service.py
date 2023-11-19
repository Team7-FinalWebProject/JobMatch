from data.database import read_query
from data.models.professional import Professional
from data.models.company import Company
from services.register_service import _hash_password
from secrets import compare_digest



def try_login_as_prof(username: str, password: str):
    password1, user = find_prof_by_username(username)
    if not user: return None
    password_check = _hash_password(password)
    return user if compare_digest(password1, password_check) else None


def try_login_as_company(username: str, password: str):
    password1, user = find_company_by_username(username)
    if not user: return None
    password_check = _hash_password(password)
    return user if compare_digest(password1, password_check) else None


def find_prof_by_username(username: str, fuser=False, fpassword=False):
    data = read_query(
        '''SELECT u.id, p.id,
           p.user_id, p.default_offer_id, p.first_name,
           p.last_name, p.summary, p.address,
           p.picture, p.status, u.username, u.password 
           FROM users AS u
           JOIN professionals AS p ON u.id = p.user_id
           WHERE u.username = %s''', (username,))
    
    if data and ~(fuser ^ fpassword):
        password_bytes = bytes(data[0][-1])
        password_string = password_bytes.decode('utf-8')
        return password_string, next(
            (Professional.from_query_result(*row[1:-1]) for row in data), None)
    else:
        return None, None
    

def find_company_by_username(username: str, fuser=False, fpassword=False):
    data = read_query(
        '''SELECT u.id, c.id, c.user_id, 
           c.name, c.description, c.address, c.picture, u.username, u.password
           FROM users AS u
           JOIN companies AS c ON u.id = c.user_id
           WHERE u.username = %s''', (username,))

    if data and ~(fuser ^ fpassword):
        password_bytes = bytes(data[0][-1])
        password_string = password_bytes.decode('utf-8')
        return password_string, next(
            (Company.from_query_result(*row[1:-1]) for row in data), None)
    else:
        return None, None
