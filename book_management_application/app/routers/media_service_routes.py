from fastapi import APIRouter, Request

from book_management_application.app.config import settings
from book_management_application.app.proxy import forward_request

media_routes = APIRouter(tags=["media_gateway"])

@media_routes.api_route(
    "/media/{path:path}",
    methods=["GET", "POST", "PUT", "DELETE"]
)
async def media_gateway(path: str, request: Request):
    return await forward_request(request, f"{settings.MEDIA_SERVICE}/media/{path}")