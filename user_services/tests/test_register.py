import pytest
import random

@pytest.mark.asyncio
async def test_register(client):
    number = random.randint(1,100000)
    payload = {
        "name": "test User",
        "username": f"testU{number}",
        "email": f"User{number}@gmail.com",
        "password": "password123"
        }
    
    response = await client.post("/user/registration", json=payload)
    assert response.status_code == 201