from fastapi import FastAPI
from starlette.staticfiles import StaticFiles

from src.api.product import product
from src.api.category import category
from src.common.images_StaticFiles import files

app = FastAPI(
    title='Gumenyuk_shop'
)

app.mount('/static', StaticFiles(directory='C:\\images'), name='static')

app.include_router(category.router,
                   prefix='/category',
                   tags=['Category'])
app.include_router(product.router,
                   prefix='/product',
                   tags=['Product'])
app.include_router(files.router,
                   prefix='/files',
                   tags=['files'])
