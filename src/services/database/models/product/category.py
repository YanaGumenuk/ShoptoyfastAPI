from sqlalchemy import Integer, VARCHAR, String
from sqlalchemy.orm import Mapped, mapped_column

from src.services.database.models.base import Base


class Category(Base):
    __tablename__ = 'category'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, unique=True, index=True)