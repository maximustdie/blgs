from typing import Optional

from sqlalchemy import String, text
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import UUID

from db.pg import Base


class User(Base):
    __tablename__ = "user_account"

    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True),
                                     primary_key=True,
                                     default=text('gen_random_uuid()')
                                     )
    name: Mapped[Optional[str]] = mapped_column(nullable=True)
    username: Mapped[Optional[str]]
    fullname: Mapped[Optional[str]] = mapped_column(String(30), nullable=True)
