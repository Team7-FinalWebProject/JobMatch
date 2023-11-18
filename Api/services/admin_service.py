from services.register_service import _hash_password
from secrets import compare_digest
from data.database import read_query
from data.models.admin import Admin
from data.readers import reader_one

def try_login_as_admin(username: str, password: str):
    password1, user = find_admin_by_username(username)
    if not user: return None
    password_check = _hash_password(password)
    return user if compare_digest(password1, password_check) else None

def find_admin_by_username(username: str):
    data = read_query(
        '''SELECT id, username, password from users
           WHERE username = %s''', (username,))
    
    if data:
        password_bytes = bytes(data[0][-1])
        password_string = password_bytes.decode('utf-8')
        return password_string, reader_one(Admin, data)
    else:
        return None, None