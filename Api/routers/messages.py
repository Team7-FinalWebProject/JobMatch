from services import messages_service
from fastapi import APIRouter, Header
from data.responses import NotFound, Success, Unauthorized, Forbidden
from data.models import Message
from common.auth import professional_or_401, company_or_401


messages_router = APIRouter(prefix='/messages')
_ERROR_MESSAGE = 'You are not logged in!'

#TODO Figure out a way to add audio recording ass message


@messages_router.get('/{company_username}')
def view_professional_messages(company_username: str, x_token: str = Header(default=None)):
    prof = professional_or_401(x_token) if x_token else None

    if prof:
        return messages_service.get_prof_messages(prof, company_username)
    else:
        return Unauthorized(content=_ERROR_MESSAGE)


@messages_router.get('/{prof_username}')
def view_company_messages(prof_username: str, x_token: str = Header(default=None)):
    company = company_or_401(x_token) if x_token else None

    if company:
        return messages_service.get_comp_messages(company, prof_username)
    else:
        return Unauthorized(content=_ERROR_MESSAGE)
    

@messages_router.post('/{receiver_username}')
def send_message(receiver_username: str, message: Message, x_token: str = Header(default=None)):
    prof = professional_or_401(x_token) if x_token else None
    comp = company_or_401(x_token) if x_token else None

    if prof:
        return messages_service.create(prof, receiver_username, message)
    elif comp:
        return messages_service.create(comp, receiver_username, message)
    else:
        return Unauthorized(content=_ERROR_MESSAGE)