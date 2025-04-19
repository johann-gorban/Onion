from sqlalchemy import String, DateTime
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from datetime import datetime

class Base(DeclarativeBase):
    pass


class Publication(Base):
    __tablename__ = 'Publications'
    id:             Mapped[str] = mapped_column(String, primary_key=True)
    title:          Mapped[str] = mapped_column(String)
    content:        Mapped[str] = mapped_column(String)
    main_image_url: Mapped[str] = mapped_column(String)
    author_id:      Mapped[str] = mapped_column(String)
    company_id:     Mapped[str] = mapped_column(String)
    created_at:     Mapped[datetime] = mapped_column(DateTime)


class Company(Base):
    __tablename__ = 'Companies'
    id:             Mapped[str] = mapped_column(String, primary_key=True)
    name:           Mapped[str] = mapped_column(String)
    description:    Mapped[str] = mapped_column(String)
    image_url:      Mapped[str] = mapped_column(String)


class UserBase:
    id:         Mapped[str] = mapped_column(String, primary_key=True)
    first_name: Mapped[str] = mapped_column(String)
    last_name:  Mapped[str] = mapped_column(String)
    login:      Mapped[str] = mapped_column(String)
    password:   Mapped[str] = mapped_column(String)
    role:       Mapped[str] = mapped_column(String)


class Writer(UserBase, Base):
    __tablename__ = 'Writers'
    company_id: Mapped[str] = mapped_column(String)


class Moderator(UserBase, Base):
    __tablename__ = 'Moderators'

