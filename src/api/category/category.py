from typing import List, Optional

from fastapi import APIRouter, Depends
from fastapi.exceptions import HTTPException
from sqlalchemy.exc import IntegrityError

from src.common.dto.category.category import CategoryCreate, CategoryInDB
from src.services.database.repositories.category.category import CategoryCrud

router = APIRouter()


@router.post("/create")
async def category_create(
    data: CategoryCreate, crud: CategoryCrud = Depends(CategoryCrud)
) -> CategoryInDB:
    try:
        result = await crud.create(new_category=data)
        return result
    except IntegrityError:
        raise HTTPException(status_code=403, detail="Category exists")


@router.get("/list")
async def category_get(
    crud: CategoryCrud = Depends(CategoryCrud),
) -> List[CategoryInDB] | None:
    result = await crud.get_all()
    return result


@router.get("/detail/{id}")
async def category_get_one(
    data: int, crud: CategoryCrud = Depends(CategoryCrud)
) -> Optional[List[CategoryInDB]]:
    result = await crud.get_one(category_id=data)
    return result


@router.patch("/update/{id}")
async def update(
    category_id: int,
    data: CategoryCreate,
    crud: CategoryCrud = Depends(CategoryCrud),
) -> CategoryInDB | None:
    result = await crud.update(category_id=category_id, name_category=data)
    return result


@router.delete("/delete/{id}")
async def delete(
    category_id: int, crud: CategoryCrud = Depends(CategoryCrud)
) -> Optional[CategoryInDB]:
    result = await crud.delete(category_id=category_id)
    return result
