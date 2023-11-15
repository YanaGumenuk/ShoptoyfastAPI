from pydantic import BaseModel

from src.common.dto.base import BaseInDB


class CategoryCreate(BaseModel):
    name: str

    class Config:
        from_attributes = True
        json_schema_extra = {
            "name": "Toy"
        }


class CategoryInDB(
    CategoryCreate,
    BaseInDB
):
    class Config:
        from_attributes = True
        json_schema_extra = {
            "id": 1,
            "created_at": "2023-04-02 22:26:20.245464 +00:00",
            "updated_at": "2023-04-02 22:26:20.245464 +00:00",
            "name": "Toy",
        }


class CategoryUpdate(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True
        json_schema_extra = {
            'id': 1,
            'name': 'Toy'
        }


class CategoryDelete(BaseModel):
    id: int

    class Config:
        from_attributes = True
        json_schema_extra = {
            'id': 1
        }
