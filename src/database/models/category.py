from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database.models.base import Base


class Category(Base):
    __tablename__: str = "categories"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, unique=True, index=True)
    parent_id: Mapped[int] = mapped_column(
        ForeignKey("categories.id", ondelete="CASCADE", onupdate="CASCADE")
    )

    parent = relationship("Category", backref="children")
    children = relationship("Category", backref="parent")

    products = relationship("Product", backref="categories")
    images = relationship("CategoryImage", backref="categories")
