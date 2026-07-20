import httpx
from fastapi import HTTPException

class BookClient:
    API_URL = "http://127.0.0.1:8002/book"
    @staticmethod
    async def get_book_by_id(book_id: int):
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{BookClient.API_URL}/get_book_by_id/{book_id}")
            # print(response.status_code)
            # print(response.json())
            if response.status_code != 200:
                raise HTTPException(status_code=404,detail="BOOK NOT FOUND.")
            return response.json()
    
    @staticmethod
    async def reduce_book_stock(book_id: int, quantity: int):
        async with httpx.AsyncClient() as client:
            response = await client.patch(f"{BookClient.API_URL}/reduce_book_stock",params={"book_id":book_id,"quantity":quantity})
            # print(response.request.method)
            # print(response.request.url)
            # print(response.status_code)
            # print(response.headers)
            # print(response.text)    
            # print(response.json())
            # if response.status_code != 200:
            #     raise HTTPException(status_code=409,detail="Books are not reduced.")
            return response.json()