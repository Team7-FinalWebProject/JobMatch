from data.database import update_query, insert_query, read_query, update_queries_transaction
from fastapi import Header, HTTPException, status
from data.models.company import Company, CompanyRequest
from data.models.offer import CompanyOffer
from psycopg2 import IntegrityError
from psycopg2.extras import Json
from data.responses import InvalidStatusError
from psycopg2.errors import UniqueViolation




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
        '''SELECT id, company_id, chosen_professional_offer_id, status,
           requirements, min_salary, max_salary 
           FROM company_offers WHERE id = %s AND company_id = %s''',
        (offer_id, company_id))
    
    return next((CompanyOffer.from_query_result(*row) for row in data), None)




def edit_company_offer(new_offer: CompanyOffer, old_offer: CompanyOffer):
    try:
        if new_offer.status != "active":
            raise InvalidStatusError("New status must be 'active'.")

        chosen_professional_offer_id = (
            new_offer.chosen_professional_offer_id
            if new_offer.chosen_professional_offer_id != 0
            else old_offer.chosen_professional_offer_id
        )

        merged = CompanyOffer(
            id=old_offer.id,
            company_id=old_offer.company_id,
            status=new_offer.status or old_offer.status,
            chosen_professional_offer_id=chosen_professional_offer_id,
            requirements=new_offer.requirements or old_offer.requirements,
            min_salary=new_offer.min_salary or old_offer.min_salary,
            max_salary=new_offer.max_salary or old_offer.max_salary,
        )

        update_query(
            '''UPDATE company_offers SET company_id = %s, status = %s, chosen_professional_offer_id = %s,
               requirements = %s, min_salary = %s, max_salary = %s WHERE id = %s''',
            (
                merged.company_id,
                merged.status,
                merged.chosen_professional_offer_id,
                Json(merged.requirements),
                merged.min_salary,
                merged.max_salary,
                merged.id,
            ),
        )

        return merged

    except IntegrityError as e:
        return e.__str__()
    except InvalidStatusError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))




def check_offer_exists(offer_id: int):
    return any(read_query(
        '''SELECT * FROM company_offers WHERE id = %s''',
        (offer_id,)))

def get_prof_id_from_prof_offer_id(prof_offer_id: int):
    data = read_query(
        '''SELECT professional_id FROM professional_offers WHERE id = %s''',
        (prof_offer_id,))
    
    return next((row[0] for row in data), None)



def create_match_request(comp_offer_id: int, prof_offer_id: int):
    try:
        insert_query(
            '''INSERT INTO requests(company_offer_id, professional_offer_id, request_from)
            VALUES (%s, %s, %s) RETURNING id''', 
            (comp_offer_id, prof_offer_id, 'company'))
        
        return f'Sent match request for professional offer {prof_offer_id}'
    except UniqueViolation:
        return None
    
    


def is_author(company_id: int, offer_id: int):
    return any(read_query(
        '''SELECT 1 FROM company_offers 
           WHERE company_id = %s AND id = %s''',
        (company_id, offer_id)))


def match_prof_offer(offer_id: int, prof_id: int, prof_offer_id: int, private_or_hidden: str):
    queries = (
        '''UPDATE professional_offers SET status = %s
           WHERE professional_id = %s AND status = %s''',

        '''UPDATE professional_offers SET status = %s, chosen_company_offer_id = %s
           WHERE id = %s''',

        '''UPDATE professionals SET status = %s
           WHERE id = %s''',
        
        '''UPDATE company_offers SET status = %s
           WHERE id = %s'''
    )
    params = ((private_or_hidden, prof_id, 'active'), ('matched', offer_id, prof_offer_id), 
              ('busy', prof_id), ('archived', offer_id))
    rowcount = update_queries_transaction(queries, params)
    return rowcount



def set_status(comp_id: int, comp_offer_id: int, status):
    rowcount = update_query(
        '''UPDATE company_offers SET status = %s
           WHERE id = %s AND company_id = %s''',
        (status, comp_offer_id, comp_id))

    return f'Changed status | {rowcount}'



def get_match_requests(company: Company):
    data = read_query(
        '''SELECT r.professional_offer_id, r.company_offer_id, r.request_from
           FROM requests AS r
           JOIN professional_offers AS p ON r.professional_offer_id = p.id
           WHERE p.professional_id = %s''', (company.id,))

    return (CompanyRequest.from_query_result(*row) for row in data)





def upload_img(comp: Company, image):
    rowcount = update_query(
        '''UPDATE companies SET picture = %s
           WHERE id = %s''', (image, comp.id))
    
    return f'Updated photo [{rowcount}]'
