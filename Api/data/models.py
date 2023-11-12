from pydantic import BaseModel


class Company(BaseModel):
    pass

    @classmethod
    def from_query_result(cls, id):
        return cls(
            id=id)


class Professional(BaseModel):
    pass

    @classmethod
    def from_query_result(cls, id):
        return cls(
            id=id)