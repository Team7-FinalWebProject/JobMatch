from pydantic import BaseModel
from data.models.offer import CompanyOffer_NoCompanyId
from datetime import datetime

class Company(BaseModel):
    id: int | None = None
    user_id: int | None = None
    name: str
    description: str | None = None
    address: str
    picture: bytes | None = None
    username: str | None = None
    issued: datetime | None = None

    @classmethod
    def from_query_result(cls, id, user_id, name, description, address, picture, username, issued=None):
        return cls(
            id=id,
            user_id=user_id,
            name=name,
            description=description,
            address=address,
            picture=picture,
            username=username)


class Company_Slim(BaseModel):
    id: int | None = None
    username: str
    name: str
    description: str
    address: str
    picture: bytes | None = None

    @classmethod
    def from_query_result(cls, id, username, name, description, address, picture):
        return cls(
            id=id,
            username=username,
            name=name,
            description=description,
            address=address,
            picture=picture)
    
class Company_W_Offers(BaseModel):
    id: int | None = None
    username: str
    name: str
    description: str
    address: str
    picture: bytes | None = None
    offers: list[CompanyOffer_NoCompanyId]

    @classmethod
    def from_query_result(cls, id, username, name, description, address, picture, offers):
        return cls(
            id=id,
            username=username,
            name=name,
            description=description,
            address=address,
            picture=picture,
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