import httpx
from fastapi import HTTPException,status

class UserClient:
    API_URL = "http://127.0.0.1:8003/user"

    async def get_current_user():
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{UserClient.API_URL}/me")
            print(response.status_code)
            print(response.json())
            if response.status_code != 200:
                raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="current user not found.")
            return response.json()