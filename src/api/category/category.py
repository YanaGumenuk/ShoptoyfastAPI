from fastapi import APIRouter, Depends
from src.services.database.repositories.category.category import CategoryCrud
from src.services.database.dto.category.category import CategoryCreate, CategoryInDB

router = APIRouter()


@router.post('/')
async def category_create(
        data: CategoryCreate,
        crud: CategoryCrud = Depends()
) -> CategoryInDB:
    result = await crud.create(data)
    return result


