from fastapi import APIRouter
from fastapi.responses import JSONResponse

from services.domains import User
from services.users import (
    get_user_info_by_id,
    get_user_info_by_login,
    get_users_unfo,
    delete_user,
    add_user
)


user_router = APIRouter(tags=['Users'])

@user_router.get('/user')
async def handler_get_user_info(user: User) -> JSONResponse:
    if user.id is not None:
        result = await get_user_info_by_id(user.id)
    else:
        result = await get_user_info_by_login(user.login)
    return JSONResponse(result)


@user_router.get('/users')
async def handler_get_users_info() -> JSONResponse:
    result = await get_users_unfo()
    return JSONResponse(result)


@user_router.post('/user/create')
async def handler_create_user(user: User) -> None:
    await add_user(user)


@user_router.delete('/user/delete')
async def handler_delete_user(user: User) -> None:
    await delete_user(user.id)
