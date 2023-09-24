

from sqlalchemy import insert

from src.services.database.repositories.base import BaseCrud
from src.services.database.dto.category.category import CategoryCreate
from src.services.database.models.product.category import Category


class CategoryCrud(BaseCrud):

    async def create(self, new_operation: CategoryCreate):
        stmt = (insert(Category).values(**new_operation.__dict__)
                )
        result = await self.session.execute(stmt)
        await self.session.commit()
        return result

