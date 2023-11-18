from fastapi import APIRouter, Header
from data.models.company import Company
from data.models.offer import CompanyOffer
from services import companies_service
from common.auth import company_or_401
from data.responses import BadRequest, Unauthorized, NotFound



companies_router = APIRouter(prefix='/companies')


@companies_router.put('/info')
def edit_company(new_info: Company, x_token: str = Header(default=None)):
    company = company_or_401(x_token) if x_token else None
    if not company:
        return Unauthorized(content='Invalid token')
    return companies_service.edit_company_info(new_info, company)


@companies_router.post('/create_offer')
def create_offer(new_offer: CompanyOffer, x_token: str = Header(default=None)):
    company = company_or_401(x_token) if x_token else None
    if not company:
        return Unauthorized(content='Invalid token')
    return companies_service.create_company_offer(new_offer)