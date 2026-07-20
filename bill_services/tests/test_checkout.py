import pytest

from bill_services.tests.get_token import get_token

@pytest.mark.asyncio
async def test_checkout(client):
    token = await get_token()
    payload = {"items":[{"book_id": 4, "quantity": 1}]}
    response = await client.post("/bill/checkout",json=payload, headers={"Authorization": f"bearer {token}"})
    # print("Status:", response.status_code)
    # print("Response:", response.text)
    assert response.status_code == 201
    result = response.json()
    assert result["total_amount"]> 0    

@pytest.mark.asyncio
async def test_book_bot_found_checkout(client):
    token = await get_token()
    payload = {"items":[{"book_id": 999999, "quantity": 1}]}
    response = await client.post("/bill/checkout",json=payload,headers={"Authorization":f"bearer {token}"})
    print(response.status_code)
    print(response.json())
    assert response.status_code == 404

@pytest.mark.asyncio
async def test_book_insufficient_checkout(client):
    token = await get_token()
    payload = {"items":[{"book_id": 1, "quantity": 1000}]}
    response = await client.post("/bill/checkout",json=payload,headers={"Authorization":f"bearer {token}"})
    print(response.status_code)
    print(response.text)
    print(response.json())
    assert response.status_code == 400

from unittest.mock import AsyncMock, patch

@pytest.mark.asyncio
async def test_checkout_internal_error(client):
    token = await get_token()
    payload = {"items": [{"book_id": 1,"quantity": 1}]}
    with patch(
        "bill_services.app.service.bill_service.BookClient.get_book_by_id",
        new=AsyncMock(side_effect=Exception("Database crashed"))
    ):
        response = await client.post(
            "/bill/checkout",
            json=payload,
            headers={"Authorization": f"Bearer {token}"}
        )

    assert response.status_code == 500
    assert response.json()["detail"] == "Checkout failed: Database crashed"