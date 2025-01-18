from sqlalchemy import String
from sqlalchemy import Integer
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    password: Mapped[str] = mapped_column(String(255))
    comments: Mapped[str] = mapped_column(String(255))

    def __repr__(self) -> str:
        return f"<User(name={self.name}, password={self.password},comments={self.comments}>"
