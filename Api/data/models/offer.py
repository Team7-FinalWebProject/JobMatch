from pydantic import BaseModel
from common.constraints import Skills

class ProfessionalOffer(BaseModel):
    id: int | None = None
    professional_id: int
    ###Add another model without offer id and full offer instead?
    chosen_company_offer_id: int | None = None
    description: str | None = None
    status: str | None = None
    skills: Skills | None = None
    min_salary: int | None = None
    max_salary: int | None = None

    @classmethod
    def from_query_result(cls, id, professional_id, chosen_company_offer_id, description, status, skills, min_salary, max_salary):
        return cls(
            id=id,
            professional_id=professional_id,
            chosen_company_offer_id=chosen_company_offer_id,
            description=description,
            status=status,
            skills=skills,
            min_salary=min_salary,
            max_salary=max_salary)
    
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
    def from_query_result(cls, id, chosen_company_offer_id, description, status, skills, min_salary, max_salary):
        return cls(
            id=id,
            chosen_company_offer_id=chosen_company_offer_id,
            description=description,
            status=status,
            skills=skills,
            min_salary=min_salary,
            max_salary=max_salary)
    

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
    
class ProfessionalOfferCreate(BaseModel):
    # chosen_company_offer_id: int | None = None
    description: str | None = None
    status: str | None = None
    skills: Skills | None = None
    min_salary: int | None = None
    max_salary: int | None = None

class ProfessionalOfferEdit(BaseModel):
    chosen_company_offer_id: int | None = None
    description: str | None = None
    # status: str | None = None
    skills: Skills | None = None
    min_salary: int | None = None
    max_salary: int | None = None

class CompanyOfferCreate(BaseModel):
    chosen_professional_id: int | None = None
    status: str | None = None
    requirements: Skills | None = None
    min_salary: int | None = None
    max_salary: int | None = None


