from fastapi import APIRouter, Response, Header, Body
from services import search_service, admin_service
from common.auth import user_or_error
from common.auth import admin_or_error
from data.models.admin import ReadConfig, UpdateConfig


admin_router = APIRouter(prefix='/admin')

##TODO: Throw error instead of if user.__class__.__name__ else None etc ?
@admin_router.get('/company/{id}', tags=["Admin"])
def view_unapproved_company(id: int, x_token: str = Header()):
    admin = admin_or_error(x_token)
    return search_service.admin_get_unapproved_company_by_id(id) if admin.__class__.__name__ == 'Admin' else None

@admin_router.get('/companies', tags=["Admin"])
def view_unapproved_companies(x_token: str = Header()):
    admin = admin_or_error(x_token)
    return search_service.admin_get_unapproved_companies() if admin.__class__.__name__ == 'Admin' else None

@admin_router.get('/professional/{id}', tags=["Admin"])
def view_unapproved_professional(id: int, x_token: str = Header()):
    user = user_or_error(x_token)
    return search_service.admin_get_unapproved_professional_by_id(id) if user.__class__.__name__ == 'Admin' else None

@admin_router.get('/professionals', tags=["Admin"])
def view_unapproved_professionals(x_token: str = Header()):
    user = user_or_error(x_token)
    return search_service.admin_get_unapproved_professionals() if user.__class__.__name__ == 'Admin' else None

@admin_router.get('/config', tags=["Admin"])
def view_config(x_token: str = Header()):
    user = user_or_error(x_token)
    return admin_service.check_config() if user.__class__.__name__ == 'Admin' else None

@admin_router.patch('/config', tags=["Admin"])
def change_config(cfg: UpdateConfig = Body(default={"static_skills": False,"min_level": 0,"max_level": 10}), x_token: str = Header()):
    user = user_or_error(x_token)
    return admin_service.set_config(cfg) if user.__class__.__name__ == 'Admin' else None

@admin_router.post('/prepare_skills', tags=["Admin"])
def prepare_all_pending_skills(x_token: str = Header()):
    user = user_or_error(x_token)
    return admin_service.approve_pending_skills() if user.__class__.__name__ == 'Admin' else None

@admin_router.delete('/delete_pending', tags=["Admin"])
def discard_all_pending_skills(x_token: str = Header()):
    user = user_or_error(x_token)
    return admin_service.discard_all_pending_skills() if user.__class__.__name__ == 'Admin' else None

@admin_router.delete('/discard_prepared', tags=["Admin"])
def discard_prepared_skills(skills: list = Body(default=["Skill1", "Skill2"]), x_token: str = Header()):
    user = user_or_error(x_token)
    return admin_service.discard_prepared_skills([s.capitalize() for s in skills]) if user.__class__.__name__ == 'Admin' else None

@admin_router.post('/commit_skills', tags=["Admin"])
def commit_all_prepared_skills(x_token: str = Header()):
    user = user_or_error(x_token)
    return admin_service.commit_prepared_skills() if user.__class__.__name__ == 'Admin' else None

@admin_router.post('/approve_professional', tags=["Admin"])
def approve_professional_by_id(prof_id: int, x_token: str = Header()):
    admin = admin_or_error(x_token)
    return admin_service.approve_professional(prof_id) if admin.__class__.__name__ == 'Admin' else None


@admin_router.post('/approve_company', tags=["Admin"])
def approve_company_by_id(comp_id: int, x_token: str = Header()):
    admin = admin_or_error(x_token)
    return admin_service.approve_company(comp_id) if admin.__class__.__name__ == 'Admin' else None
