from fastapi import APIRouter, Response, Header, Body, Depends
from services import generator_service
from common.auth import admin_or_error
from data.models.admin import ReadConfig, UpdateConfig
from common.skill_config import Config


def validate_count(count: int = Header(default=1, ge=1, le=20)) -> int:
    return count

def validate_skillcount(count: int = Header(default=100, ge=30, le=1000)) -> int:
    return count

generator_router = APIRouter(prefix='/generate')

@generator_router.post('/company', tags=["Generate"])
def fake_company(x_token: str = Header(), count = Depends(validate_count), prompt: str | None = Body(default="Please suggest a json for a company user account!")):
    admin = admin_or_error(x_token)
    return generator_service.generate_company(prompt, count)

@generator_router.post('/professional', tags=["Generate"])
def fake_professional(x_token: str = Header(), count = Depends(validate_count), prompt: str | None = Body(default="Please suggest a json for a professional user account!")):
    admin = admin_or_error(x_token)
    return generator_service.generate_professional(prompt, count)

@generator_router.post('/company_offer', tags=["Generate"])
def fake_company_offer(x_token: str, id: int = Header(), count = Depends(validate_count), prompt: str | None = Body(default="Please suggest a json for a company job offer!")):
    admin = admin_or_error(x_token)
    return generator_service.generate_company_offer(id, prompt, count)

@generator_router.post('/professional_offer', tags=["Generate"])
def fake_professional_offer(x_token: str, id: int = Header(), count = Depends(validate_count), prompt: str | None = Body(default="Please suggest a json for a professional bio!")):
    admin = admin_or_error(x_token)
    return generator_service.generate_professional_offer(id, prompt, count)

@generator_router.put('/static_skills', tags=["Generate"])
def ai_skills_proposal(x_token: str = Header(), count = Depends(validate_skillcount), prompt: str | None = Body(default="Please suggest a json for CV skills!")):
    admin = admin_or_error(x_token)
    return generator_service.generate_skills_proposal(prompt, count)
