from psycopg2 import IntegrityError
from data.models.professional import Professional, ProfessionalRequest
from data.models.offer import ProfessionalOffer
from data.database import update_query, insert_query, read_query



def edit(new_data: Professional, old_data: Professional):
    try:
        merged = Professional(
            id=old_data.id,
            user_id=old_data.user_id,
            default_offer_id=new_data.default_offer_id or old_data.default_offer_id,
            first_name=new_data.first_name or old_data.first_name,
            last_name=new_data.last_name or old_data.last_name,
            summary=new_data.summary or old_data.summary,
            address=new_data.address or old_data.address,
            picture=new_data.picture or old_data.picture)

        update_query(
            '''UPDATE professionals SET default_offer_id = %s, first_name = %s, last_name = %s,
               summary = %s, address = %s, picture = %s WHERE id = %s''',
               (merged.default_offer_id, merged.first_name, merged.last_name, 
                merged.summary, merged.address, merged.picture, merged.id))
        
        return merged
    
    except IntegrityError as e:
        return e.__str__()


def create_offer(offer: ProfessionalOffer, prof: Professional):
    try:
        generated_id = insert_query(
            '''INSERT INTO professional_offers (professional_id, description, 
               chosen_company_offer_id, status, skills, min_salary, max_salary)
               VALUES (%s, %s, %s, %s, %s, %s, %s)''', 
               (prof.id, offer.description, offer.chosen_company_offer_id,
                offer.status, offer.skills, offer.min_salary, offer.max_salary))
        
        return ProfessionalOffer(
            id=generated_id,
            professional_id=prof.id,
            chosen_company_offer_id=offer.chosen_company_offer_id,
            description=offer.description,
            status=offer.status,
            skills=offer.skills,
            min_salary=offer.min_salary,
            max_salary=offer.max_salary)
    
    except IntegrityError as e:
        return e.__str__()
    

def set_def_offer(offer_id: int, prof_id: int):
    rowcount = update_query(
        '''UPDATE professionals SET default_offer_id = %s WHERE id = %s''',
        (offer_id, prof_id))

    return rowcount


def get_offer_by_id(offer_id: int):
    data = read_query(
        '''SELECT * FROM professional_offers WHERE id = %s''',
        (offer_id,))
    
    return next((ProfessionalOffer.from_query_result(*row) for row in data), None)


def get_offer_by_prof_id(prof_id: int):
    data = read_query(
        '''SELECT * FROM professional_offers WHERE professional_id = %s''',
        (prof_id,))
    
    return next((ProfessionalOffer.from_query_result(*row) for row in data), None)


def edit_offer(new_offer: ProfessionalOffer, old_offer: ProfessionalOffer):
    try:
        merged = ProfessionalOffer(
            id=old_offer.id,
            professional_id=old_offer.professional_id,
            chosen_company_offer_id=new_offer.chosen_company_offer_id or old_offer.chosen_company_offer_id,
            description=new_offer.description or old_offer.description,
            status=new_offer.status or old_offer.status,
            skills=new_offer.skills or old_offer.skills,
            min_salary=new_offer.min_salary or old_offer.min_salary,
            max_salary=new_offer.max_salary or old_offer.max_salary)

        update_query(
            '''UPADTE professional_offers SET professional_id = %s, chosen_company_offer_id = %s,
               description = %s, status = %s, skills = %s, min_salary = %s, max_salary = %s WHERE id = %s''',
            (merged.professional_id, merged.chosen_company_offer_id, merged.description, 
            merged.status, merged.skills, merged.min_salary, merged.max_salary, merged.id))
        
        return merged
    
    except IntegrityError as e:
        return e.__str__()
    

def match():
    pass


def get_requests(offer_id: int):
    data = read_query(
        '''SELECT * FROM professional_requests WHERE professional_offer_id = %s''',
        (offer_id,))

    if len(data) > 0:
        return (ProfessionalRequest.from_query_result(*row) for row in data)
    
    return None


def archive_offer():
    pass