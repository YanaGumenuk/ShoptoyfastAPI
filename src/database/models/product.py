from sqlalchemy import DECIMAL, Boolean, ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database.models.base import Base


class Product(Base):
    __tablename__: str = "products"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, unique=True, index=True)
    code: Mapped[str] = mapped_column(String, nullable=False)
    category_id: Mapped[int] = mapped_column(
        ForeignKey("categories.id", ondelete="CASCADE", onupdate="CASCADE")
    )
    price: Mapped[int] = mapped_column(DECIMAL(10, 2), nullable=False)
    available: Mapped[bool] = mapped_column(Boolean, default=True)
    description: Mapped[str] = mapped_column(Text, default=None, nullable=True)
    images = relationship("ProductImage", backref="products")
