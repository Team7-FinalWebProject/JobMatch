from services import messages_service
from services.register_service import check_user_exist
from fastapi import APIRouter, Header, Body
from data.responses import NotFound, Unauthorized, Forbidden
from data.models.message import Message
from common.auth import user_or_error, _ADMIN_MESSAGE
from data.models.admin import Admin


messages_router = APIRouter(prefix='/messages')
_ERROR_MESSAGE = 'You are not authorized [NOT LOGGED IN | TOKEN EXPIRED]'


#TODO Figure out a way to add audio recording ass message


@messages_router.post('/chatbot', tags=['Messages'])
def chatbot_conversation(text: str = Body(default=""), x_token: str = Header(default=None)):
    user = user_or_error(x_token) if x_token else None
    if user:
        return messages_service.create_bot_conv(text)
    return Unauthorized(content=_ERROR_MESSAGE)


@messages_router.get('/{receiver_username}', tags=['Messages'])
def view_user_messages(receiver_username: str, x_token: str = Header(default=None)):
    user = user_or_error(x_token) if x_token else None
    receiver = check_user_exist(receiver_username)
    if user:
        if isinstance(user, Admin) or user.approved == True:
            if receiver:
                messages = messages_service.get_messages(user.username, receiver_username)
                if not messages:
                    return NotFound(content=f'No messages with user: {receiver_username}')
                return messages
            else:
                return NotFound(content=f'No user with username: {receiver_username}')
        else:
            return Forbidden(content=_ADMIN_MESSAGE)    
    else:
        return Unauthorized(content=_ERROR_MESSAGE)
    

@messages_router.post('/{receiver_username}', tags=['Messages'])
def send_message(receiver_username: str, message: Message, x_token: str = Header(default=None)):
    user = user_or_error(x_token) if x_token else None
    receiver = check_user_exist(receiver_username)
    if user:
        if isinstance(user, Admin) or user.approved == True:
            if receiver:
                return messages_service.create(user.username, receiver_username, message)
            else:
                return NotFound(content=F'No user with username: {receiver_username}')
        else:
            return Forbidden(content=_ADMIN_MESSAGE)
    else:
        return Unauthorized(content=_ERROR_MESSAGE)