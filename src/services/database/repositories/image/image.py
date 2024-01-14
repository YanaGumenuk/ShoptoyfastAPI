from typing import Optional

from sqlalchemy import insert

from src.common.dto.image.images import ProductImageCategoryDTO, ImageInDB, ProductImageDTO
from src.services.database.models.products.images import Image
from src.services.database.repositories import BaseCrud


class ImageCrud(BaseCrud):
    async def create(
            self,
            url: str,
            category_id: int,
            new_image: ProductImageCategoryDTO
    ) -> Optional[ImageInDB]:
        stmt = (
            insert(Image).values(url=url, category_id=category_id, **new_image.__dict__).returning(Image))
        result = await self.session.execute(stmt)
        await self.session.commit()
        return result.scalar_one_or_none()


class ImageCrud2(BaseCrud):
    async def create(self, url: str, product_id: int, new_image: ProductImageDTO) -> Optional[ImageInDB]:
        stmt = (
            insert(Image).values(url=url, product_id=product_id, **new_image.__dict__).returning(Image))
        result = await self.session.execute(stmt)
        await self.session.commit()
        return result.scalar_one_or_none()
