from fastapi import APIRouter, Depends

from src.services.database.dto.category.category import CategoryCreate, CategoryInDB
from src.services.database.repositories.category.category import CategoryCrud

router = APIRouter()


@router.post('/')
async def category_create(
        data: CategoryCreate,
        crud: CategoryCrud = Depends(CategoryCrud)
) -> CategoryInDB:
    result = await crud.create(new_category=data)
    return result



