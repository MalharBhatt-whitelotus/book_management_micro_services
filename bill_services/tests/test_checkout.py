import pytest

from bill_services.tests.get_token import get_token

@pytest.mark.asyncio
async def test_checkout(client):
    token = await get_token()
    payload = {"items":[{"book_id": 3, "quantity": 1}]}
    response = await client.post("/bill/checkout",json=payload, headers={"Authorization": f"bearer {token}"})
    print("Status:", response.status_code)
    print("Response:", response.text)
    assert response.status_code == 201
    result = response.json()
    assert result["total_amount"]> 0    