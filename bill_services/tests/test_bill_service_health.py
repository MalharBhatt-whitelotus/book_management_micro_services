import pytest

from bill_services.app.bill_config import settings
from bill_services.tests.get_token import get_token

@pytest.mark.asyncio
async def test_bill_service_health(client):
    token = await get_token()
    response = await client.get("/health",headers={"Authorization": f"bearer {token}"})

    assert response.status_code == 200

    assert response.json() == {
        "status": "ok",
        "app": settings.APP_NAME,
        "version": settings.APP_VERSION
    }