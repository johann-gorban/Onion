from enternal.services.models.domains import Publication, User
from enternal.storages.sqlalchemy_db import db

async def get_post_by_id(post_id: str) -> Publication | None:
    return await db.get_publication(post_id)


async def get_posts_by_author(author: "User") -> list["Publication"]:
    """Получение публикаций конкретного автора"""


async def create_post(publication_data: "Publication") -> "Publication":
    """Создание новой публикации"""


async def update_post(post_id: str, update_data: dict) -> "Publication":
    """Обновление существующей публикации"""


async def delete_post(post_id: str) -> bool:
    """Удаление публикации"""


async def search_posts(query: str) -> list["Publication"]:
    """Поиск публикаций по текстовому запросу"""
