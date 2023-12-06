from pydantic import BaseModel
from common.skill_config import Config

Any_Skills = Config.FILTER_SKILLS()

class Filter(BaseModel):
    id: int
    filters: Any_Skills

    @classmethod
    def from_query_result(cls, id, filters):
        return cls(
            id=id,
            filters=filters,)

