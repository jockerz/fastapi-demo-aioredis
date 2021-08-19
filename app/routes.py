from fastapi import APIRouter, Depends

from app.deps import get_redis

router = APIRouter()


@router.post('/post')
async def save_key_value(
    key: str, value: str, redis=Depends(get_redis)
):
    await redis.set(key, value)
    return {'success': True, 'data': {key: value}}


@router.get('/get')
async def get_value(key: str, redis=Depends(get_redis)):
    value = await redis.get(key)
    return {
        'success': True if value else False,
        'data': {key: value}
    }
