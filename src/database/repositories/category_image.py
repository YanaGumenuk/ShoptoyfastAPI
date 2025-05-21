from sqlalchemy import delete, insert, select

from src.common.dto.category_images import (
    CategoryImagesDTO,
    CategoryImagesInDB,
)
from src.database.models.image import CategoryImage
from src.database.repositories import BaseCrud


class CategoryImageCrud(BaseCrud):
    async def create(
        self, file_id: str, category_id: int, new_image: CategoryImagesDTO
    ):
        stmt = (
            insert(CategoryImage)
            .values(
                file_id=file_id, category_id=category_id, **new_image.__dict__
            )
            .returning(CategoryImage)
        )
        result = await self.session.execute(stmt)
        await self.session.commit()
        result_orm = result.scalar_one_or_none()
        return CategoryImagesInDB.model_validate(result_orm)

    async def get_one(self, image_id: int) -> CategoryImagesInDB | None:
        stmt = select(CategoryImage).where(CategoryImage.id == image_id)
        result = await self.session.execute(stmt)
        await self.session.commit()
        result_orm = result.scalar()
        return (
            CategoryImagesInDB.model_validate(result_orm)
            if result_orm
            else None
        )

    async def delete(self, image_id: int) -> CategoryImagesInDB | None:
        stmt = (
            delete(CategoryImage)
            .where(CategoryImage.id == image_id)
            .returning(CategoryImage)
        )
        result = await self.session.execute(stmt)
        await self.session.commit()
        result_orm = result.scalar()
        return (
            CategoryImagesInDB.model_validate(result_orm)
            if result_orm
            else None
        )
