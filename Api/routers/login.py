from fastapi import APIRouter
from data.models.login import LoginData
from data.models.professional import Professional
from data.models.company import Company
from data.models.admin import Admin
from data.responses import BadRequest
from services import login_service, admin_service
from common.auth import create_prof_token, create_company_token, create_admin_token


login_router = APIRouter(prefix='/login')

@login_router.post('', tags=["Login"])
def login(login_data: LoginData):
    user = login_service.try_login(login_data.username, login_data.password)

    if isinstance(user, Professional):
        token = create_prof_token(user)
        return {'token': token}
    elif isinstance(user, Company):
        token = create_company_token(user)
        return {'token': token}
    elif isinstance(user, Admin):
        token = create_admin_token(user)
        return {'token': token}
    else:
        return BadRequest(content='Invalid login data')
    


@login_router.post('/professionals', tags=["Login"])
def login_professional(login_data: LoginData):
    user = login_service.try_login_as_prof(login_data.username, login_data.password)

    if user:
        token = create_prof_token(user)
        return {'token': token}
    else:
        return BadRequest(content='Invalid login data')


@login_router.post('/companies', tags=["Login"])
def login_company(login_data: LoginData):
    user = login_service.try_login_as_company(login_data.username, login_data.password)

    if user:
        token = create_company_token(user)
        return {'token': token}
    else:
        return BadRequest(content='Invalid login data')
    

@login_router.post('/admins', tags=["Login"])
def login_admin(login_data: LoginData):
    user = admin_service.try_login_as_admin(login_data.username, login_data.password)

    if user:
        token = create_admin_token(user)
        return {'token': token}
    else:
        return BadRequest(content='Invalid login data')