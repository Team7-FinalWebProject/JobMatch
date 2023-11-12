from fastapi import APIRouter, Response, Query
from services import login_service


login_router = APIRouter(prefix='/login')


@login_router.post('/professional', tags=["Login"])
def login(username: str = Query(), password: str = Query()):
    user = login_service.try_login(username, password)

    if user:
        token = login_service.create_token(user)
        return {'token': token}
    else:
        return Response(status_code=404, content='Invalid login data')
