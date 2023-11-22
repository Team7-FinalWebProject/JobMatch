from mailjet_rest import Client
import os

API_KEY = os.environ['_MJ_APIKEY_PUBLIC']
API_SECRET = os.environ['_API_SECRET']

mailjet = Client(auth=(API_KEY, API_SECRET))