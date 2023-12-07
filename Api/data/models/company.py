from pydantic import BaseModel
from data.models.offer import CompanyOffer_NoCompanyId
from datetime import datetime
from typing import Any

class Company(BaseModel):
    id: int | None = None
    user_id: int | None = None
    name: str
    description: str | None = None
    address: str
    username: str | None = None
    approved: bool | None = None
    issued: datetime | None = None
    user_type: Any | None = None

    @classmethod
    def from_query_result(cls, id, user_id, name, description, address, username, approved, issued=None):
        return cls(
            id=id,
            user_id=user_id,
            name=name,
            description=description,
            address=address,
            username=username,
            approved=approved)


class Company_Slim(BaseModel):
    id: int | None = None
    username: str
    name: str
    description: str
    address: str

    @classmethod
    def from_query_result(cls, id, username, name, description, address):
        return cls(
            id=id,
            username=username,
            name=name,
            description=description,
            address=address)
    
class Company_W_Offers(BaseModel):
    id: int | None = None
    username: str
    name: str
    description: str
    address: str
    offers: list[CompanyOffer_NoCompanyId]

    @classmethod
    def from_query_result(cls, id, username, name, description, address, offers):
        return cls(
            id=id,
            username=username,
            name=name,
            description=description,
            address=address,
            offers=offers)




class Company_Data_For_Return(BaseModel):
    address: str
    id: int
    issued: str
    name: str
    user_id: int

    @classmethod
    def from_query_result(cls, address, id, issued, name, user_id):
        return cls(
            address=address,
            id=id,
            issued=issued,
            name=name,
            user_id=user_id)
        
        
class CompanyRequest(BaseModel):
    prof_offer_id: int
    comp_offer_id: int
    request_from: str

    @classmethod
    def from_query_result(cls, prof_offer_id, comp_offer_id, request_from):
        return cls(
            prof_offer_id=prof_offer_id,
            comp_offer_id=comp_offer_id,
            request_from=request_from)



class CompanyInfoEdit(BaseModel):
    name: str | None = None
    description: str | None = None
    address: str | None = None

    @classmethod
    def from_query_result(cls, name, description, address):
        return cls(
            name=name,
            description=description,
            address=address)