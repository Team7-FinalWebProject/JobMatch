from data.database import update_query, insert_query, read_query
from fastapi import Header
from data.models.company import Company
from data.models.offer import CompanyOffer
from psycopg2 import IntegrityError
from psycopg2.extras import Json




def edit_company_info(new_data: Company, old_data: Company):
    try:
        merged = Company(
            id=old_data.id,
            user_id=old_data.user_id,
            name=new_data.name or old_data.name,
            description=new_data.description or old_data.description,
            address=new_data.address or old_data.address,
            picture=new_data.picture or old_data.picture
            )

        update_query(
            '''UPDATE companies SET name = %s, description = %s, address = %s,
               picture = %s WHERE id = %s''',
               (merged.name, merged.description, merged.address, 
                merged.picture, merged.id))
        
        return merged
    
    except IntegrityError as e:
        return e.__str__()
    
def create_company_offer(offer, company: Company):


    try:
        requirements = Json(offer.requirements)
        generated_id = insert_query(
            '''INSERT INTO company_offers (company_id, chosen_professional_id, 
               requirements, min_salary, max_salary)
               VALUES (%s, %s, %s, %s, %s)''',
               (offer.company_id, offer.chosen_professional_id,
                requirements, offer.min_salary, offer.max_salary))
        
        return CompanyOffer(
            id=generated_id,
            company_id=company.id,
            status='active',
            chosen_professional_id=offer.chosen_professional_id,
            requirements=offer.requirements,
            min_salary=offer.min_salary,
            max_salary=offer.max_salary)
    
    except IntegrityError as e:
        return e.__str__()