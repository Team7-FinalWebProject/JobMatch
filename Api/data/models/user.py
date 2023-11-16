from pydantic import BaseModel


class User(BaseModel):
    id: int | None = None
    username: str

    @classmethod
    def from_query_result(cls, id, username):
        return cls(
            id=id,
            username=username)

