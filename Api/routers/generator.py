from fastapi import APIRouter, Response, Header, Body
from services import generator_service
from common.auth import admin_or_error
from data.models.admin import ReadConfig, UpdateConfig
from common.skill_config import Config


generator_router = APIRouter(prefix='/generate')

@generator_router.post('/company', tags=["Generate"])
def fake_company(x_token: str = Header(), prompt: str | None = Body(default="Please suggest a json for a company user account!")):
    admin = admin_or_error(x_token)
    return generator_service.generate_company(prompt)

@generator_router.post('/professional', tags=["Generate"])
def fake_professional(x_token: str = Header(), prompt: str | None = Body(default="Please suggest a json for a professional user account!")):
    admin = admin_or_error(x_token)
    return generator_service.generate_professional(prompt)

@generator_router.post('/company_offer', tags=["Generate"])
def fake_company_offer(x_token: str, id: int = Header(), prompt: str | None = Body(default="Please suggest a json for a company job offer!")):
    admin = admin_or_error(x_token)
    return generator_service.generate_company_offer(id, prompt)

@generator_router.post('/professional_offer', tags=["Generate"])
def fake_professional_offer(x_token: str, id: int = Header(), prompt: str | None = Body(default="Please suggest a json for a professional bio!")):
    admin = admin_or_error(x_token)
    return generator_service.generate_professional_offer(id, prompt)
