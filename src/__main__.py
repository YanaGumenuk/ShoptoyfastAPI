from fastapi import FastAPI
from starlette.staticfiles import StaticFiles

from src.api.product import product
from src.api.category import category
from src.api.image import files

app = FastAPI(
    title='Gumenyuk_shop'
)


app.include_router(category.router,
                   prefix='/category',
                   tags=['Category'])
app.include_router(product.router,
                   prefix='/products',
                   tags=['Product'])
app.include_router(files.router,
                   prefix='/files',
                   tags=['files'])
