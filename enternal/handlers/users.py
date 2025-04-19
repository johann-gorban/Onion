from fastapi import APIRouter
from services.domains import User

user_router = APIRouter(tags=['Users'])

@user_router.get('/user/')
async def get_user_info(user: User):
    return {
        'id': user.id,
        'login': user.login,
        'password_hashed': user.password_hash
    }


@user_router.get('/users')
async def get_users_info():
    pass
