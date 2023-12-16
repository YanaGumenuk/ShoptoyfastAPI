import string
from random import choice, random
from datetime import datetime
from typing import List, Optional

from fastapi import APIRouter, Depends
from sqlalchemy import insert, select, update, delete

from fastapi import UploadFile, HTTPException
from starlette.staticfiles import StaticFiles

from src.common.dto.image.images import ImageInDB, ProductImageDTO
from src.services.database.models.products.images import Image
from src.services.database.repositories import BaseCrud
from src.services.database.repositories.product.product import ProductCrud
from pydantic import ValidationError

router = APIRouter()

router.mount('/static', StaticFiles(directory='C:\\images'), name='static')


class ImageCrud(BaseCrud):

    async def create(self, url: str, new_image: ProductImageDTO) -> Optional[ImageInDB]:
        print(8)
        stmt = (insert(Image).values(Image.url == url, **new_image.__dict__).returning(Image))
        result = await self.session.execute(stmt)
        await self.session.commit()
        return result.scalar_one_or_none()




@router.post('/uploadfile/')
async def create_upload_file(file: UploadFile, data: ProductImageDTO,
                             crud: ImageCrud = Depends(ImageCrud)) -> Optional[ImageInDB]:
    print(9)
    if not file.content_type == 'image/jpeg' and not file.size <= 300000:
        raise HTTPException(status_code=500, detail='ti menya ne na.. provedesh')
    now = datetime.now()
    name = now.strftime("%m%d%Y%H%M%S")
    for i in range(6):
        name = str(name) + choice(string.ascii_uppercase)
    filename = f'{name}.jpeg'
    file_path = f'C:\\images\\{filename}'
    with open(f'C:\\images\\{name}.jpeg', 'wb') as f:
        f.write(await file.read())
    result = await crud.create(url=file_path, new_image=data)
    return result

def validate_data(data: ProductImageDTO):
    ProductImageDTO(**data.__dict__)

print(validate_data.__dict__)

# url = f'C:\\images\\{create_upload_file.name}.jpeg'
# class ProductCrud(BaseCrud):
# async def create(self):
# stmt = (insert(Image).values(Image.url == url).returning(Image))
# result = await self.session.execute(stmt)
# await self.session.commit()
# return result.scalar_one_or_none()


# @router.post('/')
# async def create(
# crud: ProductCrud = Depends(ProductCrud)
# ) -> List[ImageInDB] | None:
# result = await crud.create()
# return result
