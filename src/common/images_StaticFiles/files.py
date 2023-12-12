from typing import Annotated
from fastapi import APIRouter, Depends

from fastapi import FastAPI, File, UploadFile, HTTPException


router = APIRouter()

@router.post('/files')
async def create_file(file: Annotated[bytes, File()]):
    return {'file_size': len(file)}

@router.post('uploadfile/')
async def create_upload_file(file: UploadFile):
    if file.content_type == 'image/jpeg':
        return {'filename': file.filename}
    else:
        raise HTTPException(status_code=500, detail='ti menya ne na.. provedesh')