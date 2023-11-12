from data.database import read_query, insert_query, update_query, update_queries_transaction
from data.models import Professional, Company


def create_user(username: str, first_name:str, last_name:str, password: str) -> Professional | None:
        generated_id = insert_query(
            'INSERT INTO professionals(username, first_name, last_name, password) VALUES (?,?,?,?)',
            (username, first_name, last_name, password))

        return Professional(id=generated_id, username=username, first_name=first_name, last_name=last_name, password="")


def check_username_exist(nickname:str) -> bool:

    data = read_query(
        'SELECT username FROM professionals WHERE username = ?',
        (nickname,)
    )

    return bool(data)