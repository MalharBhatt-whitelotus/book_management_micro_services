import httpx

from fastapi import HTTPException, status

class UserClient:
    API_CALL  = "http://127.0.0.1:8001/user"
    @staticmethod
    async def get_current_user(authorization: str):
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{UserClient.API_CALL}/me",headers={"Authorization": authorization})
            print(response.status_code)
            print(response.json())
            response.raise_for_status()
            return response.json()