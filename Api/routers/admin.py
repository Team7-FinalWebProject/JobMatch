from fastapi import APIRouter, Response
from services import search_service

admin_router = APIRouter(prefix='/admin')

##TODO: Public -> Private

@admin_router.get('/company/{id}')
def view_unapproved_company(id: int):
    return search_service.get_unapproved_company_by_id(id)

@admin_router.get('/companies')
def view_unapproved_companies():
    return search_service.get_unapproved_companies()

@admin_router.get('/professional/{id}')
def view_unapproved_professional(id: int):
    return search_service.get_unapproved_professional_by_id(id)

@admin_router.get('/professionals')
def view_unapproved_professionals():
    return search_service.get_unapproved_professionals()