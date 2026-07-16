import pytest

from book_services.tests.get_token import get_token


@pytest.mark.asyncio
async def test_delete_invalid_book(client):
    token = await get_token()

    response = await client.delete(
        "/book/delete/999999",
        headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code == 404