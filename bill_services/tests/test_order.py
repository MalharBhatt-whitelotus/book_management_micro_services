import pytest

from bill_services.tests.get_token import get_token

@pytest.mark.asyncio
async def test_order_summary(client):
    token = await get_token()
    response = await client.get("/bill/order/ORD-4F705D579D",headers={"Authorization":f"bearer {token}"})
    assert response.status_code == 200

@pytest.mark.asyncio
async def test_invalid_order_summary(client):
    token = await get_token()
    response = await client.get("/bill/order/mynameistester",headers={"Authorization":f"bearer {token}"})
    assert response.status_code == 404