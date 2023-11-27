from mailjet_rest import Client
import os

API_KEY = os.environ['_MJ_APIKEY_PUBLIC']
API_SECRET = os.environ['_API_SECRET']

mailjet = Client(auth=(API_KEY, API_SECRET), version='v3.1')

def data_input(sender_email: str, sender_username: str, receiver_email: str):
    data = {
        'Messages': [
            {
                "From": {
                    "Email": "some_email",
                    "Name": "Mailjet Pilot"
                },
                "To": [
                    {
                        "Email": "some_email"
                    }
                ],
                "Subject": "Your offer has been matched",
                "TextPart": f"Dear {receiver_email}, we are happy to inform you that your offer has been matched by {sender_username}",
                "HTMLPart": '''<h3>Dear {receiver_email}, we are happy to inform you that your offer has been matched 
                                <a href=\"https://www.mailjet.com/\">Mailjet</a>!</h3><br />May the job force be with you! From: {sender_username}'''
            }
        ]
    }

    data['Messages'][0]['From']['Email'] = sender_email
    data['Messages'][0]['From']['Name'] = sender_username
    data['Messages'][0]['To'][0]['Email'] = receiver_email

    return data