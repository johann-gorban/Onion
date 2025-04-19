from sqlalchemy import String, DateTime
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from datetime import datetime


'''
Default class for tables
'''
class Base(DeclarativeBase):
    pass


'''
Class for publication
'''
class Publication(Base):
    __tablename__ = 'Publications'
    id:             Mapped[str] = mapped_column(String, primary_key=True)
    title:          Mapped[str] = mapped_column(String)
    content:        Mapped[str] = mapped_column(String)
    main_image_url: Mapped[str] = mapped_column(String)
    author_id:      Mapped[str] = mapped_column(String)
    company_id:     Mapped[str] = mapped_column(String)
    created_at:     Mapped[datetime] = mapped_column(DateTime)


'''
Class for company (organisation)
'''
class Company(Base):
    __tablename__ = 'Companies'
    id:             Mapped[str] = mapped_column(String, primary_key=True)
    name:           Mapped[str] = mapped_column(String)
    description:    Mapped[str] = mapped_column(String)
    image_url:      Mapped[str] = mapped_column(String)


'''
Abstract class for users
'''
class UserBase:
    id:         Mapped[str] = mapped_column(String, primary_key=True)
    first_name: Mapped[str] = mapped_column(String)
    last_name:  Mapped[str] = mapped_column(String)
    login:      Mapped[str] = mapped_column(String)
    password:   Mapped[str] = mapped_column(String)
    role:       Mapped[str] = mapped_column(String)


'''
Class author
'''
class Author(UserBase, Base):
    __tablename__ = 'Authors'
    company_id: Mapped[str] = mapped_column(String)


'''
Class moderator
'''
class Moderator(UserBase, Base):
    __tablename__ = 'Moderators'


'''
Class for Telegram subscriber
'''
class Subscriber(Base):
    __tablename__ = 'Subscribers'
    id:             Mapped[str] = mapped_column(String)
    telegram_id:    Mapped[str] = mapped_column(String)

'''
Table with Telegram subscriptions and companies users subscribed on
'''
class Subscription(Base):
    __tablename__ = 'Subscriptions'
    subscriber_id:  Mapped[str] = mapped_column(String)
    company_id:     Mapped[str] = mapped_column(String)