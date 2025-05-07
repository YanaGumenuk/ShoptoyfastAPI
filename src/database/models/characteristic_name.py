from sqlalchemy import Integer
from sqlalchemy.orm import Mapped, mapped_column

from src.database.models.base import Base


class CharacteristicName(Base):
    __tablename__: str = "characteristic_names"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str]
