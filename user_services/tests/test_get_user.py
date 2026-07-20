import pytest

from user_services.tests.get_token import get_token

@pytest.mark.asyncio
async def test_get_user(client):
    token = await get_token()
    response = await client.get("/user/me", headers = {"Authorization": f"bearer {token}"})

    assert response.status_code == 200

@pytest.mark.asyncio
async def test_get_user_by_id(client):
    token = await get_token()
    response = await client.get("/user/get_user_by_id/1",headers= {"Authorization" : f"bearer {token}"})
    
    assert response.status_code == 200

@pytest.mark.asyncio
async def test_get_all_user(client):
    token = await get_token()
    response = await client.get("/user/get_all", headers={"Authorization": f"bearer {token}"})

    assert response.status_code == 200

@pytest.mark.asyncio
async def test_get_user_by_username_or_email(client):
    token = await get_token()
    response = await client.get("/user/get_user_by_username_or_email/mal",headers = {"Authorization": f"bearer {token}"})

    assert response.status_code == 200