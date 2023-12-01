from data.database import read_query, multi_read_query_transaction
from data.models.professional import Professional
from data.models.company import Company
from services.register_service import _hash_password
from secrets import compare_digest
from data.models.admin import Admin
from data.readers import reader_one



# def try_login_as_prof(username: str, password: str):
#     password1, user = find_prof_by_username(username)
#     if not user: return None
#     password_check = _hash_password(password)
#     return user if compare_digest(password1, password_check) else None


# def try_login_as_company(username: str, password: str):
#     password1, user = find_company_by_username(username)
#     if not user: return None
#     password_check = _hash_password(password)
#     return user if compare_digest(password1, password_check) else None

def try_login(username: str, password: str):
    password1, user = find_user_by_username(username)
    if not user: return None
    password_check = _hash_password(password)
    return user if compare_digest(password1, password_check) else None


def find_user_by_username(username: str):
    prof = read_query(
        '''SELECT u.id, p.id,
           p.user_id, p.default_offer_id, p.first_name,
           p.last_name, p.summary, p.address, 
           p.status, u.username, p.approved, u.password 
           FROM users AS u
           JOIN professionals AS p ON u.id = p.user_id
           WHERE u.username = %s''', (username,))
    
    comp = read_query(
        '''SELECT u.id, c.id, c.user_id, 
           c.name, c.description, c.address, 
           u.username, c.approved, u.password
           FROM users AS u
           JOIN companies AS c ON u.id = c.user_id
           WHERE u.username = %s''', (username,))
    
    admin = read_query(
        '''SELECT id, id, username, password from users
           WHERE username = %s''', (username,))
    
    if prof:
        password_bytes = bytes(prof[0][-1])
        password_string = password_bytes.decode('utf-8')
        return password_string, next(
            (Professional.from_query_result(*row[1:-1]) for row in prof), None)
    
    if comp:
        password_bytes = bytes(comp[0][-1])
        password_string = password_bytes.decode('utf-8')
        return password_string, next(
            (Company.from_query_result(*row[1:-1]) for row in comp), None)
    
    if admin:
        password_bytes = bytes(admin[0][-1])
        password_string = password_bytes.decode('utf-8')
        return password_string, reader_one(Admin, admin)
    
    else:
        return None, None


# def find_prof_by_username(username: str, fuser=False, fpassword=False):
#     data = read_query(
#         '''SELECT u.id, p.id,
#            p.user_id, p.default_offer_id, p.first_name,
#            p.last_name, p.summary, p.address,
#            p.picture, p.status, u.username, p.approved, u.password 
#            FROM users AS u
#            JOIN professionals AS p ON u.id = p.user_id
#            WHERE u.username = %s''', (username,))
    
#     if data and ~(fuser ^ fpassword):
#         password_bytes = bytes(data[0][-1])
#         password_string = password_bytes.decode('utf-8')
#         return password_string, next(
#             (Professional.from_query_result(*row[1:-1]) for row in data), None)
#     else:
#         return None, None
    

# def find_company_by_username(username: str, fuser=False, fpassword=False):
#     data = read_query(
#         '''SELECT u.id, c.id, c.user_id, 
#            c.name, c.description, c.address, c.picture, 
#            u.username, c.approved, u.password
#            FROM users AS u
#            JOIN companies AS c ON u.id = c.user_id
#            WHERE u.username = %s''', (username,))

#     if data and ~(fuser ^ fpassword):
#         password_bytes = bytes(data[0][-1])
#         password_string = password_bytes.decode('utf-8')
#         return password_string, next(
#             (Company.from_query_result(*row[1:-1]) for row in data), None)
#     else:
#         return None, None
