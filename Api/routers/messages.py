from services import messages_service
from fastapi import APIRouter
from data.responses import NotFound, Success, Unauthorized, Forbidden
from data.models import Message
from common.auth import professional_or_401, company_or_401


messages_router = APIRouter(prefix='/messages')

#TODO Figure out a way to add audio recording ass message

@messages_router.post('/{receiver_id}')
def send_message(receiver_id: int, x_token: str, message: Message):
    prof = professional_or_401(x_token) if x_token else None
    comp = company_or_401(x_token) if x_token else None

    if prof:
        return messages_service.create(prof, receiver_id, message)
    else:
        return messages_service.create(comp, receiver_id, message)
        