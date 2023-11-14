from fastapi import APIRouter, Response
from services import search_service

##TODO: Temporary router, merge search router into professionals/companies when done
##TODO: Public -> Private
search_router = APIRouter(prefix='/search')

# --view company
@search_router.get('/company/{id}')
def view_company(id: int):
    pass

# --view all companies (+filters)
@search_router.get('/companies')
def view_companies():
    pass

# --view professional
@search_router.get('/professional/{id}')
def view_professional(id: int):
    pass

# --view all professionals (+filters)
@search_router.get('/professionals')
def view_professionals():
    pass

# --view company offer
@search_router.get('/company_offer/{id}')
def view_company_offer(id: int):
    pass

# --view all company offers (+filters, filters: active/inactive, salary, requirements, ++)
@search_router.get('/company_offers')
def view_company_offers():
    pass

# --view professional offer (hide hidden)
@search_router.get('/professional_offer/{id}')
def view_professional_offer(id: int):
    pass

# --view all professional offers (self, self=professional, filters: active/inactive)
# --view all professional offers (hide inactive, private and hidden) (+filters salary, requirements, ++)
@search_router.get('/professional_offers')
def view_professional_offers():
    pass

