import pytest

from book_services.tests.get_token import get_token


@pytest.mark.asyncio
async def test_update_book(client):
    token = await get_token()

    response = await client.put(
        "/book/update/21",
        json={
        "title": "Book21",
        "author": "Someone21",
        "category": "Programming",
        "price": 450,
        "quantity": 5,
        "description": "Testing",
        "book_type": "softcopy"
    },
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200

@pytest.mark.asyncio
async def test_update_invalid_quantity(client):
    token = await get_token()

    response = await client.put(
        "/book/update/21",
        json={"quantity": -1},
        headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code == 422

@pytest.mark.asyncio
async def test_update_invalid_price(client):
    token = await get_token()

    response = await client.put(
        "/book/update/21",
        json={"price": 0},
        headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code == 422


@pytest.mark.asyncio
async def test_update_invalid_book(client):
    token = await get_token()

    response = await client.put(
        "/book/update/999999",
        json={"price": 100},
        headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code == 404