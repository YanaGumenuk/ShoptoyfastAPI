from typing import Optional, List


from sqlalchemy import insert, select, update, delete


from src.common.dto.category.category import CategoryCreate, CategoryInDB
from src.services.database.repositories.base import BaseCrud

from src.services.database.models.products.category import Category


class CategoryCrud(BaseCrud):

    async def create(self, new_category: CategoryCreate) -> CategoryInDB:
        stmt = (insert(Category).values(**new_category.__dict__).returning(Category))
        print(3)
        result = await self.session.execute(stmt)
        await self.session.commit()
        return result.scalar_one_or_none()



    async def get_all(self) -> Optional[List[CategoryInDB]]:
        stmt = (select(Category))
        result = await self.session.execute(stmt)
        print(4)
        return result.scalars().all()

    async def get_one(self, category_id: int) -> Optional[CategoryInDB]:
        stmt = (select(Category).where(Category.id == category_id))
        result = await self.session.execute(stmt)
        print(5)
        return result.first()

    async def update(self, category_id: int, name_category: str) -> Optional[CategoryInDB]:
        stmt = (
            update(Category)
            .where(Category.id == category_id)
            .values(name=name_category)
            .returning(Category)
        )
        result = await self.session.execute(stmt)
        await self.session.commit()
        print(6)
        return result.scalar()

    async def delete(self, category_id: int) -> Optional[CategoryInDB]:
        stmt = (delete(Category).where(Category.id == category_id).returning(Category))
        result = await self.session.execute(stmt)
        await self.session.commit()
        print(7)
        return result.scalar()
