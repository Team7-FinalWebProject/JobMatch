from fastapi import APIRouter
from data.responses import BadRequest
from data.models import RegisterUserData
from services import register_service


register_router = APIRouter(prefix='/register')


@register_router.post('/professionals', tags=["Signup"])
def register_as_professional(user_data: RegisterUserData):
    if register_service.check_user_exist(user_data.username):
        return BadRequest(status_code=400, content=f'Username is already taken!')
    else:
        user = register_service.create_user(
            user_data.username, user_data.approved, user_data.password)
        return user


@register_router.post('/companies', tags=["Signup"])
def register_as_company_user(reg_data: RegisterUserData):
    if register_service.check_company_exist(reg_data.username):
        return BadRequest(status_code=400, content=f'Username is already taken!')
    else:
        user = register_service.create_company(reg_data.username, reg_data.company_name, reg_data.password)
        return user
