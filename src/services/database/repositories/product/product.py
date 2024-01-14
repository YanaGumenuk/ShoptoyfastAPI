
from typing import Optional, List

from pydantic import condecimal
from sqlalchemy import insert, select, update, delete

from src.common.dto.products.product import ProductCreateDTO, ProductInDB
from src.services.database.models.products.product import Product
from src.services.database.repositories import BaseCrud


class ProductCrud(BaseCrud):
    async def create(self, new_product: ProductCreateDTO) -> Optional[ProductInDB]:
        stmt = (insert(Product).values(**new_product.__dict__).returning(Product))
        result = await self.session.execute(stmt)
        await self.session.commit()
        return result.scalar_one_or_none()

    async def get_all(self) -> Optional[List[ProductInDB]]:
        stmt = (select(Product))
        result = await self.session.execute(stmt)
        return result.scalars().all()

    async def get_one(self, product_id: int) -> Optional[ProductInDB]:
        stmt = (select(Product).where(Product.id == product_id))
        result = await self.session.execute(stmt)
        return result.first()

    async def update(self, product_id: int,
                     product_name: str,
                     category_id: int,
                     product_price: condecimal(max_digits=10, decimal_places=2),
                     product_available: bool,
                     product_description: str) -> Optional[ProductInDB]:
        stmt = (update(Product).where(Product.id == product_id).values(name=product_name,
                                                                       category_id=category_id,
                                                                       price=product_price,
                                                                       available=product_available,
                                                                       description=product_description).
                returning(Product)
                )
        result = await self.session.execute(stmt)
        await self.session.commit()
        return result.scalar()

    async def delete(self, product_id: int) -> Optional[ProductInDB]:
        stmt = (delete(Product).where(Product.id == product_id).returning(Product))
        result = await self.session.execute(stmt)
        await self.session.commit()
        return result.scalar()
