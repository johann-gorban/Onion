from fastapi import APIRouter
from fastapi.responses import JSONResponse
from services.domains import Publication
from services.posts import get_posts, get_post_by_id, create_post, update_post, delete_post

post_router = APIRouter()

@post_router.get('/posts/')
async def handler_get_all_posts() -> JSONResponse:
    result = await get_posts()
    return JSONResponse(result)


@post_router.get('/post_by_id/')
async def handler_get_post_by_id(post: Publication) -> JSONResponse:
    result = await get_post_by_id(post.id)
    return JSONResponse(result)


@post_router.post('/posts/create')
async def handler_create_post(post: Publication) -> None:
    await create_post(post)


@post_router.patch('/posts/update')
async def update_post(post: Publication) -> None:
    await update_post(post)


@post_router.delete('/posts/delete')
async def delete_post(post: Publication) -> None:
    await delete_post(post)
