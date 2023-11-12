from fastapi import APIRouter, Response, Query
from services import register_service
# from common import auth

register_router = APIRouter(prefix='/register')


@register_router.post('/professionals', tags=["Signup"])
def register(username: str = Query(),
             first_name: str = Query(),
             last_name: str = Query(),
             password: str = Query(),
             ):
  
    if register_service.check_username_exist(username):
        return Response(status_code=400, content=f'Username is already taken!')
    else:
        user = register_service.create_user(username, first_name, last_name, password)
        return user
