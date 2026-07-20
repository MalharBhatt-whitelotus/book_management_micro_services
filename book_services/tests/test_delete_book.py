import pytest

from book_services.tests.get_token import get_token

@pytest.mark.asyncio
async def test_delete_book(client):
    token  = await get_token()
    id = await client.get("/book/get_book_id", headers = {"Authorization": f"bearer {token}"})
    response = await client.delete(f"/book/delete/{id.json()}", headers = {"Authorization": f"bearer {token}"})
    print(id)
    print(id.json())
    print(response.json())
    print(response.status_code)
    assert response.status_code == 200

@pytest.mark.asyncio
async def test_delete_invalid_book(client):
    token = await get_token()

    response = await client.delete(
        "/book/delete/999999",
        headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code == 404