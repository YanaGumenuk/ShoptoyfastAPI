import decimal

from pydantic import BaseModel, condecimal

from src.common.dto.base import BaseInDB


class ProductUpdateDTO(BaseModel):
    name: str
    category_id: int
    price: condecimal(max_digits=10, decimal_places=2)
    available: bool = True
    description: str

    class Config:
        from_attributes = True
        json_schema_extra = {
            'name': "Toy",
            'price': '178.9',
            'available': 'True',
            'description': 'Loren ipsum',
        }


class ProductCreateDTO(ProductUpdateDTO):
    category_id: int

    class Config:
        from_attributes = True
        json_schema_extra = {
            'name': "Toy",
            'price': '178.9',
            'available': 'True',
            'description': 'Loren ipsum',
        }


class ProductInDB(BaseInDB, ProductCreateDTO):
    class Config:
        from_attributes = True
        json_schema_extra = {
            'id': 1,
            'create_at': '2023-11-15 22:03:21.605901 +00:00',
            'updated_at': '2023-11-15 22:03:21.605901 +00:00',
            'name': "Toy",
            'category_id': '2',
            'price': '178.9',
            'available': 'True',
            'description': 'Loren ipsum',
        }


class ProductUpdateInDB(BaseModel):
    id: int
    name: str
    category_id: int
    price: condecimal(max_digits=10, decimal_places=2)
    available: bool
    description: str

    class Config:
        from_attributes = True
        json_schema_extra = {
            'id': 1,
            'name': "Toy",
            'category_id': '2',
            'price': '178.9',
            'available': 'True',
            'description': 'Loren ipsum',
        }
