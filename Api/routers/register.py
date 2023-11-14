from fastapi import APIRouter, Header
from common.auth import user_or_401
from data.responses import BadRequest, Unauthorized
from data.models.register import RegisterUserData
from data.models.professional import Professional
from data.models.company import Company
from services import register_service


register_router = APIRouter(prefix='/register')


@register_router.post('/users', tags=["Signup"])
def register_user(user_data: RegisterUserData):
    if register_service.check_user_exist(user_data.username):
        return BadRequest(status_code=400, content=f'Username is already taken!')
    else:
        user = register_service.create_user(
            user_data.username, user_data.approved, user_data.password)
        return user


@register_router.post('/professionals', tags=["Signup"])
def register_professional(prof_data: Professional, x_token: str = Header(default=None)):
    user = user_or_401(x_token) if x_token else None
    if user:
        return register_service.create_professional(prof_data)
    else:
        return Unauthorized(content='Not logged in')
    

@register_router.post('/companies', tags=["Signup"])
def register_company(comp_data: Company, x_token: str = Header(default=None)):
    user = user_or_401(x_token) if x_token else None
    if user:
        return register_service.create_company(comp_data)
    else:
        return Unauthorized(content='Not logged in')
    
