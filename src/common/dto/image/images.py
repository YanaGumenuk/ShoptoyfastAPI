from src.common.dto.base import BaseInDB
from pydantic import BaseModel


class ProductImageDTO(BaseModel):
    url: str
