import jwt
from common.secret import _JWT_SECRET
from data.responses import Unauthorized, ExpiredException
from data.models.company import Company
from data.models.professional import Professional
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


def create_token(user: Company | Professional) -> str:
    payload = {
        "id": user.id,
        "username": user.username,
        "registration_date": user.registration_date.strftime("%Y-%m-%d %H:%M:%S"), #TODO: see if needed! 
        "issued": str(datetime.now())
    }

    return jwt.encode(payload, _JWT_SECRET, algorithm="HS256")


def _is_authenticated(token: str) -> bool:
    return jwt.decode(token, _JWT_SECRET, algorithms=["HS256"])