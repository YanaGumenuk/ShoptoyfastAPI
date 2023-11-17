from fastapi import FastAPI

from src.api.product import product
from src.api.category import category

app = FastAPI(
    title='Gumenyuk_shop'
)

app.include_router(category.router,
                   prefix='/category',
                   tags=['Category'])
app.include_router(product.router,
                   prefix='/product',
                   tags=['Product'])
