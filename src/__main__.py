
from fastapi import FastAPI

from src.api.category import category

app = FastAPI(
    title='Gumenyuk_shop'
)

app.include_router(category.router,
                      prefix='/category',
                      tags=['Category'])



