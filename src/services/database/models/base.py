from datetime import datetime
from sqlalchemy import DateTime
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    created_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True), nullable=False, default=datetime.now
    )
    updated_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        default=datetime.now,
        onupdate=datetime.now,
    )
