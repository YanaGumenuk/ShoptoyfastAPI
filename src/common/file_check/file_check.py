import string
from datetime import datetime
from random import sample

from fastapi import HTTPException, UploadFile


def check_file(file: UploadFile):
    if file.content_type != "images/jpeg" or (
        file.size is not None and file.size > 300000
    ):
        raise HTTPException(
            status_code=500, detail="Extension is not suitable"
        )


def generate_file_id(rand_text_size: int = 6):
    time_text = datetime.now().strftime("%m%d%Y%H%M%S")
    rand_text = "".join(sample(string.ascii_uppercase, k=rand_text_size))
    return f"{time_text}{rand_text}"
