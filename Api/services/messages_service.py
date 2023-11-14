from data.models.message import Message
from data.models.user import User
from data.database import read_query, insert_query


def get_messages(sender: User, receiver_username: str):
    data = read_query(
        '''SELECT * FROM messsages WHERE sender_username = ? AND receiver_username = ?''',
        (sender.username, receiver_username)
    )

    return (Message.from_query_result(*row) for row in data)


def create(sender: User, receiver_username: str, message: Message):
    generated_id = insert_query(
        '''INSERT INTO messages(sender, receiver, content) 
           VALUES(?, ?, ?)''', (sender.username, receiver_username, message.content)
    )

    message.id = generated_id
    return Message(
        id=message.id,
        sender_username=sender.username,
        receiver_username=receiver_username,
        content=message.content)