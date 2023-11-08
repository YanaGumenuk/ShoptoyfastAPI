from typing import List, Optional

from fastapi import APIRouter, Depends

from src.services.database.dto.category.category import CategoryCreate, CategoryInDB, CategoryUpdate, CategoryDelete
from src.services.database.repositories.category.category import CategoryCrud

router = APIRouter()


@router.post('/')
async def category_create(
        data: CategoryCreate,
        crud: CategoryCrud = Depends(CategoryCrud)
) -> CategoryInDB:
    result = await crud.create(new_category=data)
    return result


@router.get('/get_all')
async def category_get(
        crud: CategoryCrud = Depends(CategoryCrud)
) -> List[CategoryInDB]:
    result = await crud.get_all()
    return result


@router.get('/get_one')
async def category_get_one(
        category_id: int,
        crud: CategoryCrud = Depends(CategoryCrud)
) -> List[CategoryInDB]:
    result = await crud.get_one(category_id=category_id)
    return result


@router.put('/update')
async def update(
        data: CategoryUpdate,
        crud: CategoryCrud = Depends(CategoryCrud)
) -> CategoryInDB:
    result = await crud.update(category_id=data.id, name_category=data.name)
    return result


@router.post('/delete')
async def delete(
        data: CategoryDelete,
        crud: CategoryCrud = Depends(CategoryCrud)
) -> Optional[CategoryInDB]:
    result = await crud.delete(category_id=data.id)
    return result
