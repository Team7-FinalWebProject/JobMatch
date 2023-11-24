from pydantic import BaseModel
from data.models.offer import ProfessionalOffer_NoProfessionalId
from datetime import datetime



class Professional(BaseModel):
    id: int | None = None
    user_id: int
    default_offer_id: int | None = None
    first_name: str
    last_name: str
    summary: str | None = None
    address: str
    picture: bytes | None = None
    status: str | None = None
    username: str | None = None
    approved: bool | None = None
    issued: datetime | None = None

    @classmethod
    def from_query_result(cls, id, user_id, default_offer_id, first_name, last_name, summary, address, picture, status, username, approved, issued=None):
        return cls(
            id=id,
            user_id=user_id,
            default_offer_id=default_offer_id,
            first_name=first_name,
            last_name=last_name,
            summary=summary,
            address=address,
            picture=picture,
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
    picture: bytes | None = None
    status: str = None

    @classmethod
    def from_query_result(cls, id, username, default_offer_id, first_name, last_name, summary, address, picture, status):
        return cls(
            id=id,
            username=username,
            default_offer_id=default_offer_id,
            first_name=first_name,
            last_name=last_name,
            summary=summary,
            address=address,
            picture=picture,
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
    picture: bytes | None = None
    offers: list[ProfessionalOffer_NoProfessionalId]

    @classmethod
    def from_query_result(cls, id, username, default_offer_id, first_name, last_name, summary, address, picture, offers):
        return cls(
            id=id,
            username=username,
            default_offer_id=default_offer_id,
            first_name=first_name,
            last_name=last_name,
            summary=summary,
            address=address,
            picture=picture,
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
    first_name: str | None = None
    last_name: str | None = None
    summary: str | None = None
    address: str | None = None
    picture: bytes | None = None

    @classmethod
    def from_query_result(cls, first_name, last_name, summary, address, picture):
        return cls(
            first_name=first_name,
            last_name=last_name,
            summary=summary,
            address=address,
            picture=picture)