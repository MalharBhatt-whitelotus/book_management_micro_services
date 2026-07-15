import pytest
import random

from book_services.tests.get_token import get_token


@pytest.mark.asyncio
async def test_create_book_negative_quantity(client):
    token = await get_token()

    payload = {
        "title": f"Book {random.randint(1,1000)}",
        "author": "Someone",
        "category": "Programming",
        "price": 450,
        "quantity": -5,
        "description": "Testing",
        "book_type": "hardcopy"
    }

    response = await client.post(
        "/book/create",
        json=payload,
        headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code == 422
    detail = response.json()["detail"]
    assert detail[0]["loc"] == ["body", "quantity"]
    assert detail[0]["type"] == "greater_than_equal"

@pytest.mark.asyncio
async def test_create_book_invalid_price(client):
    token = await get_token()

    payload = {
        "title": f"Book {random.randint(1,1000)}",
        "author": "Someone",
        "category": "Programming",
        "price": 0,
        "quantity": 10,
        "description": "Testing",
        "book_type": "hardcopy"
    }

    response = await client.post(
        "/book/create",
        json=payload,
        headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code == 422
    detail =  response.json()["detail"]
    assert detail[0]["loc"] == ["body","price"]
    assert detail[0]["type"] ==  "greater_than"