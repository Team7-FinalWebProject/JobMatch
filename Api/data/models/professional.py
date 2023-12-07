from pydantic import BaseModel
from data.models.offer import ProfessionalOffer_NoProfessionalId
from datetime import datetime
from typing import Any



class Professional(BaseModel):
    id: int | None = None
    user_id: int | None = None
    default_offer_id: int | None = None
    first_name: str
    last_name: str
    summary: str | None = None
    address: str
    status: str | None = None
    username: str | None = None
    approved: bool | None = None
    issued: datetime | None = None
    user_type: Any | None = None

    @classmethod
    def from_query_result(cls, id, user_id, default_offer_id, first_name, last_name, summary, address, status, username, approved, issued=None, user_type=None):
        return cls(
            id=id,
            user_id=user_id,
            default_offer_id=default_offer_id,
            first_name=first_name,
            last_name=last_name,
            summary=summary,
            address=address,
            status=status,
            username=username,
            approved=approved)
    

class Professional_Slim(BaseModel):
    id: int | None = None
    username: str
    default_offer_id: int | None = None
    first_name: str
    last_name: str
    summary: str
    address: str
    status: str = None

    @classmethod
    def from_query_result(cls, id, username, default_offer_id, first_name, last_name, summary, address, status):
        return cls(
            id=id,
            username=username,
            default_offer_id=default_offer_id,
            first_name=first_name,
            last_name=last_name,
            summary=summary,
            address=address,
            status=status)
    
class Professional_W_Offers(BaseModel):
    id: int | None = None
    username: str
    ###Add another model without default id and default offer in offers?
    default_offer_id: int | None = None
    first_name: str
    last_name: str
    summary: str
    address: str
    offers: list[ProfessionalOffer_NoProfessionalId]

    @classmethod
    def from_query_result(cls, id, username, default_offer_id, first_name, last_name, summary, address, offers):
        return cls(
            id=id,
            username=username,
            default_offer_id=default_offer_id,
            first_name=first_name,
            last_name=last_name,
            summary=summary,
            address=address,
            offers=offers)
    
class ProfessionalRequest(BaseModel):
    prof_offer_id: int
    comp_offer_id: int
    request_from: str

    @classmethod
    def from_query_result(cls, prof_offer_id, comp_offer_id, request_from):
        return cls(
            prof_offer_id=prof_offer_id,
            comp_offer_id=comp_offer_id,
            request_from=request_from)
    
class ProfessionalInfoEdit(BaseModel):
    username: str | None = None
    first_name: str | None = None
    last_name: str | None = None
    summary: str | None = None
    address: str | None = None

    @classmethod
    def from_query_result(cls, username, first_name, last_name, summary, address):
        return cls(
            username=username,
            first_name=first_name,
            last_name=last_name,
            summary=summary,
            address=address)