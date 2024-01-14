import string
from datetime import datetime
from random import sample

from fastapi import UploadFile, HTTPException


def check_file(file: UploadFile) -> None:
    if not file.content_type == 'image/gpeg' and not file.size <= 300000:
        raise HTTPException(status_code=500, detail='ti menya ne na.. provedesh')


def generate_file_name(rand_text_size: int = 6):
    time_text = datetime.now().strftime("%m%d%Y%H%M%S")
    rand_text = "".join(sample(string.ascii_uppercase, k=rand_text_size))
    return f'{time_text}{rand_text}.jpeg'
