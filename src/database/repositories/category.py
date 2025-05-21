from sqlalchemy import delete, insert, select, update
from sqlalchemy.orm import joinedload, selectinload

from src.common.dto.category import (
    CategoryDTO,
    CategoryInDB,
    CategoryWithImagesInDB,
)
from src.database.models.category import Category
from src.database.repositories.base import BaseCrud


class CategoryCrud(BaseCrud):
    async def create(self, new_category: CategoryDTO) -> CategoryInDB:
        stmt = (
            insert(Category)
            .values(**new_category.__dict__)
            .returning(Category)
        )
        result = await self.session.execute(stmt)
        await self.session.commit()
        result_orm = result.scalar_one()
        return CategoryInDB.model_validate(result_orm)

    async def get_all(
        self, offset: int, limit: int
    ) -> list[CategoryWithImagesInDB]:
        stmt = (
            select(Category)
            .options(selectinload(Category.images))
            .offset(offset)
            .limit(limit)
        )
        result = await self.session.execute(stmt)
        result_orm = result.scalars().all()
        return [
            CategoryWithImagesInDB.model_validate(row) for row in result_orm
        ]

    async def get_one(self, category_id: int) -> CategoryWithImagesInDB | None:
        stmt = (
            select(Category)
            .options(joinedload(Category.images))
            .where(Category.id == category_id)
        )
        result = await self.session.execute(stmt)
        result_orm = result.scalar()
        return (
            CategoryWithImagesInDB.model_validate(result_orm)
            if result_orm
            else None
        )

    async def update(
        self, category_id: int, name_category: CategoryDTO
    ) -> CategoryInDB | None:
        stmt = (
            update(Category)
            .where(Category.id == category_id)
            .values(name=name_category.name)
            .returning(Category)
        )
        result = await self.session.execute(stmt)
        await self.session.commit()
        result_orm = result.scalar()
        return CategoryInDB.model_validate(result_orm) if result_orm else None

    async def delete(self, category_id: int) -> CategoryInDB | None:
        stmt = (
            delete(Category)
            .where(Category.id == category_id)
            .returning(Category)
        )
        result = await self.session.execute(stmt)
        await self.session.commit()
        result_orm = result.scalar()
        return CategoryInDB.model_validate(result_orm) if result_orm else None
