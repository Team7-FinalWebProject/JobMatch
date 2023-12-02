import json
# from openai import OpenAI
# from dotenv import load_dotenv
# load_dotenv()

# client = OpenAI()

# response = client.chat.completions.create(
#   model="gpt-3.5-turbo-1106",
#   response_format={ "type": "json_object" },
#   messages=[
#     {"role": "system", "content": """You are a helpful linguistic expert tasked with creating
#       output JSON in the flat schema: username, name, description, address. 
#      The json describes an original company"s website account.
#      Avoid repetition for name and username and avoid copying pre-existing entities. 
#      Addresses can be worldwide, but please prefer eastern europe.
#      Make use of advanced linguistic techniques such as compounding and clipping to come up with names."""},
#     {"role": "user", "content": "Please suggest a json for a company user account!"}
#   ]
# )
# print(response.choices[0].message.content)
# print(response)

# print(json.loads('{"username": "projobseeker87", "first_name": "Erik", "last_name": "Mikhaylov", "address": "Sofia, Bulgaria", "summary": "Experienced professional seeking new opportunities in the finance industry."}'))
data = json.loads('{"requirements": {"Java": [7, "Experienced developer"], "Spring Framework": [6, "Intermediate level"], "Cloud Computing": [5, "Familiar with AWS or Azure"], "Problem-solving": [8, "Strong analytical skills"], "Communication": [9, "Excellent verbal and written skills"]}, "min_salary": 2500, "max_salary": 3500}')

print(data["requirements"]["Java"][1])