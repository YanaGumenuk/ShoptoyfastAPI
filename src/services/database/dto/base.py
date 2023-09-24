from pydantic import BaseModel
from datetime import datetime


class BaseInDB(BaseModel):
    id: int
    created_at: datetime
    updated_at: datetime
