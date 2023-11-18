from fastapi import APIRouter, Header
from common.auth import professional_or_401
from data.responses import BadRequest, Unauthorized, NotFound
from data.models.professional import ProfessionalInfoEdit
from data.models.offer import ProfessionalOffer, ProfessionalOfferCreate
from services import professionals_service


professionals_router = APIRouter(prefix='/professionals')
_ERROR_MESSAGE = 'You are not authorized [NOT LOGGED IN | TOKEN EXPIRED]'


@professionals_router.put('/info')
def edit_info(new_info: ProfessionalInfoEdit, x_token: str = Header(default=None)):
    prof = professional_or_401(x_token) if x_token else None
    if not prof:
        return Unauthorized(content=_ERROR_MESSAGE)
    return professionals_service.edit(new_info, prof)
        

@professionals_router.put('/{offer_id}/default_offer')
def set_default_prof_offer(offer_id: int, x_token: str = Header(default=None)):
    prof = professional_or_401(x_token) if x_token else None
    offer = professionals_service.get_offer(offer_id, prof.id)
    if not prof:
        return Unauthorized(content=_ERROR_MESSAGE)
    if not offer:
        return BadRequest(content='You are not the owner or offer doesnt exist')
    return professionals_service.set_def_offer(offer_id, prof.id)


@professionals_router.post('/offer')
def create_offer(new_offer: ProfessionalOfferCreate, x_token: str = Header(default=None)):
    prof = professional_or_401(x_token) if x_token else None
    if not prof:
        return Unauthorized(content=_ERROR_MESSAGE)
    return professionals_service.create_offer(new_offer, prof)


@professionals_router.put('/{offer_id}/edit_offer')
def edit_prof_offer(new_offer: ProfessionalOffer, 
                    offer_id: int, 
                    x_token: str = Header(default=None)):
    prof = professional_or_401(x_token) if x_token else None
    offer = professionals_service.get_offer(offer_id, prof.id)
    if not prof:
        return Unauthorized(content=_ERROR_MESSAGE)
    if not offer:
        return NotFound(content=f'No offer with id: {offer_id}')
    return professionals_service.edit_offer(new_offer, offer)


@professionals_router.post('/match')
def create_match_request(x_token: str = Header(default=None)):
    prof = professional_or_401(x_token) if x_token else None
    if not prof:
        return Unauthorized(content=_ERROR_MESSAGE)
    return professionals_service.match()


@professionals_router.get('/requests')
def view_match_requests(x_token: str = Header(default=None)):
    prof = professional_or_401(x_token) if x_token else None
    offer = professionals_service.get_offers_by_prof_id(prof.id)
    if not prof:
        return Unauthorized(content='Invalid token')
    if not offer:
        return NotFound(content=f'No such offer for professional: {prof.id}')
    return professionals_service.get_requests(offer.id)


@professionals_router.put('/archive')
def archive_prof_offer(x_token: str = Header(default=None)):
    prof = professional_or_401(x_token) if x_token else None
    if not prof:
        return Unauthorized(content=_ERROR_MESSAGE)
        
    return professionals_service.archive_offer()