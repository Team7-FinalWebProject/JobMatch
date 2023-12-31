from typing import Any
from pydantic import BaseModel, validator

class ClassType(BaseModel):
    a_class: Any

    @validator("a_class")
    def validate_a_class(cls, val):
        if issubclass(type(val), BaseModel):
            return val
        raise TypeError("Wrong type for class, must be subclass of pydantic BaseModel")


def reader_one(cls : ClassType, data: list[tuple[Any, ...]]) -> ClassType | None:
    return next((cls.from_query_result(*user_row) for user_row in data), None)

def reader_many(cls : ClassType, data: list[tuple[Any, ...]]) -> tuple[ClassType, ...]:
    return (cls.from_query_result(*row) for row in data)

