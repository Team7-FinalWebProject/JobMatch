from db_data import db_utils
from dotenv import load_dotenv

load_dotenv()

def main(**kwargs):
    db_utils.main(**kwargs)
