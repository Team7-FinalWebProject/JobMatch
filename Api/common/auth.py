import jwt
from fastapi import HTTPException
from data.responses import ExpiredException
from data.models.company import Company
from data.models.professional import Professional
from data.models.admin import Admin
from datetime import datetime, timedelta
import os
_JWT_SECRET = os.getenv('JWT_SECRET')
_ADMIN_MESSAGE = 'Cannot execute request. [MUST BE APPROVED BY ADMIN]'


def _base_auth(token: str):
    '''
    Base function for authenticating.
    Verifies whether a token has expired
    !!!NOTE: This function is not to be used outside this module.
    '''
    payload = _is_authenticated(token)
    iat = datetime.strptime(payload["issued"], '%Y-%m-%d %H:%M:%S.%f')
    if iat > datetime.now() - timedelta(weeks=2000): #TODO: time is set to 30min maybe change later?
        return payload
    else:
        raise ExpiredException


def company_or_401(token: str) -> Company:
    '''Authenticate a company profile.
       Returns a Company object.'''
    try:
        payload = _base_auth(token)
    except ExpiredException:
        return None
    try:
        company = Company.from_query_result(**payload)
        if company.approved == False:
            raise HTTPException(status_code=403, detail=_ADMIN_MESSAGE)
        return company
    except Exception as e:
        raise e
    

def professional_or_401(token: str) -> Professional:
    '''Authenticate a professional's profile.
       Returns a Professional object.'''
    try:
        payload = _base_auth(token)
    except ExpiredException:
        return None
    try:
        prof = Professional.from_query_result(**payload)
        if prof.approved == False:
            raise HTTPException(status_code=403, detail=_ADMIN_MESSAGE)
        return prof
    except Exception as e:
        raise e
    

def user_or_error(token: str) -> Company | Professional:
    '''Authenticate a profile
       Returns a Company/Professional object.'''
    try:
        payload = _base_auth(token)
    except ExpiredException:
        return None
    try:
        try:
            return Professional.from_query_result(**payload)
        except:
            try:
                return Company.from_query_result(**payload)
            except:
                return Admin.from_query_result(**payload)
    except Exception as e:
        raise e
    

def create_prof_token(prof: Professional) -> str:
    payload = {
        "id": prof.id,
        "user_id": prof.user_id,
        "default_offer_id": prof.default_offer_id,
        "first_name": prof.first_name,
        "last_name": prof.last_name,
        "summary": prof.summary,
        "address": prof.address,
        "picture": prof.picture,
        "status": prof.status,
        "username": prof.username,
        "approved": prof.approved,
        "issued": str(datetime.now())
    }

    return jwt.encode(payload, _JWT_SECRET, algorithm="HS256")


def create_company_token(comp: Company) -> str:
    payload = {
        "id": comp.id,
        "user_id": comp.user_id,
        "name": comp.name,
        "description": comp.description,
        "address": comp.address,
        "picture": comp.picture,
        "username": comp.username,
        "approved": comp.approved,
        "issued": str(datetime.now())
    }

    return jwt.encode(payload, _JWT_SECRET, algorithm="HS256")


def _is_authenticated(token: str):
    return jwt.decode(token, _JWT_SECRET, algorithms=["HS256"])

    
def create_admin_token(admin: Admin) -> str:
    payload = {
        "id": admin.id,
        "user_id": admin.id,
        "username": admin.username,
        "issued": str(datetime.now())
    }

    return jwt.encode(payload, _JWT_SECRET, algorithm="HS256")
    