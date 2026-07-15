import httpx
from fastapi import Request
from fastapi.responses import JSONResponse

async def forward_request(
    request: Request,
    service_url: str,
):
    async with httpx.AsyncClient() as client:

        body = await request.body()

        response = await client.request(
            method=request.method,
            url=service_url,
            params=request.query_params,
            headers={
                k: v
                for k, v in request.headers.items()
                if k.lower() != "host"
            },
            content=body,
        )

        return JSONResponse(
            status_code=response.status_code,
            content=response.json(),
        )