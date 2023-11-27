from fastapi import APIRouter, Header, UploadFile, File
from data.models.company import Company
from data.models.offer import CompanyOfferCreate
from services import companies_service, professionals_service
from common.auth import company_or_401
from data.responses import BadRequest, Unauthorized, NotFound, Forbidden
from services.search_service import _get_professional_offer_by_id
from common.utils.file_uploader import create_upload_file




_ERROR_MESSAGE = 'You are not authorized [NOT LOGGED IN | TOKEN EXPIRED]'


companies_router = APIRouter(prefix='/companies')


@companies_router.put('/info', tags=['Companies'])
def edit_company(new_info: Company, x_token: str = Header(default=None)):
    company = company_or_401(x_token) if x_token else None
    if not company:
        return Unauthorized(content='Invalid token')
    return companies_service.edit_company_info(new_info, company)


@companies_router.post('/create_offer', tags=['Companies'])
def create_offer(new_offer: CompanyOfferCreate, x_token: str = Header(default=None)):
    company = company_or_401(x_token) if x_token else None
    if not company:
        return Unauthorized(content='Invalid token')
    return companies_service.create_company_offer(new_offer, company)




# {
#   "username": "KOKOOO",
#   "password": "BatDoko123@"
# }




# {
#   "status": "string",
#   "requirements": {"British": [7, "Native"], "Computers": [10, "Master"]},
#   "min_salary": 1000,
#   "max_salary": 2000
# }


@companies_router.put('/{company_offer_id}/edit_offer', tags=['Companies'])
def edit_comp_offer(new_offer: CompanyOfferCreate, 
                    company_offer_id: int,
                    x_token: str = Header(default=None)):
    company = company_or_401(x_token) if x_token else None
    if not company:
        return Unauthorized(content=_ERROR_MESSAGE)
    offer = companies_service.get_company_offer(company_offer_id, company.id)
    if not offer:
        return NotFound(content=f'No offer with id: {company_offer_id}')
    return companies_service.edit_company_offer(new_offer, offer)



@companies_router.post('/{company_offer_id}/{prof_offer_id}/request', tags=['Companies'])
def send_match_request_to_prof_offer(company_offer_id: int, prof_offer_id: int, x_token: str = Header(default=None)):
    company = company_or_401(x_token) if x_token else None

    company_offer_exist = companies_service.check_offer_exists(company_offer_id)


    if not company:
        return Unauthorized(content=_ERROR_MESSAGE)
    

    if company_offer_exist:
        company_offer_info = companies_service.get_company_offer(company_offer_id, company.id)
    else:
        return NotFound(content=f'No offer with id: {company_offer_id}')

    
    if company_offer_info.status != 'active':
        return Forbidden(content='Cannot send a match request when busy!')

    prof_offer = professionals_service.check_prof_offer_exists(prof_offer_id)

    if not prof_offer:
        return NotFound(content=f'No professional offer with id: {prof_offer_id}')
    
    prof_id = companies_service.get_prof_id_from_prof_offer_id(prof_offer_id)

    return companies_service.create_match_request(company_offer_id, prof_id, prof_offer_id)



@companies_router.post('/match', tags=['Companies'])
def match(prof_offer_id: int, company_offer_id: int, private_or_hidden = 'hidden', x_token: str = Header(default=None)):
    company = company_or_401(x_token) if x_token else None
    
    # if private_or_hidden not in ('hidden', 'private'):
    #     private_or_hidden = 'hidden'

    company_offer_exist = companies_service.check_offer_exists(company_offer_id)

    if not company:
        return Unauthorized(content=_ERROR_MESSAGE)
    
    if company_offer_exist:
        company_offer_info = companies_service.get_company_offer(company_offer_id, company.id)
    else:
        return NotFound(content=f'No offer with id: {company_offer_id}')
    
    if company_offer_info.status != 'active':
        return Forbidden(content='You have already matched an offer!')
    
    
    if not professionals_service.is_author(company.id, company_offer_id):
        return Forbidden(content=f'You are not the owner of offer {company_offer_id}')
    
    return professionals_service.match_comp_offer(prof_offer_id, company.id, company_offer_id, private_or_hidden)


@companies_router.post('/upload_photo', tags=['Companies'])
def create_upload_company_photo(myfile: UploadFile = File(...), x_token: str = Header(default=None)):
    company = company_or_401(x_token) if x_token else None
    if not company:
        return Unauthorized(content=_ERROR_MESSAGE)
    image_bytes = create_upload_file(myfile)
    return companies_service.upload_img(company, image_bytes)
