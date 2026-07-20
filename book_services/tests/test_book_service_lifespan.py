import pytest
from asgi_lifespan import LifespanManager
from httpx import AsyncClient, ASGITransport

from book_services.app.main import app

@pytest.mark.asyncio
async def test_book_service_lifespan():
    async with LifespanManager(app):
        async with AsyncClient(
            transport=ASGITransport(app=app),
            base_url = "http://test"
        ) as client:
            response = await client.get("/health")
            assert response.status_code == 200