from fastapi import APIRouter
from data.models.login import LoginData
from data.responses import BadRequest
from services import login_service
from common.auth import create_token


login_router = APIRouter(prefix='/login')


@login_router.post('/professionals', tags=["Login"])
def login_professional(login_data: LoginData):
    user = login_service.try_login(login_data.username, login_data.password)

    if user:
        token = create_token(user)
        return {'token': token}
    else:
        return BadRequest(content='Invalid login data')


@login_router.post('/companies', tags=["Login"])
def login_company(login_data: LoginData):
    user = login_service.try_login(login_data.username, login_data.password)

    if user:
        token = create_token(user)
        return {'token': token}
    else:
        return BadRequest(content='Invalid login data')