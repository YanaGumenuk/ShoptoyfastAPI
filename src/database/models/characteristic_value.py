from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database.models.base import Base


class CharacteristicValue(Base):
    __tablename__: str = "characteristic_values"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    value: Mapped[str]
    characteristic_id: Mapped[int] = mapped_column(
        ForeignKey(
            "characteristic_names.id", ondelete="CASCADE", onupdate="CASCADE"
        )
    )
    product_id: Mapped[int] = mapped_column(
        ForeignKey("products.id", ondelete="CASCADE", onupdate="CASCADE")
    )
    characteristic_name = relationship(
        "CharacteristicName", backref="characteristic_values"
    )
    product = relationship("Product", backref="characteristic_values")
