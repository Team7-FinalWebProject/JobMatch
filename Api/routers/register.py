from fastapi import APIRouter
from data.responses import BadRequest, Conflict
from data.models.register import RegisterProfessionalData, RegisterCompanyData
from services import register_service


register_router = APIRouter(prefix='/register')


@register_router.post('/professionals', tags=["Signup"])
def register_professional(user_data: RegisterProfessionalData):
    if register_service.check_user_exist(user_data.username):
        return BadRequest(content=f'Username is already taken!')
    else:
        user, prof = register_service.create_professional(user_data)
        if not user and not prof:
            return Conflict(content='Unexpected error occured')
        else:
            return register_service.prof_response_object(user, prof)
        

@register_router.post('/companies', tags=["Signup"])
def register_company(comp_data: RegisterCompanyData):
    if register_service.check_user_exist(comp_data.username):
        return BadRequest(content=f'Username is already taken!')
    else:
        user, company = register_service.create_company(comp_data)
        if not user and not company:
            return Conflict(content='Unexpected error occured.')
        else:
            return register_service.company_response_object(user, company)

