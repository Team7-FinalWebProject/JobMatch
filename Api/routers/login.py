from fastapi import APIRouter, Response, Query
from data.models import LoginData
from services import login_service
from common.auth import create_token

login_router = APIRouter(prefix='/login')


@login_router.post('/professional', tags=["Login"])
def login_as_professional(login_data: LoginData):
    user = login_service.try_login_as_professional(login_data.username, login_data.password)

    if user:
        token = create_token(user)
        return {'token': token}
    else:
        return Response(status_code=404, content='Invalid login data')


@login_router.post('/company', tags=["Login"])
def login_as_company(login_data: LoginData):
    user = login_service.try_login_as_company(login_data.username, login_data.password)

    if user:
        token = create_token(user)
        return {'token': token}
    else:
        return Response(status_code=404, content='Invalid login data')
