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
    username: str | None = None
    issued: datetime | None = None

    @classmethod
    def from_query_result(cls, id, user_id, default_offer_id, first_name, last_name, summary, address, picture, username, issued=None):
        return cls(
            id=id,
            user_id=user_id,
            default_offer_id=default_offer_id,
            first_name=first_name,
            last_name=last_name,
            summary=summary,
            address=address,
            picture=picture,
            username=username)
    

class Professional_Slim(BaseModel):
    id: int | None = None
    username: str
    default_offer_id: int | None = None
    first_name: str
    last_name: str
    summary: str
    address: str
    picture: bytes | None = None

    @classmethod
    def from_query_result(cls, id, username, default_offer_id, first_name, last_name, summary, address, picture):
        return cls(
            id=id,
            username=username,
            default_offer_id=default_offer_id,
            first_name=first_name,
            last_name=last_name,
            summary=summary,
            address=address,
            picture=picture)
    
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
    id: int
    prof_offer_id: int
    comp_offer_id: int

    @classmethod
    def from_query_result(cls, id, prof_offer_id, comp_offer_id):
        return cls(
            id=id,
            prof_offer_id=prof_offer_id,
            comp_offer_id=comp_offer_id)
    
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