from fastapi import APIRouter,Request

from book_management_application.app.config import settings
from book_management_application.app.proxy import forward_request

bill_routes = APIRouter(tags=["bill_gateway"])
@bill_routes.api_route(
    "/bill/{path:path}",
    methods=["GET", "POST", "PUT", "DELETE"]
)
async def bill_gateway(path: str, request: Request):

    return await forward_request(
        request,
        f"{settings.BILL_SERVICE}/bill/{path}"
    )