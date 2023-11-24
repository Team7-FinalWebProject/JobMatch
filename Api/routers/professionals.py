from fastapi import APIRouter, Header
from common.auth import professional_or_401
from data.responses import BadRequest, Unauthorized, NotFound, Forbidden
from data.models.professional import ProfessionalInfoEdit, ProfStatusSetter
from data.models.offer import ProfessionalOfferCreate, ProfessionalOffer, ProfessionalOfferEdit
from services import professionals_service
from services.companies_service import check_offer_exists
from services.search_service import _get_company_offer_by_id


professionals_router = APIRouter(prefix='/professionals')
_ERROR_MESSAGE = 'You are not authorized [NOT LOGGED IN | TOKEN EXPIRED | NOT APPROVED]'


@professionals_router.put('/info', tags=['Professional'])
def edit_info(new_info: ProfessionalInfoEdit, x_token: str = Header(default=None)):
    prof = professional_or_401(x_token) if x_token else None
    if not prof:
        return Unauthorized(content=_ERROR_MESSAGE)
    return professionals_service.edit(new_info, prof)
        

@professionals_router.put('/{offer_id}/default_offer', tags=['Professional'])
def set_default_prof_offer(offer_id: int, x_token: str = Header(default=None)):
    prof = professional_or_401(x_token) if x_token else None
    offer = professionals_service.get_offer(offer_id, prof.id)
    if not prof:
        return Unauthorized(content=_ERROR_MESSAGE)
    if not offer:
        return BadRequest(content='You are not the owner or offer doesnt exist')
    return professionals_service.set_def_offer(offer_id, prof.id)


@professionals_router.post('/offer', tags=['Professional'])
def create_offer(new_offer: ProfessionalOfferCreate, x_token: str = Header(default=None)):
    prof = professional_or_401(x_token) if x_token else None
    if not prof:
        return Unauthorized(content=_ERROR_MESSAGE)
    if prof.status != 'active':
        return Forbidden(content='Cannot create offers when busy!')
    return professionals_service.create_offer(new_offer, prof)


@professionals_router.put('/{offer_id}/edit_offer', tags=['Professional'])
def edit_prof_offer(new_offer: ProfessionalOfferEdit, 
                    offer_id: int, 
                    x_token: str = Header(default=None)):
    prof = professional_or_401(x_token) if x_token else None
    if not prof:
        return Unauthorized(content=_ERROR_MESSAGE)
    offer = professionals_service.get_offer(offer_id, prof.id)
    if not offer:
        return NotFound(content=f'No offer with id: {offer_id}')
    return professionals_service.edit_offer(new_offer, offer)


@professionals_router.post('/{company_offer_id}/{prof_offer_id}/requests', tags=['Professional'])
def send_match_request(company_offer_id: int, prof_offer_id: int, x_token: str = Header(default=None)):
    prof = professional_or_401(x_token) if x_token else None
    if not prof:
        return Unauthorized(content=_ERROR_MESSAGE)
    if prof.status != 'active':
        return Forbidden(content='Cannot send a match request when busy!')
    prof_offer = professionals_service.get_offer(prof_offer_id, prof.id)
    if not prof_offer:
        return NotFound(content=f'No such offer for professional: {prof.id}')
    comp_offer = check_offer_exists(company_offer_id)
    if not comp_offer:
        return NotFound(content=f'No offer with id: {company_offer_id}')
    request = professionals_service.create_match_request(prof_offer_id, company_offer_id)
    if not request:
        return Forbidden(content='Cannot send the same offer to the same company twice')
    return request


@professionals_router.post('/match', tags=['Professional'])
def match(offer_id: int, comp_offer_id: int, private_or_hidden = 'hidden', x_token: str = Header(default=None)):
    prof = professional_or_401(x_token) if x_token else None
    if private_or_hidden not in ('hidden', 'private'):
        private_or_hidden = 'hidden'
    if not prof:
        return Unauthorized(content=_ERROR_MESSAGE)
    if prof.status != 'active':
        return Forbidden(content='You have already matched an offer!')
    comp_offer = check_offer_exists(comp_offer_id)
    if not comp_offer:
        return NotFound(content=f'No offer with id: {comp_offer_id}')
    if not professionals_service.is_author(prof.id, offer_id):
        return Forbidden(content=f'You are not the owner of offer {offer_id}')
    return professionals_service.match_comp_offer(offer_id, prof.id, comp_offer_id, private_or_hidden)


@professionals_router.put('/status', tags=['Professional'])
def set_offer_status(offer_id: int, status: ProfStatusSetter, x_token: str = Header(default=None)):
    prof = professional_or_401(x_token) if x_token else None
    if not prof:
        return Unauthorized(content=_ERROR_MESSAGE)
    offer = professionals_service.get_offer(offer_id, prof.id)
    if not offer:
        return NotFound(content=f'No offer with id: {offer_id}')
    return professionals_service.set_status(prof.id, offer.id, status)