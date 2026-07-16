import pytest_asyncio
from httpx import AsyncClient, ASGITransport

from bill_services.app.main import app


@pytest_asyncio.fixture(scope="function")
async def client():

    transport = ASGITransport(app=app)

    async with AsyncClient(
        transport=transport,
        base_url="http://bill"
    ) as ac:
        yield ac