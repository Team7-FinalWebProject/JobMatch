from fastapi import APIRouter, Response, Query
from services import login_service
from common.auth import create_token

login_router = APIRouter(prefix='/login')


@login_router.post('/professional', tags=["Login"])
def login_as_professional(username: str = Query(), password: str = Query()):
    user = login_service.try_login_as_professional(username, password)

    if user:
        token = create_token(user)
        return {'token': token}
    else:
        return Response(status_code=404, content='Invalid login data')


@login_router.post('/company', tags=["Login"])
def login_as_company(username: str = Query(), password: str = Query()):
    user = login_service.try_login_as_company(username, password)

    if user:
        token = create_token(user)
        return {'token': token}
    else:
        return Response(status_code=404, content='Invalid login data')
