import os
import json
from psycopg2.extras import Json
from data.database import insert_query, update_query
from data.models.company import Company
from data.models.offer import CompanyOffer, ProfessionalOffer
from data.models.professional import Professional
from common.skill_config import Config
from fastapi import Response
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()
client = OpenAI()
from hashlib import sha256

def _hash_password(password: str):
    return sha256(password.encode('utf-8')).hexdigest()

def generate_company(prompt = "Please suggest a json for a company user account!", count=1):
    try:
        password = _hash_password(os.getenv('userpassword'))
        response = client.chat.completions.create(
            model="gpt-3.5-turbo-1106",
            response_format={ "type": "json_object" },
            messages=[
                {"role": "system", "content": f"""You are a helpful language expert tasked with creating
                output JSON in the flat schema: username, name, description, address.
                 {(f"Please generate {count} companies packed in a list - " + "{companies:[]}.") if count > 1 else ""}
                The json describes an original company's website account. Company can be in any industry.
                Avoid repetition for name and username and country of origin and avoid copying pre-existing entities. 
                Addresses can be worldwide, but please prefer eastern europe.
                Use techniques such as compounding and clipping to create names."""},
                {"role": "user", "content": prompt}
        ])
        data = json.loads(response.choices[0].message.content)
        def db_io(company):
            user_id = insert_query(
                '''INSERT INTO users(username, password) 
                VALUES (%s, %s) RETURNING id''', 
                (company.username, password))
            company.user_id = user_id
            company_id = insert_query(
                '''INSERT INTO companies(name, description, address, user_id)
                VALUES (%s, %s, %s, %s) RETURNING id''', 
                (company.name, company.description,
                    company.address, user_id))
            company.id = company_id
        if count == 1:
            comp = Company(username=data["username"], name=data["name"], description=data["description"], address=data["address"])
            db_io(comp)
        if count > 1:
            companies = [Company(username=x["username"], name=x["name"], description=x["description"], address=x["address"]) for x in data["companies"]]
            for comp in companies:
                db_io(comp)
        return comp if count==1 else companies
    except Exception as e:
        print("exception:", e)
    return Response(status_code=500, content="Error generating company, possibly duplicate. Try again.")
    

def generate_professional(prompt = "Please suggest a json for a professional user account!", count=1):
    try:
        password = _hash_password(os.getenv('userpassword'))
        response = client.chat.completions.create(
            model="gpt-3.5-turbo-1106",
            response_format={ "type": "json_object" },
            messages=[
                {"role": "system", "content": f"""You are a helpful language expert tasked with creating
                output JSON in the flat schema: username, first_name, last_name, address, summary. 
                 {(f"Please generate {count} professionals packed in a list - " + "{professionals:[]}.") if count > 1 else ""}
                The json describes an original human's jobhunting website account. Professional can have experience in any industry.
                Avoid repetition for name, username and country of origin and avoid copying pre-existing entities. 
                Addresses can be worldwide, but please prefer eastern europe.
                Use techniques such as compounding and clipping to create names."""},
                {"role": "user", "content": prompt}
        ])
        data = json.loads(response.choices[0].message.content)
        def db_io(professional):
            user_id = insert_query(
                '''INSERT INTO users(username, password) 
                VALUES (%s, %s) RETURNING id''', (professional.username, password))
            professional.user_id = user_id
            prof_id = insert_query(
                '''INSERT INTO professionals(
                first_name, last_name, address, user_id, summary)
                VALUES (%s, %s, %s, %s, %s) RETURNING id''', 
                (professional.first_name, professional.last_name, 
                professional.address, user_id, professional.summary))
            professional.id = prof_id
        if count == 1:
            prof = Professional(username=data["username"], first_name=data["first_name"], last_name=data["last_name"], 
                    address=data["address"], summary=data["summary"])
            db_io(prof)
        if count > 1:
            professionals = [Professional(username=x["username"], first_name=x["first_name"], last_name=x["last_name"], 
                    address=x["address"], summary=x["summary"]) for x in data["professionals"]]
            for prof in professionals:
                db_io(prof)
        return prof if count==1 else professionals
    except Exception as e:
        return Response(status_code=500, content="Error generating professional, possibly duplicate. Try again.")

