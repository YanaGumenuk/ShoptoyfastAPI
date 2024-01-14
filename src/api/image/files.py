from typing import List, Optional

from fastapi import APIRouter, Depends, File
from sqlalchemy import insert, select, update, delete

from fastapi import UploadFile
from starlette.staticfiles import StaticFiles

from src.common.dto.image.images import ImageInDB, ProductImageDTO, ImageDTO, ProductImageCategoryDTO
from src.common.filechek.file_chek import check_file, generate_file_name
from src.services.database.models.products.images import Image
from src.services.database.repositories import BaseCrud
from src.services.database.repositories.image.image import ImageCrud, ImageCrud2

router = APIRouter()

router.mount('/static', StaticFiles(directory='C:\\images'), name='static')


@router.post('/upload_file/create/{id}')
async def create_file_category(category_id: int,
                               file: UploadFile = File(...),
                               data: ProductImageCategoryDTO = Depends(),
                               crud: ImageCrud = Depends(ImageCrud)) -> ImageDTO:
    check_file(file)
    file_name = generate_file_name()
    file_path = f'C:\\images\\{file_name}'
    with open(file_path, 'wb') as f:
        f.write(await file.read())
    result = await crud.create(url=file_path, category_id=category_id, new_image=data)
    return result


@router.post('/upload_file/create2/{id}')
async def create_file_product(product_id: int,
                              file: UploadFile = File(...),
                              data: ProductImageDTO = Depends(),
                              crud: ImageCrud2 = Depends(ImageCrud2)) -> ImageDTO:
    check_file(file)
    file_name = generate_file_name()
    file_path = f'C:\\images\\{file_name}'
    with open(file_path, 'wb') as f:
        f.write(await file.read())
    result = await crud.create(url=file_path, product_id=product_id, new_image=data)
    return result
