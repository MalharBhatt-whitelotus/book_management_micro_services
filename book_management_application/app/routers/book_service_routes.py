from fastapi import APIRouter,Request

from book_management_application.app.config import settings
from book_management_application.app.proxy import forward_request

book_routes = APIRouter(tags=["book_gateway"])
@book_routes.api_route(
    "/book/{path:path}",
    methods=["GET", "POST", "PUT", "DELETE"]
)
async def book_gateway(path: str, request: Request):

    return await forward_request(
        request,
        f"{settings.BOOK_SERVICE}/book/{path}"
    )