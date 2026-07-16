import httpx
from fastapi import FastAPI
# from fastapi import Request
# from fastapi.responses import HTMLResponse
# from fastapi.templating import Jinja2Templates
from book_management_application.app.proxy import forward_request
from book_management_application.app.routers.view_router import view_routes
from book_management_application.app.routers.user_service_routes import user_routes
from book_management_application.app.routers.book_service_routes import book_routes
from book_management_application.app.routers.bill_service_routes import bill_routes
from book_management_application.app.config import settings

app = FastAPI(title="API Gateway")

app.include_router(view_routes)
app.include_router(user_routes)
app.include_router(book_routes)
app.include_router(bill_routes)

# templates = Jinja2Templates(directory="./book_management_application/frontend/templates")

# @app.get("/",response_class=HTMLResponse)
# def main(request:Request):
#     return templates.TemplateResponse(request=request, name="login_registration.html")

# @app.get("/admin",response_class=HTMLResponse)
# def admin_dashboard(request:Request):
#     return templates.TemplateResponse(request=request, name="admin_dashboard.html")

# @app.post("/login")
# async def login(request: Request):

#     data = await request.json()

#     async with httpx.AsyncClient() as client:

#         response = await client.post(
#             f"{settings.USER_SERVICE}/user/login",
#             json=data
#         )

#     return response.json()

# @app.post("/registration")
# async def registration(request: Request):

#     data = await request.json()

#     async with httpx.AsyncClient() as client:

#         response = await client.post(
#             f"{settings.USER_SERVICE}/user/registration",
#             json=data
#         )
#         print(response.status_code)
#         print(response.json())
#     return response.json()

# @app.get("/books")
# async def books():

#     async with httpx.AsyncClient() as client:

#         response = await client.get(
#             f"{settings.BOOK_SERVICE}/book/get"
#         )

#     return response.json()

# @app.post("/books")
# async def books():

#     async with httpx.AsyncClient() as client:

#         response = await client.post(
#             f"{settings.BOOK_SERVICE}/book/"
#         )

#     return response.json()

# @app.post("/checkout")
# async def checkout(request: Request):

#     body = await request.json()

#     async with httpx.AsyncClient() as client:

#         response = await client.post(
#             f"{settings.BILL_SERVICE}/checkout",
#             json=body
#         )

#     return response.json()