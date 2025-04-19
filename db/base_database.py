from pathlib import Path
import os
from datetime import datetime, timedelta
from typing import List

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy import create_engine, update, select, delete

from .models import Base, Company, Publication, User, Subscriber, Subscription
from .config import CONTENT_AGREGATOR_DB 

from abc import ABC
from uuid import uuid4

import asyncio

class Database(ABC):
    def __init__(self):
        pass
    
    async def init_db(self):
        pass
    
    async def add_subscription(self, telegram_id: str, company_id: str) -> None:
        pass

    async def remove_subscription(self, telegram_id: str, company_id: str) -> None:
        pass

    async def get_user(self, id: str) -> User | None:
        pass

    async def get_company(self, id: str) -> Company | None:
        pass

    async def get_subscriber(self, id: str) -> Subscriber | None:
        pass
