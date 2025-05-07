from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column

from src.database.models.base import Base


class ProductImage(Base):
    __tablename__: str = "product_images"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    file_id: Mapped[str]
    product_id: Mapped[int] = mapped_column(
        ForeignKey("products.id", ondelete="CASCADE", onupdate="CASCADE"),
    )
    is_main_image: Mapped[bool]


class CategoryImage(Base):
    __tablename__: str = "category_images"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    file_id: Mapped[str]
    category_id: Mapped[int] = mapped_column(
        ForeignKey("categories.id", ondelete="CASCADE", onupdate="CASCADE"),
    )
    is_main_image: Mapped[bool]
