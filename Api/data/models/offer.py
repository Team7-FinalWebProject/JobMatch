from pydantic import BaseModel
from common.constraints import Allowed_Skill_Names as skill_name, Allowed_Skill_Levels as skill_level, _USE_STATIC

class SkillsStatic(BaseModel):
    skills: dict[skill_name, dict[skill_level, str]]

class SkillsDynamitc(BaseModel):
    skills: dict[str, dict[int, str]]

Skills = SkillsDynamitc if not _USE_STATIC else SkillsStatic

class ProfessionalOffer(BaseModel):
    id: int | None = None
    professional_id: int | None = None
    ###Add another model without offer id and full offer instead?
    chosen_company_offer_id: int | None = None
    description: str | None = None
    status: str | None = None
    skills: Skills | None = None
    min_salary: int | None = None
    max_salary: int | None = None

    @classmethod
    def from_query_result(cls, id, default_offer_id, first_name, last_name, summary, address, picture):
        return cls(
            id=id,
            default_offer_id=default_offer_id,
            first_name=first_name,
            last_name=last_name,
            summary=summary,
            address=address,
            picture=picture)
    

class ProfessionalOffer_NoProfessionalId(BaseModel):
    id: int | None = None
    ###Add another model without offer id and full offer instead?
    chosen_company_offer_id: int | None = None
    description: str | None = None
    status: str | None = None
    skills: Skills | None = None
    min_salary: int | None = None
    max_salary: int | None = None

    @classmethod
    def from_query_result(cls, id, default_offer_id, first_name, last_name, summary, address, picture):
        return cls(
            id=id,
            default_offer_id=default_offer_id,
            first_name=first_name,
            last_name=last_name,
            summary=summary,
            address=address,
            picture=picture)
    

class CompanyOffer(BaseModel):
    id: int | None = None
    company_id: int
    ###Add another model without professional Id and full professional instead?
    chosen_professional_id: int | None = None
    status: str | None = None
    requirements: Skills | None = None
    min_salary: int | None = None
    max_salary: int | None = None

    @classmethod
    def from_query_result(cls, id, company_id, chosen_professional_id, status, requirements, min_salary,max_salary):
        return cls(
            id = id,
            company_id = company_id,
            chosen_professional_id = chosen_professional_id,
            status=status,
            requirements=requirements,
            min_salary=min_salary,
            max_salary=max_salary)
    
class CompanyOffer_NoCompanyId(BaseModel):
    id: int | None = None
    ###Add another model without professional Id and full professional instead?
    chosen_professional_id: int | None = None
    status: str | None = None
    requirements: Skills | None = None
    min_salary: int | None = None
    max_salary: int | None = None

    @classmethod
    def from_query_result(cls, id, chosen_professional_id, status, requirements, min_salary,max_salary):
        return cls(
            id = id,
            chosen_professional_id = chosen_professional_id,
            status=status,
            requirements=requirements,
            min_salary=min_salary,
            max_salary=max_salary)