from psycopg2 import IntegrityError
from data.models.professional import Professional
from data.models.offer import ProfessionalOffer
from data.database import update_query, insert_query, read_query, update_queries_transaction, insert_queries_trasnaction



def edit(new_data: Professional, old_data: Professional):
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
        '''UPADTE professionals SET default_offer_id = ?, first_name = ?, last_name = ?,
           summary = ?, address = ?, picture = ? WHERE id = ?''',
           (merged.default_offer_id, merged.first_name, merged.last_name, 
            merged.summary, merged.address, merged.picture, merged.id))
    
    return merged


def create_offer(offer: ProfessionalOffer, prof: Professional):
    try:
        generated_id = insert_query(
            '''INSERT INTO professional_offers (professional_id, description, 
            chosen_company_offer_id, status, skills, min_salary, max_salary)
            VALUES (?, ?, ?, ?, ?, ?, ?)''', 
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