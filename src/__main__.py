from fastapi import FastAPI

from src.api import category, category_image, product, product_image

app = FastAPI(title="Gumenyuk_shop")


app.include_router(category.router)
app.include_router(product.router)
app.include_router(category_image.router)
app.include_router(product_image.router)
