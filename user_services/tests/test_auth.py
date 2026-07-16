import pytest

@pytest.mark.asyncio
async def test_login(client):
    payload ={
        "username": "admin",
        "password": "admin123"
    }

    response = await client.post("/user/login", json=payload)
    assert response.status_code == 200
    body = response.json()  
    assert "access_token" in body   

@pytest.mark.asyncio
async def test_invalid_login(client):
    payload ={
        "username": "admin1",
        "password": "admin1234"
    }

    response = await client.post("/user/login", json=payload)
    assert response.status_code == 401