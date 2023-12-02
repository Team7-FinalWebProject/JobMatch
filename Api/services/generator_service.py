import os
import json
from psycopg2.extras import Json
from data.database import insert_query
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

def generate_company(prompt = "Please suggest a json for a company user account!"):
    try:
        password = _hash_password(os.getenv('userpassword'))
        response = client.chat.completions.create(
            model="gpt-3.5-turbo-1106",
            response_format={ "type": "json_object" },
            messages=[
                {"role": "system", "content": """You are a helpful language expert tasked with creating
                output JSON in the flat schema: username, name, description, address. 
                The json describes an original company's website account. Company can be in any industry.
                Avoid repetition for name and username and country of origin and avoid copying pre-existing entities. 
                Addresses can be worldwide, but please prefer eastern europe.
                Use techniques such as compounding and clipping to create names."""},
                {"role": "user", "content": prompt}
        ])
        data = json.loads(response.choices[0].message.content)
        
        user_id = insert_query(
            '''INSERT INTO users(username, password) 
            VALUES (%s, %s) RETURNING id''', 
            (data["username"], password))

        company_id = insert_query(
            '''INSERT INTO companies(name, description, address, user_id)
            VALUES (%s, %s, %s, %s) RETURNING id''', 
            (data["name"], data["description"],
                data["address"], user_id))
    except:
        return Response(status_code=500, content="Error generating company, possibly duplicate. Try again.")
    return Company(id=company_id, user_id=user_id, name=data["name"], description=data["description"], address=data["address"])
    

def generate_professional(prompt = "Please suggest a json for a professional user account!"):
    try:
        password = _hash_password(os.getenv('userpassword'))
        response = client.chat.completions.create(
            model="gpt-3.5-turbo-1106",
            response_format={ "type": "json_object" },
            messages=[
                {"role": "system", "content": """You are a helpful language expert tasked with creating
                output JSON in the flat schema: username, first_name, last_name, address, summary. 
                The json describes an original human's jobhunting website account. Professional can have experience in any industry.
                Avoid repetition for name, username and country of origin and avoid copying pre-existing entities. 
                Addresses can be worldwide, but please prefer eastern europe.
                Use techniques such as compounding and clipping to create names."""},
                {"role": "user", "content": prompt}
        ])
        data = json.loads(response.choices[0].message.content)
        
        user_id = insert_query(
            '''INSERT INTO users(username, password) 
            VALUES (%s, %s) RETURNING id''', (data["username"], password))
        
        prof_id = insert_query(
            '''INSERT INTO professionals(
            first_name, last_name, address, user_id, summary)
            VALUES (%s, %s, %s, %s, %s) RETURNING id''', 
            (data["first_name"], data["last_name"], 
            data["address"], user_id, data["summary"]))
    except:
        return Response(status_code=500, content="Error generating professional, possibly duplicate. Try again.")
    return Professional(
        id=prof_id, user_id=user_id,
        first_name=data["first_name"], last_name=data["last_name"], 
        address=data["address"], summary=data["summary"])

##TODO: row for artificial entities, in order to disable generation of offers to non-artificial entities
def generate_company_offer(id, prompt = "Please suggest a json for a company job offer!"):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo-1106",
            response_format={ "type": "json_object" },
            messages=[
                {"role": "system", "content": """You are a helpful language expert tasked with creating
                output JSON in the following schema: {"requirements" : {str : [int, str], str : [int, str], ... }, "min_salary" : int, "max_salary" : int}. 
                Requirements contains a list of at least one skill, stuctured as such: skill_name : [skill_level, skill_description].
                 Example: {"requirements" : {"Python": [8, "Senior developer"], "SQL": [4, "Experienced"], "English": [9, "Fluent speaker"]}, "min_salary" : 2000, "max_salary" : 3000}.
                 The json describes an company's job offer. Offer can be from any industry. Avoid repetition, do not copy the example, provide an original offer.
                """},
                {"role": "user", "content": prompt}
        ])
        data = json.loads(response.choices[0].message.content)
        print(data)

        generated_id = insert_query(
            '''INSERT INTO company_offers (company_id, requirements, min_salary, max_salary)
               VALUES (%s, %s, %s, %s) RETURNING id''',
               (id, Json(data["requirements"]), data["min_salary"], data["max_salary"]))
    except Exception as e:
        print("exception:", e)
        return Response(status_code=500, content="Error generating company offer. Try again.")
    return CompanyOffer(
            id=generated_id,
            company_id=id,
            requirements=data["requirements"],
            min_salary=data["min_salary"],
            max_salary=data["max_salary"])
    

##TODO: row for artificial entities, in order to disable generation of offers to non-artificial entities
def generate_professional_offer(id, prompt = "Please suggest a json for a professional bio!"):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo-1106",
            response_format={ "type": "json_object" },
            messages=[
                {"role": "system", "content": """You are a helpful language expert tasked with creating
                output JSON in the following schema: {"description" : str, "skills" : {str : [int, str], str : [int, str], ... }, "min_salary" : int, "max_salary" : int}. 
                Skills contains a list of at least one skill, stuctured as such: skill_name : [skill_level, skill_description].
                 Example: {"description" : "A talented embedded systems programmer.", "skills" : {"Electronics": [8, "Senior"], "C": [6, "Advanced"], "English": [5, "Good communication"]}, "min_salary" : 2000, "max_salary" : 3000}.
                 The json describes an professional looking for employment's bio. Professional can be from any industry. Avoid repetition, do not copy the example, provide an original bio.
                """},
                {"role": "user", "content": prompt}
        ])
        data = json.loads(response.choices[0].message.content)
        print(data)
        generated_id = insert_query(
            '''INSERT INTO professional_offers (professional_id, description, 
               skills, min_salary, max_salary)
               VALUES (%s, %s, %s, %s, %s) RETURNING id''', 
               (id, data["description"], 
                Json(data["skills"]), data["min_salary"], data["max_salary"]))
    except Exception as e:
        print("exception:", e)
        return Response(status_code=500, content="Error generating professional offer. Try again.")
    return ProfessionalOffer(
            id=generated_id,
            professional_id=id,
            description=data["description"],
            skills=data["skills"],
            min_salary=data["min_salary"],
            max_salary=data["max_salary"])
    
