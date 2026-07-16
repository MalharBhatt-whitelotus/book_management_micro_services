import pytest
from book_services.tests.get_token import get_token
@pytest.mark.asyncio
async def test_get_books(client):
    token = await get_token()
    response = await client.get("/book/get", headers= {"Authorization":f"bearer {token}"})
    assert response.status_code == 200
    books = response.json()
    assert isinstance(books,list)

@pytest.mark.asyncio
async def test_get_books_by_keyword(client):
    token = await get_token()
    response = await client.get("/book/get?/keyword=someone",headers={"Authorization":f"bearer {token}"})
    assert response.status_code == 200
    books = response.json()
    assert isinstance(books,list)

@pytest.mark.asyncio
async def test_get_book_by_id(client):
    token = await get_token()

    response = await client.get(
        f"/book/get_book_by_id/21",
        headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code == 200

    book = response.json()

    assert book["id"] == 21

@pytest.mark.asyncio
async def test_get_book_by_invalid_id(client):
    token = await get_token()

    response = await client.get(
        f"/book/get_book_by_id/999999",
        headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code == 404


@pytest.mark.asyncio
async def test_get_invalid_book(client):
    token = await get_token()

    response = await client.get(
        "/book/get/999999",
        headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code == 404

@pytest.mark.asyncio
async def test_available_books(client):
    token = await get_token()

    response = await client.get(
        "/book/get_available",
        headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code == 200

    books = response.json()

    for book in books:
        assert book["quantity"] > 0