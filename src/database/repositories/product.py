from decimal import Decimal
from typing import Annotated

from pydantic import Field
from sqlalchemy import delete, insert, select, update
from sqlalchemy.orm import joinedload, selectinload

from src.common.dto.product import (
    ProductDTO,
    ProductInDB,
    ProductWithImagesInDB,
)
from src.database.models.product import Product
from src.database.repositories import BaseCrud

PriceType = Annotated[
    Decimal, Field(strict=True, max_digits=10, decimal_places=2)
]


class ProductCrud(BaseCrud):
    async def create(self, new_product: ProductDTO) -> ProductInDB:
        stmt = (
            insert(Product).values(**new_product.__dict__).returning(Product)
        )
        result = await self.session.execute(stmt)
        await self.session.commit()
        result_orm = result.scalar()
        return ProductInDB.model_validate(result_orm)

    async def get_all(
        self, offset: int, limit: int
    ) -> list[ProductWithImagesInDB]:
        stmt = (
            select(Product)
            .options(selectinload(Product.images))
            .offset(offset)
            .limit(limit)
        )
        result = await self.session.execute(stmt)
        result_orm = result.scalars().all()
        return [
            ProductWithImagesInDB.model_validate(row) for row in result_orm
        ]

    async def get_one(self, product_id: int) -> ProductWithImagesInDB | None:
        stmt = (
            select(Product)
            .options(joinedload(Product.images))
            .where(Product.id == product_id)
        )
        result = await self.session.execute(stmt)
        result_orm = result.scalar()
        return (
            ProductWithImagesInDB.model_validate(result_orm)
            if result_orm
            else None
        )

    async def update(
        self,
        product_id: int,
        product_name: str,
        category_id: int,
        product_price: PriceType,
        product_available: bool,
        product_description: str,
    ) -> ProductInDB | None:
        stmt = (
            update(Product)
            .where(Product.id == product_id)
            .values(
                name=product_name,
                category_id=category_id,
                price=product_price,
                available=product_available,
                description=product_description,
            )
            .returning(Product)
        )
        result = await self.session.execute(stmt)
        await self.session.commit()
        result_orm = result.scalar()
        return ProductInDB.model_validate(result_orm) if result_orm else None

    async def delete(self, product_id: int) -> ProductInDB | None:
        stmt = (
            delete(Product).where(Product.id == product_id).returning(Product)
        )
        result = await self.session.execute(stmt)
        await self.session.commit()
        result_orm = result.scalar()
        return ProductInDB.model_validate(result_orm) if result_orm else None
