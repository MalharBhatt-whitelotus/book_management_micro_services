import random
import pytest
from book_services.tests.get_token import get_token

@pytest.mark.asyncio
async def test_create_book(client): 
    token = await get_token()
    payload = {
        "title":f"Book {random.randint(1,1000)}",
        "author":"Someone",
        "category":"Programming",
        "price":450,
        "quantity":10,
        "description":"Testing",
        "book_type":"hardcopy"
    }

    response = await client.post(f"/book/create", json=payload, headers={"Authorization":f"bearer {token}"})
    assert response.status_code == 201
    result = response.json()
    assert isinstance(result, dict)