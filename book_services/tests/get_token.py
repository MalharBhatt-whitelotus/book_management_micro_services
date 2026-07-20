import httpx
async def get_token():
    async with httpx.AsyncClient() as client:
        response = await client.post("http://localhost:8001/user/login", json={
        "username": "admin",
        "password": "admin123"
        })
        return response.json()["access_token"]
    
async def get_non_admin_token():
    async with httpx.AsyncClient() as client:
        response = await client.post("http://localhost:8001/user/login", json = {
            "username": "mal",
            "password": "mal123"
        })
        return response.json()["access_token"]