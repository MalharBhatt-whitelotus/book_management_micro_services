from fastapi import APIRouter,Request

from book_management_application.app.config import settings
from book_management_application.app.proxy import forward_request

user_routes = APIRouter(tags=["user_gateway"])
@user_routes.api_route(
    "/user/{path:path}",
    methods=["GET", "POST", "PUT", "DELETE"]
)
async def user_gateway(path: str, request: Request):

    return await forward_request(
        request,
        f"{settings.USER_SERVICE}/user/{path}"
    )