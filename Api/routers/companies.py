from fastapi import APIRouter, Header
from data.models.company import Company
from data.models.offer import CompanyOfferCreate
from services import companies_service
from common.auth import company_or_401
from data.responses import BadRequest, Unauthorized, NotFound


_ERROR_MESSAGE = 'You are not authorized [NOT LOGGED IN | TOKEN EXPIRED]'


companies_router = APIRouter(prefix='/companies')


@companies_router.put('/info')
def edit_company(new_info: Company, x_token: str = Header(default=None)):
    company = company_or_401(x_token) if x_token else None
    if not company:
        return Unauthorized(content='Invalid token')
    return companies_service.edit_company_info(new_info, company)


@companies_router.post('/create_offer')
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


@companies_router.put('/{offer_id}/edit_offer')
def edit_comp_offer(new_offer: CompanyOfferCreate, 
                    offer_id: int, 
                    x_token: str = Header(default=None)):
    company = company_or_401(x_token) if x_token else None
    if not company:
        return Unauthorized(content=_ERROR_MESSAGE)
    offer = companies_service.get_company_offer(offer_id, company.id)
    if not offer:
        return NotFound(content=f'No offer with id: {offer_id}')
    return companies_service.edit_company_offer(new_offer, offer)
