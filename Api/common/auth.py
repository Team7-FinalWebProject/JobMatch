import jwt
from common.secret import _JWT_SECRET
from data.responses import Unauthorized, ExpiredException, BadRequest
from data.models.company import Company
from data.models.professional import Professional
from data.models.user import User
from datetime import datetime, timedelta


def _base_auth(token: str) -> bool:
    '''
    Base function for authenticating.
    Verifies whether a token has expired
    !!!NOTE: This function is not to be used outside this module.
    '''
    payload = _is_authenticated(token)
    iat = datetime.strptime(payload["issued"], '%Y-%m-%d %H:%M:%S.%f')
    if iat > datetime.now() - timedelta(minutes=30): #TODO: time is set to 30min maybe change later?
        return payload
    else:
        return ExpiredException


def company_or_401(token: str) -> Company:
    '''Authenticate a company profile.
       Returns a Company object.'''
    try:
        payload = _base_auth(token)
        return Company.from_query_result(**payload)
    except ExpiredException:
        raise Unauthorized(status_code=401,
                            detail='Expired token.')
    except Exception:
        raise Unauthorized(status_code=401)
    

def professional_or_401(token: str) -> Professional:
    '''Authenticate a professional's profile.
       Returns a Professional object.'''
    try:
        payload = _base_auth(token)
        return Professional.from_query_result(**payload)
    except ExpiredException:
        raise Unauthorized(status_code=401,
                            detail='Expired token.')
    except Exception:
        raise Unauthorized(status_code=401)
    

def create_prof_token(prof: Professional) -> str:
    payload = {
        "id": prof.id,
        "user_id": prof.user_id,
        "first_name": prof.first_name,
        "last_name": prof.last_name,
        "address": prof.address,
        "issued": str(datetime.now())
    }

    return jwt.encode(payload, _JWT_SECRET, algorithm="HS256")


def create_company_token(comp: Company) -> str:
    payload = {
        "id": comp.id,
        "user_id": comp.user_id,
        "name": comp.name,
        "address": comp.address,
        "issued": str(datetime.now())
    }

    return jwt.encode(payload, _JWT_SECRET, algorithm="HS256")


def _is_authenticated(token: str) -> bool:
    return jwt.decode(token, _JWT_SECRET, algorithms=["HS256"])





# CURRENTLY OUT OF USE


# def user_or_401(token: str):
#     try:
#         payload = _base_auth(token)
#         return User.from_query_result(**payload)
#     except ExpiredException:
#         raise Unauthorized(content='Expired token.')
#     except Exception:
#         raise BadRequest(content='Unexpected error occured')
    