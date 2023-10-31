import typing

from sqlalchemy import insert

from src.services.database.repositories.base import BaseCrud
from src.services.database.dto.category.category import CategoryCreate, CategoryInDB
from src.services.database.models.product.category import Category


class CategoryCrud(BaseCrud):

    async def create(self, new_category: CategoryCreate) -> CategoryInDB:
        stmt = (insert(Category).values(**new_category.__dict__).returning(Category))
        result = await self.session.execute(stmt)
        await self.session.commit()
        return result.scalar_one_or_none()
