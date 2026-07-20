import pytest
import httpx
from bill_services.tests.get_token import get_token
@pytest.mark.asyncio
async def test_checkout(client, external_client):
    token = await get_token()       
    id_reponse = await external_client.get("/book/get_book_id", headers={"Authorization": f"bearer {token}"})
    assert id_reponse.status_code == 200
    book_id = id_reponse.json()
    payload = {"items":[{"book_id": book_id, "quantity": 1}]}
    response = await client.post("/bill/checkout",json=payload, headers={"Authorization": f"bearer {token}"})
    assert response.status_code == 201
    result = response.json()
    assert result["total_amount"]> 0    

@pytest.mark.asyncio
async def test_book_bot_found_checkout(client):
    token = await get_token()
    payload = {"items":[{"book_id": 999999, "quantity": 1}]}
    response = await client.post("/bill/checkout",json=payload,headers={"Authorization":f"bearer {token}"})
    assert response.status_code == 404

@pytest.mark.asyncio
async def test_book_insufficient_checkout(client, external_client):
    token = await get_token()
    id_response = await external_client.get("/book/get_book_id", headers = {"Authorization": f"bearer {token}"})
    book_id = id_response.json()
    payload = {"items":[{"book_id": book_id, "quantity": 1000}]}
    response = await client.post("/bill/checkout",json=payload,headers={"Authorization":f"bearer {token}"})
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