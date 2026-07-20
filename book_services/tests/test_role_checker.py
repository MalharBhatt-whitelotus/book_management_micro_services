import pytest
import random

from book_services.tests.get_token import get_non_admin_token

@pytest.mark.asyncio
async def test_role_checker(client):
    token = await get_non_admin_token()
    payload = {
        "title":f"Book {random.randint(1,1000)}",
        "author":"Someone",
        "category":"Programming",
        "price":450,
        "quantity":10,
        "description":"Testing",
        "book_type":"hardcopy"
    }
    response = await client.post("/book/create",json = payload, headers= {"Authorization": f"bearer {token}"})
    print(response.json())
    assert response.status_code == 403