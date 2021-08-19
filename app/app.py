import aioredis
from fastapi import Depends, FastAPI
from fastapi.requests import Request
from fastapi.responses import JSONResponse

from .routes import router

REDIS_URL = 'redis://localhost'
REDIS_DB = 0
REDIS_PASS = 'RedisPassword'


def create_app(redis=None):
    """
    redis: Redis instance / coroutine
    """

    app = FastAPI()

    app.include_router(router)

    @app.on_event('startup')
    async def startup():
        nonlocal redis

        if redis is None:
            # if redis is None, create the instance on start up
            redis = await aioredis.from_url(
                REDIS_URL, db=REDIS_DB, password=REDIS_PASS
            )
        assert await redis.ping()

    @app.middleware('http')
    async def http_middleware(request: Request, call_next):
        nonlocal redis

        # Initial response when exception raised on 
        #  `call_next` function
        err = {'error': True, 'message': "Internal server error"},
        response = JSONResponse(err, status_code=500)
        
        try:
            request.state.redis = redis
            response = await call_next(request)
        finally:
            return response

    return app
