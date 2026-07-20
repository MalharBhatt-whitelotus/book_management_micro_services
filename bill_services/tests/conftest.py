import pytest_asyncio
from httpx import AsyncClient, ASGITransport

from bill_services.app.main import app
from book_services.app.main import app as book_app

@pytest_asyncio.fixture(scope="function")
async def client():

    transport = ASGITransport(app=app)

    async with AsyncClient(
        transport=transport,
        base_url="http://bill"
    ) as ac:
        yield ac

@pytest_asyncio.fixture(scope="function")
async def external_client():

    transport = ASGITransport(app=book_app)

    async with AsyncClient(transport=transport,
                           base_url="http://book") as bsc:
        yield bsc