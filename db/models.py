from sqlalchemy import String, DateTime, Integer, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
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
    created_at:     Mapped[datetime] = mapped_column(DateTime)

    # Foreign keys
    author_id:      Mapped[str] = mapped_column(String, ForeignKey('Authors.id'))
    company_id:     Mapped[str] = mapped_column(String, ForeignKey('Companies.id'))

    # Relationships
    author:         Mapped['Author'] = relationship(back_populates='publications')
    company:        Mapped['Company'] = relationship(back_populates='publications')


'''
Class for company (organisation)
'''
class Company(Base):
    __tablename__ = 'Companies'
    id:             Mapped[str] = mapped_column(String, primary_key=True)
    name:           Mapped[str] = mapped_column(String)
    description:    Mapped[str] = mapped_column(String)
    image_url:      Mapped[str] = mapped_column(String)

    # Relationships
    publications:   Mapped[list['Publication']] = relationship(back_populates='company')
    writers:        Mapped[list['Author']] = relationship(back_populates='company')
    subscriptions:  Mapped[list["Subscription"]] = relationship(back_populates="company")

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
    company_id:     Mapped[str] = mapped_column(String, ForeignKey('Companies.id'))

    # Relationships
    company:        Mapped[str] = relationship(back_populates='authors')
    publications:   Mapped[list['Publication']] = relationship(back_populates='author')


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
    id:             Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    telegram_id:    Mapped[str] = mapped_column(String)

    # Relationships
    subscriptions:  Mapped[list['Subscription']] = relationship(back_populates='subscriber')

'''
Table with Telegram subscriptions and companies users subscribed on
'''
class Subscription(Base):
    __tablename__ = 'Subscriptions'

    id:             Mapped[int] = mapped_column(primary_key=True, autoincrement=True) 

    # Foreign keys
    subscriber_id:  Mapped[int] = mapped_column(Integer, ForeignKey('Subscribers.id'))
    company_id:     Mapped[str] = mapped_column(String, ForeignKey('Companies.id'))

    # Relationships
    subscriber:     Mapped['Subscriber'] = relationship(back_populates='subscriptions')
    company:        Mapped['Company'] = relationship(back_populates='subscriptions')

