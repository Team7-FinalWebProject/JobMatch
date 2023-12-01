from fastapi import APIRouter, Header, UploadFile, File
from data.models.company import Company, CompanyInfoEdit
from data.models.offer import CompanyOfferCreate, CompanyOffer
from services import companies_service, professionals_service
from common.auth import company_or_401
from data.responses import BadRequest, Unauthorized, NotFound, Forbidden
from common.utils.file_uploader import create_upload_file




_ERROR_MESSAGE = 'You are not authorized [NOT LOGGED IN | TOKEN EXPIRED]'


companies_router = APIRouter(prefix='/companies')


@companies_router.put('/info', tags=['Companies'])
def edit_company(new_info: CompanyInfoEdit, x_token: str = Header(default=None)):
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
def edit_comp_offer(new_offer: CompanyOffer, 
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
    
    return companies_service.create_match_request(company_offer_id, prof_offer_id)



@companies_router.post('/match', tags=['Companies'])
def match(offer_id: int, prof_offer_id: int, private_or_hidden = 'hidden', x_token: str = Header(default=None)):
    company = company_or_401(x_token) if x_token else None
    if private_or_hidden not in ('hidden', 'private'):
        private_or_hidden = 'hidden'
    if not company:
        return Unauthorized(content=_ERROR_MESSAGE)
    # if company.status == 'busy':
    #     return Forbidden(content='You have already matched an offer!')
    prof_offer = professionals_service.check_prof_offer_exists(prof_offer_id)
    if not prof_offer:
        return NotFound(content=f'No professional offer with id: {prof_offer}')
    if not companies_service.is_author(company.id, offer_id):
        return Forbidden(content=f'You are not the owner of offer {offer_id}')
    prof_id = companies_service.get_prof_id_from_prof_offer_id(prof_offer_id)
    
    # match = companies_service.match_prof_offer(offer_id, prof_id, prof_offer_id, private_or_hidden)
    
    companies_service.match_prof_offer(offer_id, prof_id, prof_offer_id, private_or_hidden)
    
    # if match is True:
    #     mail_data = data_input(os.getenv('sender_email'), prof.username, 'usermail@mailsac.com')
    #     result = mailjet.send.create(mail_data)
    #     print(result.status_code)
    #     print(result.json())
    return f'Matched with company offer: {prof_offer_id}'







# eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6NSwidXNlcl9pZCI6MTAsIm5hbWUiOiJHb3Nob0tvbSIsImRlc2NyaXB0aW9uIjoic3RyaW5nIiwiYWRkcmVzcyI6InN0cmluZyIsInBpY3R1cmUiOm51bGwsInVzZXJuYW1lIjoiR29zaG8iLCJhcHByb3ZlZCI6ZmFsc2UsImlzc3VlZCI6IjIwMjMtMTEtMzAgMTY6MTg6MjkuODQ0NjIwIn0.YAsEcCv3fCCPTGmLgXqqmodupqJpSNW1Zz_8OXDyHiI



@companies_router.put('/offer_status', tags=['Companies'])
def set_offer_status(offer_id: int, status: str, x_token: str = Header(default=None)):
    company = company_or_401(x_token) if x_token else None
    if not company:
        return Unauthorized(content=_ERROR_MESSAGE)
    offer = companies_service.get_company_offer(offer_id, company.id)
    if not offer:
        return NotFound(content=f'No offer with id: {offer_id}')
    return companies_service.set_status(company.id, offer.id, status)


@companies_router.get('/match_requests', tags=['Companies'])
def get_match_requests(x_token: str = Header(default=None)):
    company = company_or_401(x_token) if x_token else None
    if not company:
        return Unauthorized(content=_ERROR_MESSAGE)
    return companies_service.get_match_requests(company)







@companies_router.post('/upload_photo', tags=['Companies'])
def create_upload_company_photo(myfile: UploadFile = File(...), x_token: str = Header(default=None)):
    company = company_or_401(x_token) if x_token else None
    if not company:
        return Unauthorized(content=_ERROR_MESSAGE)
    image_path = create_upload_file(myfile)
    return companies_service.upload_img(company, image_path)
