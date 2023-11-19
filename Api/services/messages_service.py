from data.models.message import Message
from data.models.professional import Professional
from data.models.company import Company
from data.database import read_query, insert_query


def get_messages(sender_username: str, receiver_username: str):
    data = read_query(
        '''SELECT * FROM messages WHERE sender_username = %s 
           AND receiver_username = %s''',
        (sender_username, receiver_username))
    
    if len(data) > 0:
        return (Message.from_query_result(*row) for row in data)
    
    return None
    

def create(sender_username: str, receiver_username: str, message: Message):
    generated_id = insert_query(
        '''INSERT INTO messages(sender_username, receiver_username, content) 
           VALUES(%s, %s, %s) RETURNING id''', 
           (sender_username, receiver_username, message.content)
    )

    message.id = generated_id
    return Message(
        id=message.id,
        sender_username=sender_username,
        receiver_username=receiver_username,
        content=message.content)


def extract_username(user: Professional | Company):
    username = read_query(
        '''SELECT u.username FROM users AS u
           LEFT JOIN professionals AS p ON u.id = p.user_id
           WHERE p.user_id = %s''', (user.id,))
    
    return username[0][0]