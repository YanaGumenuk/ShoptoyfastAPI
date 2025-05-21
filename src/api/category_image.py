import os.path

from fastapi import APIRouter, Depends, File, HTTPException, UploadFile
from starlette.responses import FileResponse

from src.common.constants.constant import IMAGES_DIR
from src.common.dto.category_images import (
    CategoryImagesDTO,
    CategoryImagesInDB,
)
from src.common.file_check.file_check import check_file, generate_file_id
from src.database.repositories.category_image import (
    CategoryImageCrud,
)

router = APIRouter(prefix="/categories-images", tags=["CategoryImage"])


@router.post("")
async def create_file_category(
    category_id: int,
    file: UploadFile = File(...),
    data: CategoryImagesDTO = Depends(),
    crud: CategoryImageCrud = Depends(CategoryImageCrud),
) -> CategoryImagesInDB:
    check_file(file)
    file_id = generate_file_id()
    file_path = IMAGES_DIR + file_id + ".jpeg"
    with open(file_path, "wb") as f:
        f.write(await file.read())
    result = await crud.create(
        file_id=file_id, category_id=category_id, new_image=data
    )
    return result


@router.get("")
async def get_image(
    image_id: int, crud: CategoryImageCrud = Depends(CategoryImageCrud)
):
    result = await crud.get_one(image_id=image_id)
    if result and os.path.isfile(IMAGES_DIR + result.file_id + ".jpeg"):
        return FileResponse(IMAGES_DIR + result.file_id + ".jpeg")
    raise HTTPException(status_code=404, detail="Image not found")


@router.delete("/{image_id}")
async def image_delete(
    image_id: int, crud: CategoryImageCrud = Depends(CategoryImageCrud)
) -> CategoryImagesInDB:
    result = await crud.delete(image_id=image_id)
    if result:
        return result
    raise HTTPException(status_code=404, detail="Image not found")
