import os.path

from fastapi import APIRouter, Depends, File, HTTPException

from fastapi import UploadFile
from starlette.responses import FileResponse
from starlette.staticfiles import StaticFiles

from src.common.constant.constant import URL, Directory
from src.common.dto.image.images import (
    ImageDTO,
    ProductImageCategoryDTO,
)
from src.common.filechek.file_chek import check_file
from src.services.database.repositories.image.image import (
    ImageCrudCategory,
    ImageCrudProduct,
    ImageCrud,
)

router = APIRouter()

router.mount("/static", StaticFiles(directory=Directory), name="static")

file_path = URL


@router.post("/upload_file/create/category/{id}")
async def create_file_category(
    category_id: int,
    file: UploadFile = File(...),
    data: ProductImageCategoryDTO = Depends(),
    crud: ImageCrudCategory = Depends(ImageCrudCategory),
) -> ImageDTO:
    check_file(file)
    with open(file_path, "wb") as f:
        f.write(await file.read())
    result = await crud.create(
        url=file_path, category_id=category_id, new_image=data
    )
    return result


@router.post("/upload_file/create/product/{id}")
async def create_file_product(
    product_id: int,
    file: UploadFile = File(...),
    data: ProductImageCategoryDTO = Depends(),
    crud: ImageCrudProduct = Depends(ImageCrudProduct),
) -> ImageDTO:
    check_file(file)
    with open(file_path, "wb") as f:
        f.write(await file.read())
    result = await crud.create(
        url=file_path, product_id=product_id, new_image=data
    )
    return result


@router.get("/images/{image_id}")
async def get_image(image_id: int, crud: ImageCrud = Depends(ImageCrud)):
    result = await crud.get_one(image_id=image_id)
    if result and os.path.isfile(result.url):
        return FileResponse(result.url)
    raise HTTPException(status_code=404, detail="Image not found")
