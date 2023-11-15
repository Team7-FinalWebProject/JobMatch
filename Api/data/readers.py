from typing import Any, TypeVar
from pydantic import BaseModel
T = TypeVar('T')

def reader_one(cls : BaseModel[T], data: list[tuple[Any, ...]]) -> BaseModel[T] | None:
    return next((cls.from_query_result(*user_row) for user_row in data), None)

def reader_many(cls : BaseModel[T], data: list[tuple[Any, ...]]) -> tuple[BaseModel[T], ...]:
    return (cls.from_query_result(*row) for row in data)