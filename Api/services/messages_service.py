import json
import uuid
from pathlib import Path
from fastapi.responses import StreamingResponse
from data.models.message import Message
from fastapi import HTTPException, status
from data.database import read_query, insert_query
from dotenv import load_dotenv
from openai import OpenAI
load_dotenv()
client = OpenAI()


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


def create_bot_conv(text: str):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo-1106",
            response_format={ "type": "json_object" },
            messages=[
                {"role": "system", "content": """You are a helpful tech support specialist."""},
                {"role": "user", "content": text}
            ])
        
        data = json.loads(response.choices[0].message.content)
        
        unique_id = str(uuid.uuid4())
        filename = f"speech_{unique_id}.mp3"
        speech_file_path = Path("./data/audio") / filename
        response = client.audio.speech.create(
            model="tts-1",
            voice="alloy",
            input=str(data["content"])
        )
        response.stream_to_file(speech_file_path)
        
        def file_generator():
            with open(speech_file_path, 'rb') as file:
                yield from iter(lambda: file.read(4096), b"")
        
        return StreamingResponse(file_generator(), media_type="audio/mpeg")

    except Exception as e:
        print(f"Error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal Server Error"
        )