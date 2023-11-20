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
            '''INSERT INTO company_offers (company_id, requirements, min_salary, max_salary)
               VALUES (%s, %s, %s, %s) RETURNING id''',
               (company.id,
                requirements, offer.min_salary, offer.max_salary))
        
        return CompanyOffer(
            id=generated_id,
            company_id=company.id,
            status='active',
            chosen_professional_id=None,
            requirements=offer.requirements,
            min_salary=offer.min_salary,
            max_salary=offer.max_salary)
    
    except IntegrityError as e:
        return e.__str__()
    

def get_company_offer(offer_id: int, company_id: int):
    data = read_query(
        '''SELECT id, company_id, status, chosen_professional_id, 
           requirements, min_salary, max_salary 
           FROM company_offers WHERE id = %s AND company_id = %s''',
        (offer_id, company_id))
    
    return next((CompanyOffer.from_query_result(*row) for row in data), None)


def edit_company_offer(new_offer: CompanyOffer, old_offer: CompanyOffer):
    try:
        merged = CompanyOffer(
            id=old_offer.id,
            company_id=old_offer.company_id,
            status=new_offer.status or old_offer.status,
            chosen_professional_id=new_offer.chosen_professional_id or old_offer.chosen_professional_id,
            requirements=new_offer.requirements or old_offer.requirements,
            min_salary=new_offer.min_salary or old_offer.min_salary,
            max_salary=new_offer.max_salary or old_offer.max_salary)

        update_query(
            '''UPDATE company_offers SET company_id = %s, status = %s, chosen_professional_id = %s,
               requirements = %s, min_salary = %s, max_salary = %s WHERE id = %s''',
            (merged.company_id, merged.status, merged.chosen_professional_id,
            Json(merged.requirements), merged.min_salary, merged.max_salary, merged.id))
        
        return merged
    
    except IntegrityError as e:
        return e.__str__()



def check_offer_exists(offer_id: int):
    return any(read_query(
        '''SELECT * FROM company_offers WHERE id = %s''',
        (offer_id,)))