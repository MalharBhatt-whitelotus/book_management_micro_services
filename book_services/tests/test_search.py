import pytest

from book_services.tests.get_token import get_token


@pytest.mark.asyncio
async def test_search_book(client):
    token = await get_token()

    response = await client.get(
        "/book/get?keyword=Python",
        headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code == 200

    books = response.json()

    assert isinstance(books, list)


@pytest.mark.asyncio
async def test_search_no_result(client):
    token = await get_token()

    response = await client.get(
        "/book/get?keyword=abcdefghijk",
        headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code == 200
    assert response.json() == []