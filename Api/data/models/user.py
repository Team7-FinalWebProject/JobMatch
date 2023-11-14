from pydantic import BaseModel

class User(BaseModel):
    id: int | None = None
    username: str
    approved: bool

    @classmethod
    def from_query_result(cls, id, username, approved):
        return cls(
            id=id,
            username=username,
            approved=approved)

