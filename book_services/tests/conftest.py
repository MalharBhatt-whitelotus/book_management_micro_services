import pytest_asyncio
from httpx import AsyncClient, ASGITransport

from book_services.app.main import app


@pytest_asyncio.fixture(scope="function")
async def client():

    transport = ASGITransport(app=app)

    async with AsyncClient(
        transport=transport,
        base_url="http://book"
    ) as ac:
        yield ac