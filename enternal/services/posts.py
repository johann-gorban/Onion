from typing import Optional

from enternal.services.models.domains import Publication, User


async def get_post_by_id(post: Publication) -> Optional["Publication"]:
    """Получение публикации по ID"""


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
