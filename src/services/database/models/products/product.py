import decimal
from sqlalchemy import Integer, String, ForeignKey, DECIMAL, Boolean, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.services.database.models import Base


class Product(Base):
    __tablename__ = 'products'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, unique=True, index=True)
    category_id: Mapped[int] = mapped_column(Integer, ForeignKey('category.id', ondelete='CASCADE'), nullable=True)
    image_id: Mapped[int] = mapped_column(Integer, ForeignKey('images.id', ondelete='CASCADE'), nullable=True)
    price: Mapped[int] = mapped_column(DECIMAL(10, 2), nullable=False)
    available: Mapped[bool] = mapped_column(Boolean, default=True)
    description: Mapped[str] = mapped_column(Text, default=None, nullable=True)

    category = relationship('Category', back_populates='products')
    images = relationship('Image', back_populates='products')
