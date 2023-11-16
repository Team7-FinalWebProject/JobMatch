from fastapi import APIRouter, Header
from common.auth import professional_or_401
from data.responses import BadRequest, Unauthorized
from data.models.professional import Professional
from data.models.offer import ProfessionalOffer
from services import professionals_service


professionals_router = APIRouter(prefix='/professionals')


@professionals_router.put('/info')
def edit_info(new_info: Professional, x_token: str = Header(default=None)):
    prof = professional_or_401(x_token) if x_token else None
    if not prof:
        return Unauthorized(content='Invalid token')
    return professionals_service.edit(new_info, prof)
        

@professionals_router.put('/default_offer')
def set_default_prof_offer(x_token: str = Header(default=None)):
    pass


@professionals_router.post('/offer')
def create_offer(new_offer: ProfessionalOffer, x_token: str = Header(default=None)):
    prof = professional_or_401(x_token) if x_token else None
    if not prof:
        return Unauthorized(content='Invalid token')
    return professionals_service.create_offer(new_offer, prof)


@professionals_router.put('/edit/offer')
def edit_prof_offer(x_token: str = Header(default=None)):
    pass


@professionals_router.post('/match')
def create_match_request(x_token: str = Header(default=None)):
    pass


@professionals_router.get('/requests')
def view_match_requests(x_token: str = Header(default=None)):
    pass


@professionals_router.put('/archive')
def archive_prof_offer(x_token: str = Header(default=None)):
    pass