from pydantic import BaseModel
from datetime import datetime

class Admin(BaseModel):
    id: int | None = None
    user_id: int | None = None
    username: str | None = None
    issued: datetime | None = None

    @classmethod
    def from_query_result(cls, id, user_id, username, issued=None):
        return cls(
            id=id,
            user_id=user_id,
            username=username)
    
class ReadConfig(BaseModel):
    static_skills: bool
    min_level: int
    max_level: int
    baseline_skills: dict
    approved_skills: dict
    pending_approval_skills: dict

    @classmethod
    def from_query_result(cls, static_skills, min_level, max_level, baseline_skills, approved_skills, pending_approval_skills):
        return cls(
            static_skills=static_skills,
            min_level=min_level,
            max_level=max_level,
            baseline_skills=baseline_skills,
            approved_skills=approved_skills,
            pending_approval_skills=pending_approval_skills)
    
class UpdateConfig(BaseModel):
    static_skills: bool | None = None
    min_level: int | None = None
    max_level: int | None = None

    @classmethod
    def from_query_result(cls, static_skills, min_level, max_level):
        return cls(
            static_skills=static_skills,
            min_level=min_level,
            max_level=max_level)
