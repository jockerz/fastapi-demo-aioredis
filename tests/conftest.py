import pytest
from fakeredis import aioredis
from httpx import AsyncClient

from app.app import create_app


@pytest.fixture
async def redis():
    print(dir(aioredis))
    return aioredis.FakeRedis(encoding='utf-8')


@pytest.fixture
def app(redis):
    app = create_app(redis=redis)
    return app


@pytest.fixture
def http_client(app):
    return AsyncClient(app=app, base_url='http://test')
