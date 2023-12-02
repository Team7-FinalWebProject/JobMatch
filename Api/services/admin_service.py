from services.register_service import _hash_password
from secrets import compare_digest
from data.database import read_query, update_query
from data.models.admin import Admin, ReadConfig, UpdateConfig
from data.readers import reader_one, reader_many
from psycopg2.extras import Json
from common.skill_config import Config

def try_login_as_admin(username: str, password: str):
    password1, user = find_admin_by_username(username)
    if not user: return None
    password_check = _hash_password(password)
    return user if compare_digest(password1, password_check) else None

def find_admin_by_username(username: str):
    data = read_query(
        '''SELECT id, id, username, password from users
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
    return reader_one(ReadConfig, data)

def set_config(data: UpdateConfig):
    result = update_query(
        '''UPDATE config
        SET static_skills = COALESCE(%s, static_skills),
        min_level = COALESCE(%s, min_level),
        max_level = COALESCE(%s, max_level)
        WHERE lock = %s''',
        (data.static_skills, data.min_level, data.max_level, 'X',))
    Config.refresh_config()
    ##TODO: check result and remodel
    return result
    
def approve_pending_skills():
    result = update_query(
        '''UPDATE config
        SET approved_skills = approved_skills || pending_approval_skills,
        pending_approval_skills = %s
        WHERE lock = %s''', (Json({}), 'X'))
    ##TODO: check result and remodel
    return result

def discard_all_pending_skills():
    result = update_query(
        '''UPDATE config
        SET pending_approval_skills = %s
        WHERE lock = %s''', (Json({}), 'X'))
    ##TODO: check result and remodel
    return result

def discard_prepared_skills(skills):
    result = update_query(
        '''UPDATE config
        SET approved_skills = approved_skills - %s::text[]
        WHERE lock = %s''', (skills, 'X'))
    ##TODO: check result and remodel
    return result

def commit_prepared_skills():
    result = update_query(
        '''UPDATE config
        SET baseline_skills = (SELECT jsonb_object_agg(key, NULL::jsonb) FROM
            (SELECT key FROM
                (SELECT jsonb_object_keys(baseline_skills || approved_skills) AS key) AS keys) AS subquery),
        approved_skills = %s
        WHERE lock = %s''', (Json({}), 'X'))
    ##TODO: check result and remodel
    return result

def approve_professional(id):
    result = update_query(
        '''UPDATE professionals
        SET approved = %s
        WHERE id = %s''', ('t', id))

def approve_company(id):
    result = update_query(
        '''UPDATE companies
        SET approved = %s
        WHERE id = %s''', ('t', id))
    

def get_admin_by_id(id: int):
    data = read_query(
        '''SELECT id, id, username from users
            where admin = %s
            and id = %s''',
        (True, id))
    return reader_one(Admin, data)

def get_admins():
    data = read_query(
        '''SELECT id, id, username from users
            where admin = %s''',
        (True,))
    return reader_many(Admin, data)