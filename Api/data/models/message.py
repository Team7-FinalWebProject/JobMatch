from pydantic import BaseModel

class Message(BaseModel):
    id: int | None = None
    sender_username: str
    receiver_username: str
    content: str

    @classmethod
    def from_query_result(cls, id, sender_username, receiver_username, content):
        return cls(
            id=id,
            sender_username=sender_username,
            receiver_username=receiver_username,
            content=content)