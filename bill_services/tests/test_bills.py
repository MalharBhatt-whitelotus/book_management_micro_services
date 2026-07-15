import pytest

from bill_services.tests.get_token import get_token

@pytest.mark.asyncio
async def test_bills(client):
    token = await get_token()
    response = await client.get("/bill/",headers={"Authorization":f"bearer {token}"})
    assert response.status_code == 200