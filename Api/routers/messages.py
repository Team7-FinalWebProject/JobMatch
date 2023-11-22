from services import messages_service
from services.register_service import check_user_exist
from fastapi import APIRouter, Header
from data.responses import NotFound, Unauthorized
from data.models.message import Message
from common.auth import user_or_error


messages_router = APIRouter(prefix='/messages')
_ERROR_MESSAGE = 'You are not authorized [NOT LOGGED IN | TOKEN EXPIRED]'


#TODO Figure out a way to add audio recording ass message
#TODO See for the most optimal way to aquire the user.


@messages_router.get('/{receiver_username}')
def view_user_messages(receiver_username: str, x_token: str = Header(default=None)):
    user = user_or_error(x_token) if x_token else None
    receiver = check_user_exist(receiver_username)
    if user:
        if receiver:
            sender_username = messages_service.extract_username(user)
            messages = messages_service.get_messages(sender_username, receiver_username)
            if not messages:
                return NotFound(content=f'No messages with user: {receiver_username}')
            return messages
        else:
            return NotFound(content=f'No user with username: {receiver_username}')    
    else:
        return Unauthorized(content=_ERROR_MESSAGE)
    

@messages_router.post('/{receiver_username}')
def send_message(receiver_username: str, message: Message, x_token: str = Header(default=None)):
    user = user_or_error(x_token) if x_token else None
    receiver = check_user_exist(receiver_username)
    if user:
        if receiver:
            sender_username = messages_service.extract_username(user)
            return messages_service.create(sender_username, receiver_username, message)
        else:
            return NotFound(content=F'No user with username: {receiver_username}')
    else:
        return Unauthorized(content=_ERROR_MESSAGE)