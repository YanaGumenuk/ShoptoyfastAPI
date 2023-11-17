from typing import Optional, List

from fastapi import APIRouter, Depends

from src.common.dto.products.product import ProductCreateDTO, ProductInDB, ProductUpdateInDB
from src.services.database.repositories.product.product import ProductCrud

router = APIRouter()


@router.post('/')
async def product_create(
        data: ProductCreateDTO,
        crud: ProductCrud = Depends(ProductCrud)
) -> ProductInDB:
    result = await crud.create(new_product=data)
    return result


@router.get('/get_all')
async def product_get(
        crud: ProductCrud = Depends(ProductCrud)
) -> List[ProductInDB] | None:
    result = await crud.get_all()
    return result


@router.get('/get_one')
async def product_get_one(
        product_id: int,
        crud: ProductCrud = Depends(ProductCrud)
) -> Optional[List[ProductInDB]]:
    result = await crud.get_one(product_id=product_id)
    return result


@router.put('/update')
async def product_update(
        data: ProductUpdateInDB,
        crud: ProductCrud = Depends(ProductCrud)
) -> ProductInDB | None:
    result = await crud.update(product_id=data.id,
                               category_id=data.category_id,
                               product_name=data.name,
                               product_available=data.available,
                               product_price=data.price,
                               product_description=data.description)
    return result


@router.post('/delete')
async def product_delete(
        product_id: int,
        crud: ProductCrud = Depends(ProductCrud)
) -> Optional[ProductInDB]:
    result = await crud.delete(product_id=product_id)
    return result
