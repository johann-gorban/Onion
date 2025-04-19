from datetime import datetime
from typing import Any

from sqlalchemy import DateTime, ForeignKey, Integer, String
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(AsyncAttrs, DeclarativeBase):
    """Default class for tables"""

    __abstract__ = True


class Publication(Base):
    __tablename__ = "Publications"
    id: Mapped[str] = mapped_column(String, primary_key=True)
    title: Mapped[str] = mapped_column(String)
    content: Mapped[str] = mapped_column(String)
    main_image_url: Mapped[str] = mapped_column(String)
    created_at: Mapped[datetime] = mapped_column(DateTime)

    # Foreign keys
    author_id: Mapped[str] = mapped_column(String, ForeignKey("Authors.id"))
    company_id: Mapped[str] = mapped_column(String, ForeignKey("Companies.id"))

    # Relationships
    author: Mapped["Author"] = relationship(back_populates="publications")
    company: Mapped["Company"] = relationship(back_populates="publications")


class Company(Base):
    __tablename__ = "Companies"
    id: Mapped[str] = mapped_column(String, primary_key=True)
    name: Mapped[str] = mapped_column(String)
    description: Mapped[str] = mapped_column(String)
    image_url: Mapped[str] = mapped_column(String)

    # Relationships
    publications: Mapped[list["Publication"]] = relationship(
        back_populates="company"
    )
    authors: Mapped[list["Author"]] = relationship(back_populates="company")
    subscriptions: Mapped[list["Subscription"]] = relationship(
        back_populates="company"
    )

    def to_json(self, include_relationships: bool = True) -> dict[str, Any]:
        result = {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "image_url": self.image_url,
        }

        if include_relationships:
            result.update(
                {
                    "publications": [
                        p.to_json(include_relationships=False)
                        for p in self.publications
                    ],
                    "authors": [
                        a.to_json(include_relationships=False)
                        for a in self.authors
                    ],
                    "subscriptions": [
                        s.to_json(include_relationships=False)
                        for s in self.subscriptions
                    ],
                }
            )
        return


class UserBase:
    id: Mapped[str] = mapped_column(String, primary_key=True)
    first_name: Mapped[str] = mapped_column(String)
    last_name: Mapped[str] = mapped_column(String)
    login: Mapped[str] = mapped_column(String)
    password: Mapped[str] = mapped_column(String)
    role: Mapped[str] = mapped_column(String)


class Author(UserBase, Base):
    __tablename__ = "Authors"
    company_id: Mapped[str] = mapped_column(String, ForeignKey("Companies.id"))

    # Relationships
    company: Mapped["Company"] = relationship(back_populates="authors")
    publications: Mapped[list["Publication"]] = relationship(
        back_populates="author"
    )


class Moderator(UserBase, Base):
    __tablename__ = "Moderators"


class Subscriber(Base):
    __tablename__ = "Subscribers"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    telegram_id: Mapped[str] = mapped_column(String)

    # Relationships
    subscriptions: Mapped[list["Subscription"]] = relationship(
        back_populates="subscriber"
    )


class Subscription(Base):
    __tablename__ = "Subscriptions"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    subscriber_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("Subscribers.id")
    )
    company_id: Mapped[str] = mapped_column(String, ForeignKey("Companies.id"))

    # Relationships
    subscriber: Mapped["Subscriber"] = relationship(
        back_populates="subscriptions"
    )
    company: Mapped["Company"] = relationship(back_populates="subscriptions")
