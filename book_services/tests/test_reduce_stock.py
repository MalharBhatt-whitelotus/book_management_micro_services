import pytest

from book_services.tests.get_token import get_token

@pytest.mark.asyncio
async def test_reduce_stock_quantity(client):
    token = await get_token()
    id = await client.get("/book/get_book_id", headers={"Authorization": f"bearer {token}"})
    response = await client.patch(f"/book/reduce_book_stock?book_id={id.json()}&quantity=1",
                                  headers={"Authorization": f"bearer {token}"})
    assert response.status_code == 200

@pytest.mark.asyncio
async def test_reduce_stock_invalid_quantity(client):
    token = await get_token()

    response = await client.patch(
        "/book/reduce_book_stock?book_id=21&quantity=-1",
        headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code == 422


@pytest.mark.asyncio
async def test_reduce_stock_invalid_book(client):
    token = await get_token()

    response = await client.patch(
        "/book/reduce_book_stock?book_id=999999&quantity=1",
        headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code == 404