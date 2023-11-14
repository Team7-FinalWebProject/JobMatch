from pydantic import BaseModel

class Company(BaseModel):
    id: int | None = None
    name: str
    description: str
    address: str
    picture: bytes | None = None
    approved: bool | None = None
    user_id: int

    @classmethod
    def from_query_result(cls, id, name, description, address, picture, approved, user_id):
        return cls(
            id=id,
            name=name,
            description=description,
            address=address,
            picture=picture,
            approved=approved,
            user_id=user_id)

