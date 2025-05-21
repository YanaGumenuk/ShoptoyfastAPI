from decimal import Decimal
from typing import Annotated, Any

from pydantic import BaseModel, Field

from src.common.constants.constant import BASE_PRODUCT_IMAGE_URL
from src.common.dto.base import BaseInDB

PriceType = Annotated[Decimal, Field(max_digits=10, decimal_places=2)]


class ProductDTO(BaseModel):
    name: str
    code: str
    category_id: int
    price: PriceType
    available: bool = True
    description: str

    class Config:
        from_attributes = True


class ProductInDB(BaseInDB, ProductDTO):
    pass


class ProductWithImagesInDB(ProductInDB):
    image_links: list[dict]

    @classmethod
    def model_validate(
        cls,
        obj: Any,
        *,
        strict: bool | None = None,
        from_attributes: bool | None = None,
        context: dict[str, Any] | None = None,
    ):
        product_in_db = ProductInDB.model_validate(
            obj,
            strict=strict,
            from_attributes=from_attributes,
            context=context,
        )
        image_links = [
            {
                "id": image.id,
                "link": f"{BASE_PRODUCT_IMAGE_URL}{image.id}",
                "main": image.is_main_image,
            }
            for image in obj.images
        ]
        return ProductWithImagesInDB(
            **product_in_db.model_dump(),
            image_links=image_links,
        )
