from data.models import Message, Professional, Company
from data.database import read_query, insert_query


def get_prof_messages(sender: Professional, receiver_username: str):
    data = read_query(
        '''SELECT * FROM messsages WHERE sender = ? AND receiver = ?''',
        (sender.username, receiver_username)
    )

    return (Message.from_query_result(*row) for row in data)


def get_comp_messages(sender: Company, receiver_username: str):
    data = read_query(
        '''SELECT * FROM messsages WHERE sender = ? AND receiver = ?''',
        (sender.username, receiver_username)
    )

    return (Message.from_query_result(*row) for row in data)


def create(sender: Professional | Company, message: Message):
    generated_id = insert_query(
        '''INSERT INTO messages(sender, receiver, content) 
            VALUES(?, ?, ?)''', (sender.username, message.receiver_username, message.content)
    )

    message.id = generated_id
    return Message(
        id=message.id,
        sender_username=sender.username,
        receiver_username=message.receiver_username,
        content=message.content)