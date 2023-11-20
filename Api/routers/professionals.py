from fastapi import APIRouter, Header
from common.auth import professional_or_401
from data.responses import BadRequest, Unauthorized, NotFound, Forbidden
from data.models.professional import ProfessionalInfoEdit
from data.models.offer import ProfessionalOffer, ProfessionalOfferCreate
from services import professionals_service
from services.companies_service import check_offer_exists


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
    if prof.status != 'active':
        return Forbidden(content='Cannot create offers when busy!')
    return professionals_service.create_offer(new_offer, prof)


@professionals_router.put('/{offer_id}/edit_offer')
def edit_prof_offer(new_offer: ProfessionalOfferCreate, 
                    offer_id: int, 
                    x_token: str = Header(default=None)):
    prof = professional_or_401(x_token) if x_token else None
    if not prof:
        return Unauthorized(content=_ERROR_MESSAGE)
    offer = professionals_service.get_offer(offer_id, prof.id)
    if not offer:
        return NotFound(content=f'No offer with id: {offer_id}')
    return professionals_service.edit_offer(new_offer, offer)


@professionals_router.get('/requests')
def view_match_requests(x_token: str = Header(default=None)):
    prof = professional_or_401(x_token) if x_token else None
    if not prof:
        return Unauthorized(content='Invalid token')
    offers = professionals_service.get_offers_by_prof_id(prof.id)
    if not offers:
        return NotFound(content=f'No such offer for professional: {prof.id}')
    return professionals_service.get_requests(list(offers), prof.id)


@professionals_router.post('/{company_offer_id}/{prof_offer_id}/requests')
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
    return professionals_service.create_match_request(prof.id, prof_offer_id, company_offer_id)


@professionals_router.post('/match')
def match(offer_id: int, comp_offer_id: int, x_token: str = Header(default=None)):
    prof = professional_or_401(x_token) if x_token else None
    if not prof:
        return Unauthorized(content=_ERROR_MESSAGE)
    if prof.status != 'active':
        return Forbidden(content='You have already matched an offer!')
    comp_offer = check_offer_exists(comp_offer_id)
    if not comp_offer:
        return NotFound(content=f'No offer with id: {comp_offer_id}')
    return professionals_service.match_comp_offer(offer_id, prof.id, comp_offer_id)



# Maybe no need for these? 

@professionals_router.put('/status')
def set_status(x_token: str = Header(default=None)):
    pass


@professionals_router.put('/archive')
def archive_prof_offer(x_token: str = Header(default=None)):
    prof = professional_or_401(x_token) if x_token else None
    if not prof:
        return Unauthorized(content=_ERROR_MESSAGE)
        
    return professionals_service.archive_offer()