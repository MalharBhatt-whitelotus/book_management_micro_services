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