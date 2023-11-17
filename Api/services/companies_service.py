from data.database import update_query, insert_query, read_query
from fastapi import Header
from data.models.company import Company
from psycopg2 import IntegrityError




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