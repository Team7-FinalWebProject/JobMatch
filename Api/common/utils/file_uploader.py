import os
import secrets
from PIL import Image
from fastapi import UploadFile, HTTPException


def create_upload_file(myfile: UploadFile):
    _IMAGE_DIR = "./data/logos/"

    filename = myfile.filename
    extention = filename.split('.')[-1].lower()

    if extention not in ('png', 'jpg', 'jpeg'):
        raise HTTPException(status_code=400, detail='File extention not allowed')
    token_name = secrets.token_hex(10) + "." + extention
    generated_name = _IMAGE_DIR + token_name
    file_content = myfile.file.read()
    try:
        with open(generated_name, "wb") as f:
            f.write(file_content)

        img = Image.open(generated_name)
        img = img.resize(size = (200, 200))
        img.save(generated_name)
 
        print(generated_name)
        return generated_name
    except Exception as e:
        raise HTTPException(status_code=500, detail="Unexpected error occured.")