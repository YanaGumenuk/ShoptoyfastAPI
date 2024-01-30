from typing import Optional

from sqlalchemy import insert, select

from src.common.dto.image.images import (
    ProductCategoryImageDTO,
    ImageInDB,
)
from src.services.database.models.products.images import Image
from src.services.database.repositories import BaseCrud


class ImageCrudCategory(BaseCrud):
    async def create(
        self, url: str, category_id: int, new_image: ProductCategoryImageDTO
    ) -> Optional[ImageInDB]:
        stmt = (
            insert(Image)
            .values(url=url, category_id=category_id, **new_image.__dict__)
            .returning(Image)
        )
        result = await self.session.execute(stmt)
        await self.session.commit()
        return result.scalar_one_or_none()


class ImageCrudProduct(BaseCrud):
    async def create(
        self, url: str, product_id: int, new_image: ProductCategoryImageDTO
    ) -> Optional[ImageInDB]:
        stmt = (
            insert(Image)
            .values(url=url, product_id=product_id, **new_image.__dict__)
            .returning(Image)
        )
        result = await self.session.execute(stmt)
        await self.session.commit()
        return result.scalar_one_or_none()


class ImageCrud(BaseCrud):
    async def get_one(self, image_id: int) -> Optional[ImageInDB]:
        stmt = select(Image).where(Image.id == image_id)
        result = await self.session.execute(stmt)
        await self.session.commit()
        return result.scalar()
