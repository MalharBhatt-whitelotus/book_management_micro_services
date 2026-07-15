import pytest_asyncio
from httpx import AsyncClient, ASGITransport

from book_services.app.main import app

@pytest_asyncio.fixture
async def client():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://book") as ac:
        yield ac