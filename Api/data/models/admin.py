from pydantic import BaseModel
from datetime import datetime

class Admin(BaseModel):
    id: int | None = None
    username: str | None = None
    issued: datetime | None = None

    @classmethod
    def from_query_result(cls, id, username, issued=None):
        return cls(
            id=id,
            username=username)
    
class Config(BaseModel):
    static_skills: bool | None = None
    min_level: int | None = None
    max_level: int | None = None
    baseline_skills: dict | None = None
    approved_skills: dict | None = None
    pending_approval_skills: dict | None = None

    @classmethod
    def from_query_result(cls, static_skills, min_level, max_level, baseline_skills, approved_skills, pending_approval_skills):
        return cls(
            static_skills=static_skills,
            min_level=min_level,
            max_level=max_level,
            baseline_skills=baseline_skills,
            approved_skills=approved_skills,
            pending_approval_skills=pending_approval_skills)