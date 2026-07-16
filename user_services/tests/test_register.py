import pytest
import random

number = random.randint(1,100000)

@pytest.mark.asyncio
async def test_register(client):
    payload = {
        "name": "test User",
        "username": f"testU{number}",
        "dial_code": "+91",
        "phone_number": "1237894560",
        "email": f"User{number}@gmail.com",
        "password": "password123"
        }
    
    response = await client.post("/user/registration", json=payload)
    assert response.status_code == 201

@pytest.mark.asyncio
async def test_username_already_exists_registration(client):
    payload = {
        "name":"test User",
       "username": f"testU{number}",
        "dial_code": "+91",
        "phone_number": "1237894560",
        "email": f"User{number+1}@gmail.com",
        "password": "password123"
    }
    response = await client.post("/user/registration", json=payload)
    assert response.status_code == 400

@pytest.mark.asyncio
async def test_email_already_exists_registration(client):
    payload = {
        "name":"test User",
       "username": f"testU{number+1}",
        "dial_code": "+91",
        "phone_number": "1237894560",
        "email": f"User{number}@gmail.com",
        "password": "password123"
    }
    response = await client.post("/user/registration", json=payload)
    assert response.status_code == 400