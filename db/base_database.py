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
    
    async def init_db(self) -> None: pass
    
    async def get_publication(self, publication_id: str) -> Publication | None:
        pass

    async def get_publications(self) -> List[Publication]: 
        pass

    async def remove_publication(self, publication_id: str) -> None: 
        pass

    async def add_publication(
            self, 
            title: str, 
            content: str, 
            image_url: str, 
            created_at: datetime, 
            author_id: str
            ) -> None: 
        pass

    async def update_publication(
            self, 
            publication_id: str, 
            title: str, 
            content: str, 
            image_url: str, 
            created_at: datetime, 
            author_id: str
            ) -> None: 
        pass
    
    async def get_company(self, id: str) -> Company | None: 
        pass

    async def get_companies(self) -> List[Company]: 
        pass
    
    async def get_user_by_id(self, id: str) -> User | None: 
        pass

    async def get_user_by_login(self, login: str) -> User | None: 
        pass

    async def get_users(self) -> List[User]: 
        pass

    async def add_user(
            self, 
            login: str, 
            password: str, 
            role: str, 
            company_id: str | None
            ) -> None: 
        pass

    async def remove_user(self, id: str) -> None: 
        pass
