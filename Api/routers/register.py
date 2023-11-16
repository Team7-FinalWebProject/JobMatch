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
        if not user_data.password:
            prof = register_service.create_professional(user_data, 
                                                              register_service.generate_random_password(user_data))
        else:
            prof = register_service.create_professional(user_data, user_data.password)
        if not prof:
            return Conflict(content='Unexpected error occured')
        else:
            return register_service.prof_response_object(user_data, prof)
        

@register_router.post('/companies', tags=["Signup"])
def register_company(comp_data: RegisterCompanyData):
    if register_service.check_user_exist(comp_data.username):
        return BadRequest(content=f'Username is already taken!')
    else:
        if not comp_data.password:
            company = register_service.create_company(comp_data, 
                                                            register_service.generate_random_password(comp_data))
        else:
            company = register_service.create_company(comp_data, comp_data.password)
        if not company:
            return Conflict(content='Unexpected error occured.')
        else:
            return register_service.company_response_object(comp_data, company)

