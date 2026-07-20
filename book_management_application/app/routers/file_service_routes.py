from fastapi import APIRouter, Request

from book_management_application.app.config import settings
from book_management_application.app.proxy import forward_request

file_routes = APIRouter(tags=["file_gateway"])

@file_routes.api_route(
    "/file/{path:path}",
    methods=["GET", "POST", "PUT", "DELETE"]
)
async def file_gateway(path: str, request: Request):
    return await forward_request(request, f"{settings.FILE_SERVICE}/file/{path}")