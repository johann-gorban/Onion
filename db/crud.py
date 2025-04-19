from pathlib import Path
import os
from datetime import datetime, timedelta

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy import create_engine, update, select, delete

from .models import Base, Company, Publication, Author, Moderator, Subscriber, Subscription
from .config import DB_PATH
from .exceptions import CompanyNotFound, UserNotFound


import asyncio

class Database:
    def __init__(self):
        self.db_name = 'sqlite+aiosqlite:///' + str(DB_PATH)
        self.engine = create_async_engine(self.db_name, echo=False)
        self.SessionLocal =  async_sessionmaker(bind=self.engine, expire_on_commit=False)


    async def init_db(self):
        db_file = self.db_name.split(':///')[-1]
        if not os.path.exists(db_file):
            async with self.engine.begin() as conn:
                await conn.run_sync(Base.metadata.create_all)


    async def add_subscriber(self, telegram_id: str):
        pass


    async def add_subscription(self, telegram_id: str, company_id: str):
        pass


    async def remove_subscription(self, telegram_id: str, company_id: str):
        subscriber =await self.get_subscriber(telegram_id)
        if subscriber is None:
            raise UserNotFound
        
        company = await self.get_company(company_id)
        if company is None:
            raise CompanyNotFound
        
        async with self.SessionLocal() as session:
            stmt = delete(Subscription).where(
                Subscription.subscriber_id.in_(
                    select(Subscriber.id)
                    .where(Subscriber.telegram_id == telegram_id)
                    .scalar_subquery()
                )
            )
            result = await session.execute(stmt)


    async def get_company(self, id: str) -> Company | None:
        async with self.SessionLocal() as session:
            stmt = select(Company).where(Company.id == id)
            result = await session.execute(stmt)
            return result.scalar()
        

    async def get_subscriber(self, id: str) -> Subscriber | None:
        async with self.SessionLocal() as session:
            stmt = select(Subscriber).where(Subscriber.id == id)
            result = await session.execute(stmt)
            return result.scalar()


db = Database()

asyncio.run(db.init_db())