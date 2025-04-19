from pathlib import Path
import os
from datetime import datetime, timedelta

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy import create_engine, update, and_
from sqlalchemy.future import select

from .models import Base, Company, Publication, Author, Moderator
from .config import DB_PATH

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



db = Database()

asyncio.run(db.init_db())