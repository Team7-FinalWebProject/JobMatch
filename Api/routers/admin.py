
from fastapi import APIRouter, Response, Header
from services import search_service
from common.auth import user_or_401

admin_router = APIRouter(prefix='/admin')

##TODO: Throw error instead of if user.__class__.__name__ else None etc ?
@admin_router.get('/company/{id}', tags=["Admin"])
def view_unapproved_company(id: int, x_token: str = Header()):
    user = user_or_401(x_token)
    return search_service.admin_get_unapproved_company_by_id(id) if user.__class__.__name__ == 'Admin' else None

@admin_router.get('/companies', tags=["Admin"])
def view_unapproved_companies(x_token: str = Header()):
    user = user_or_401(x_token)
    return search_service.admin_get_unapproved_companies() if user.__class__.__name__ == 'Admin' else None

@admin_router.get('/professional/{id}', tags=["Admin"])
def view_unapproved_professional(id: int, x_token: str = Header()):
    user = user_or_401(x_token)
    return search_service.admin_get_unapproved_professional_by_id(id) if user.__class__.__name__ == 'Admin' else None

@admin_router.get('/professionals', tags=["Admin"])
def view_unapproved_professionals(x_token: str = Header()):
    user = user_or_401(x_token)
    return search_service.admin_get_unapproved_professionals() if user.__class__.__name__ == 'Admin' else None

