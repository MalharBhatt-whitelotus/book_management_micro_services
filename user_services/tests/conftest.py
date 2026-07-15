import pytest_asyncio
from httpx import AsyncClient, ASGITransport

from user_services.app.main import app

@pytest_asyncio.fixture
async def client():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://user") as ac:
        yield ac