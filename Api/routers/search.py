from fastapi import APIRouter, Response, Header
from services import search_service
from common.auth import user_or_401, professional_or_401, company_or_401

##TODO: Temporary router, merge search router into professionals/companies when done
##TODO: Public -> Private
search_router = APIRouter(prefix='/search', tags=["Search"])
search_professional_router = APIRouter(prefix='/search', tags=["Search Professional"])
search_company_router = APIRouter(prefix='/search', tags=["Search Company"])

# --view company
@search_router.get('/company/{id}', tags=["Search"])
def view_approved_company(id: int, x_token: str = Header()):
    user = user_or_401(x_token)
    return search_service.search_get_company_by_id(id)

# --view all companies (+filters)
@search_router.get('/companies', tags=["Search"])
def view_approved_companies(x_token: str = Header()):
    user = user_or_401(x_token)
    return search_service.search_get_companies()

# --view professional
@search_router.get('/professional/{id}', tags=["Search"])
def view_approved_professional(id: int, x_token: str = Header()):
    user = user_or_401(x_token)
    return search_service.search_get_professional_by_id(id)

# --view all professionals (+filters)
@search_router.get('/professionals', tags=["Search"])
def view_approved_professionals(x_token: str = Header()):
    user = user_or_401(x_token)
    return search_service.search_get_professionals()

# --view company offer
@search_router.get('/company_offer/{id}', tags=["Search"])
def view_approved_company_offer(id: int, x_token: str = Header()):
    user = user_or_401(x_token)
    return search_service.search_get_company_offer_by_id(id)

# --view all company offers (+filters, filters: active/inactive, salary, requirements, ++)
@search_router.get('/company_offers', tags=["Search"])
def view_approved_company_offers(x_token: str = Header()):
    user = user_or_401(x_token)
    return search_service.search_get_company_offers()

# --view professional offer (hide hidden)
@search_router.get('/professional_offer/{id}', tags=["Search"])
def view_approved_professional_offer(id: int, x_token: str = Header()):
    user = user_or_401(x_token)
    return search_service.search_get_professional_offer_by_id(id)

# --view all professional offers (self, self=professional, filters: active/inactive)
# --view all professional offers (hide inactive, private and hidden) (+filters salary, requirements, ++)
@search_router.get('/professional_offers', tags=["Search"])
def view_approved_professional_offers(x_token: str = Header()):
    user = user_or_401(x_token)
    return search_service.search_get_professional_offers()

##TODO: Throw error instead of if user.__class__.__name__ else None etc ?
# ####Professional:
@search_professional_router.get('/professional_self_info', tags=["Search Professional"])
def view_approved_professional_self_info(x_token: str = Header()):
    user = user_or_401(x_token)
    return search_service.professional_get_self_info(user.id) if user.__class__.__name__ == 'Professional' else None

@search_professional_router.get('/professional_self_offer', tags=["Search Professional"])
def view_approved_hidden_professional_self_offer(id: int, x_token: str = Header()):
    user = user_or_401(x_token)
    return search_service.professional_get_self_offer_by_id(id, user.id) if user.__class__.__name__ == 'Professional' else None

@search_professional_router.get('/professional_self_offers', tags=["Search Professional"])
def view_approved_hidden_professional_self_offers(x_token: str = Header()):
    user = user_or_401(x_token)
    return search_service.professional_get_self_offers(user.id) if user.__class__.__name__ == 'Professional' else None

@search_professional_router.get('/professional_company_offer', tags=["Search Professional"])
def view_approved_active_company_offer(id:int, x_token: str = Header()):
    user = user_or_401(x_token)
    return search_service.professional_get_company_offer_by_id(id) if user.__class__.__name__ == 'Professional' else None

@search_professional_router.get('/professional_company_offers', tags=["Search Professional"])
def view_approved_active_company_offers(x_token: str = Header()):
    user = user_or_401(x_token)
    return search_service.professional_get_company_offers() if user.__class__.__name__ == 'Professional' else None

##TODO: Throw error instead of if user.__class__.__name__ else None etc ?
# ####Company:
@search_company_router.get('/company_self_info', tags=["Search Company"])
def view_approved_company_self_info(x_token: str = Header()):
    user = user_or_401(x_token)
    return search_service.company_get_self_info(user.id) if user.__class__.__name__ == 'Company' else None

@search_company_router.get('/company_self_offer', tags=["Search Company"])
def view_approved_archived_company_self_offer(id:int, x_token: str = Header()):
    user = user_or_401(x_token)
    return search_service.company_get_self_offer_by_id(id, user.id) if user.__class__.__name__ == 'Company' else None

@search_company_router.get('/company_self_offers', tags=["Search Company"])
def view_approved_archived_company_self_offers(x_token: str = Header()):
    user = user_or_401(x_token)
    return search_service.company_get_self_offers(user.id) if user.__class__.__name__ == 'Company' else None

@search_company_router.get('/company_professional_offer', tags=["Search Company"])
def view_approved_active_company_professional_offer(id:int,x_token: str = Header()):
    user = user_or_401(x_token)
    return search_service.company_get_professional_offer_by_id(id) if user.__class__.__name__ == 'Company' else None

@search_company_router.get('/company_professional_offers', tags=["Search Company"])
def view_approved_active_company_professional_offers(x_token: str = Header()):
    user = user_or_401(x_token)
    return search_service.company_get_professional_offers() if user.__class__.__name__ == 'Company' else None

