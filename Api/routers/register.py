from fastapi import APIRouter, Query
from data.responses import BadRequest
from data.models import RegisterCompanyData, RegisterProfessionalData
from services import register_service
# from common import auth

register_router = APIRouter(prefix='/register')


@register_router.post('/professionals', tags=["Signup"])
def register_as_professional(prof_data: RegisterProfessionalData):
    if register_service.check_professional_exist(prof_data.username):
        return BadRequest(status_code=400, content=f'Username is already taken!')
    else:
        user = register_service.create_professional(
            prof_data.username, prof_data.first_name, prof_data.last_name, prof_data.password)
        return user


@register_router.post('/companies', tags=["Signup"])
def register_as_company(reg_data: RegisterCompanyData):
    if register_service.check_company_exist(reg_data.username):
        return BadRequest(status_code=400, content=f'Username is already taken!')
    else:
        user = register_service.create_company(reg_data.username, reg_data.company_name, reg_data.password)
        return user
