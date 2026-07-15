import httpx
async def get_token():
    async with httpx.AsyncClient() as client:
        response = await client.post("http://localhost:8001/user/login", json={
        "username":"admin",
        "password":"admin123"
        })
        print(response.request.method)
        print(response.request.url)
        print(response.status_code)
        print(response.headers)
        print(response.text)    
        print(response.json())
        return response.json()["access_token"]