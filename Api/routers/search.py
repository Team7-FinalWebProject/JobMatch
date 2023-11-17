from fastapi import APIRouter, Response
from services import search_service

##TODO: Temporary router, merge search router into professionals/companies when done
##TODO: Public -> Private
search_router = APIRouter(prefix='/search')

# --view company
@search_router.get('/company/{id}')
def view_approved_company(id: int):
    return search_service.get_approved_company_by_id(id)

# --view all companies (+filters)
@search_router.get('/companies')
def view_approved_companies():
    return search_service.get_approved_companies()

# --view professional
@search_router.get('/professional/{id}')
def view_approved_professional(id: int):
    return search_service.get_approved_professional_by_id(id)

# --view all professionals (+filters)
@search_router.get('/professionals')
def view_approved_professionals():
    return search_service.get_approved_professionals()

# --view company offer
@search_router.get('/company_offer/{id}')
def view_approved_company_offer(id: int):
    return search_service.get_approved_company_offer_by_id(id)

# --view all company offers (+filters, filters: active/inactive, salary, requirements, ++)
@search_router.get('/company_offers')
def view_approved_company_offers():
    return search_service.get_approved_company_offers()

# --view professional offer (hide hidden)
@search_router.get('/professional_offer/{id}')
def view_approved_professional_offer(id: int):
    return search_service.get_approved_professional_offer_by_id(id)

# --view all professional offers (self, self=professional, filters: active/inactive)
# --view all professional offers (hide inactive, private and hidden) (+filters salary, requirements, ++)
@search_router.get('/professional_offers')
def view_approved_professional_offers():
    return search_service.get_approved_professional_offers()

