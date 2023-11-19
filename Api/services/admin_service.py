from services.register_service import _hash_password
from secrets import compare_digest
from data.database import read_query, update_query
from data.models.admin import Admin, Config
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
    
def check_config():
    data = read_query(
        '''SELECT static_skills,min_level,max_level,baseline_skills,approved_skills,pending_approval_skills from config
           WHERE lock = %s''', ('X',))
    return reader_one(Config, data)

def set_config(data: Config):
    result = update_query(
        '''UPDATE config
        SET static_skills = COALESCE(%s, static_skills),
        min_level = COALESCE(%s, min_level),
        max_level = COALESCE(%s, max_level),
        baseline_skills = COALESCE(%s, baseline_skills)
        WHERE lock = %s''',
        (data.static_skills, data.min_level, data.max_level, data.baseline_skills, 'X',))
    ##TODO: check result and remodel
    return result
    
def approve_pending_skills():
    result = update_query(
        '''UPDATE config
        SET approved_skills = approved_skills || pending_approval_skills,
        pending_approval_skills = ARRAY[]::text[];
        WHERE lock = %s''', ('X',))
    ##TODO: check result and remodel
    return result
    
def discard_pending_skills():
    result = update_query(
        '''UPDATE config
        SET pending_approval_skills = ARRAY[]::text[];
        WHERE lock = %s''', ('X',))
    ##TODO: check result and remodel
    return result