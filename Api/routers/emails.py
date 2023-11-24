from mailjet_rest import Client
import os

API_KEY = os.environ['_MJ_APIKEY_PUBLIC']
API_SECRET = os.environ['_API_SECRET']

mailjet = Client(auth=(API_KEY, API_SECRET), version='v3.1')

data = {
  'Messages': [
        {
        "From": {
                "Email": "anotherinbox@mailsac.com",
                "Name": "Mailjet Pilot"},
        "To": [
                {
                "Email": "jobtestmail@mailsac.com",
                "Name": "testuser1"
                }
        ],
        "Subject": "Your offer has been matched",
        "TextPart": "Dear testuser1, we are happy to inform you that your offer has been matched",
        "HTMLPart": "<h3>Dear passenger 1, welcome to <a href=\"https://www.mailjet.com/\">Mailjet</a>!</h3><br />May the delivery force be with you!"
        }
        ]
}
result = mailjet.send.create(data=data)
print(result.status_code)
print(result.json())