##TODO: row for artificial entities, in order to disable generation of offers to non-artificial entities
def generate_company_offer(id, prompt = "Please suggest a json for a company job offer!", count=1):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo-1106",
            response_format={ "type": "json_object" },
            messages=[
                {"role": "system", "content": """You are a helpful language expert tasked with creating
                output JSON in the following schema: {"requirements" : {str : [int, str], str : [int, str], ... }, "min_salary" : int, "max_salary" : int}. """ +
                 f"""{(f"Please generate {count} offers packed in a list - " + "{offers:[]}.") if count > 1 else ""}""" +
                """Requirements contains a list of at least one skill, stuctured as such: skill_name : [skill_level, skill_description].
                 Example: {"requirements" : {"Python": [8, "Senior developer"], "SQL": [4, "Experienced"], "English": [9, "Fluent speaker"]}, "min_salary" : 2000, "max_salary" : 3000}.
                 The json describes an company's job offer. Offer can be from any industry. Avoid repetition, do not copy the example, provide an original offer.
                """},
                {"role": "user", "content": prompt}
        ])
        data = json.loads(response.choices[0].message.content)
        def db_io(offer):
            generated_id = insert_query(
                '''INSERT INTO company_offers (company_id, requirements, min_salary, max_salary)
                VALUES (%s, %s, %s, %s) RETURNING id''',
                (id, Json(offer.requirements), offer.min_salary, offer.max_salary))
            offer.id = generated_id
        if count == 1:
            off = CompanyOffer(company_id=id, requirements=data["requirements"], min_salary=data["min_salary"], max_salary=data["max_salary"])
            db_io(off)
        if count > 1:
            offers = [CompanyOffer(company_id=id, requirements=x["requirements"], min_salary=x["min_salary"], max_salary=x["max_salary"]) for x in data["offers"]]
            for off in offers:
                db_io(off)
        return off if count==1 else offers
    except Exception as e:
        return Response(status_code=500, content="Error generating company offer. Try again.")
    

##TODO: row for artificial entities, in order to disable generation of offers to non-artificial entities
def generate_professional_offer(id, prompt = "Please suggest a json for a professional bio!", count=1):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo-1106",
            response_format={ "type": "json_object" },
            messages=[
                {"role": "system", "content": """You are a helpful language expert tasked with creating
                output JSON in the following schema: {"description" : str, "skills" : {str : [int, str], str : [int, str], ... }, "min_salary" : int, "max_salary" : int}. """ +
                 f"""{(f"Please generate {count} offers packed in a list - " + "{offers:[]}.") if count > 1 else ""}""" +
                """Skills contains a list of at least one skill, stuctured as such: skill_name : [skill_level, skill_description].
                 Example: {"description" : "A talented embedded systems programmer.", "skills" : {"Electronics": [8, "Senior"], "C": [6, "Advanced"], "English": [5, "Good communication"]}, "min_salary" : 2000, "max_salary" : 3000}.
                 The json describes an professional looking for employment's bio. Professional can be from any industry. Avoid repetition, do not copy the example, provide an original bio.
                """},
                {"role": "user", "content": prompt}
        ])
        data = json.loads(response.choices[0].message.content)
        print(data)
        def db_io(offer):
            generated_id = insert_query(
                '''INSERT INTO professional_offers (professional_id, description, 
                skills, min_salary, max_salary)
                VALUES (%s, %s, %s, %s, %s) RETURNING id''', 
                (id, offer.description, 
                    Json(offer.skills), offer.min_salary, offer.max_salary))
            offer.id = generated_id
        if count == 1:
            off = ProfessionalOffer(professional_id=id, description=data["description"], skills=data["skills"], min_salary=data["min_salary"], max_salary=data["max_salary"])
            db_io(off)
        if count > 1:
            offers = [ProfessionalOffer(professional_id=id, description=x["description"], skills=x["skills"], min_salary=x["min_salary"], max_salary=x["max_salary"]) for x in data["offers"]]
            for off in offers:
                db_io(off)
        return off if count==1 else offers
    except Exception as e:
        print("exception:", e)
        return Response(status_code=500, content="Error generating professional offer. Try again.")
  

def generate_skills_proposal(prompt = "Please suggest a json for CV skills!", count=100):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo-1106",
            response_format={ "type": "json_object" },
            messages=[
                {"role": "system", "content": """You are a helpful language expert tasked with creating
                output JSON in the flat schema: {str : None}. Example: {"English" : null, React : None}""" +
                 f"""Please generate {count} skills or as a many as you can come up with.""" +
                """The json describes CV skills or requirements. Skills can be from any industry.
                Avoid repetition for skills and avoid copying pre-existing skills."""},
                {"role": "user", "content": prompt}
        ])
        data = json.loads(response.choices[0].message.content)
        update_query(
            '''UPDATE config
            SET pending_approval_skills = pending_approval_skills || %s
            WHERE lock = %s''', (Json(data),'X',))
        return Response(status_code=200)
    except:
        return Response(status_code=500)