from pydantic import BaseModel


class Professional(BaseModel):
    id: int | None = None
    first_name: str
    last_name: str
    address: str
    user_id: int
    summary: str
    default_offer_id: int | None = None
    picture: bytes | None = None
    approved: bool | None = None

    @classmethod
    def from_query_result(cls, id, first_name, last_name, address, user_id, summary, default_offer_id, picture, approved):
        return cls(
            id=id,
            first_name=first_name,
            last_name=last_name,
            address=address,
            user_id=user_id,
            summary=summary,
            default_offer_id=default_offer_id,
            picture=picture,
            approved=approved)