import string
from random import choice, random
from datetime import datetime
from fastapi import APIRouter

from fastapi import UploadFile, HTTPException


router = APIRouter()


@router.post('uploadfile/')
async def create_upload_file(file: UploadFile):
    if not file.content_type == 'image/jpeg' and not file.size <= 300000:
        raise HTTPException(status_code=500, detail='ti menya ne na.. provedesh')
    now = datetime.now()
    name = now.strftime("%m%d%Y%H%M%S")
    for i in range(6):
        name = str(name) + choice(string.ascii_uppercase)
    with open(f'C:\\images\\{name}.jpeg', 'wb') as f:
        f.write(await file.read())

