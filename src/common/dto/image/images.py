from typing import Optional

from src.common.dto.base import BaseInDB
from pydantic import BaseModel


class ImageDTO(BaseModel):
    category_id: Optional[int] = None
    product_id: Optional[int] = None
    is_main_image: bool = True

    class Config:
        from_attributes = True
        json_schema_extra = {
            "category_id": 1,
            "product_id": 1,
            "is_main_image": True,
        }


class ImageInDB(ImageDTO, BaseInDB):
    url: str

    class Config:
        from_attributes = True
        json_schema_extra = {
            "id": 1,
            "url": "fuftuf",
            "created_at": "2023-04-02 22:26:20.245464 +00:00",
            "updated_at": "2023-04-02 22:26:20.245464 +00:00",
            "category_id": 1,
            "product_id": 1,
            "is_main_image": True,
        }


class ProductCategoryImageDTO(BaseModel):
    is_main_image: bool = True

    class Config:
        from_attributes = True
        json_schema_extra = {"is_main_image": True}


class ImageIdDTO(BaseModel):
    url: str

    class Config:
        from_attributes = True
        json_schema_extra = {"url": "hj"}
