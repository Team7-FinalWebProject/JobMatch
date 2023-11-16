from pydantic import BaseModel
from data.models.offer import CompanyOffer_NoCompanyId

class Company(BaseModel):
    id: int | None = None
    user_id: int | None = None
    name: str
    description: str | None = None
    address: str
    picture: bytes | None = None

    @classmethod
    def from_query_result(cls, id, user_id, name, description, address, picture):
        return cls(
            id=id,
            user_id=user_id,
            name=name,
            description=description,
            address=address,
            picture=picture)


class Company_Username(BaseModel):
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



