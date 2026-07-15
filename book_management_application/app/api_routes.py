from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from book_services.app import main as book
from bill_services.app import main as bill
from user_services.app import main as user

templates = Jinja2Templates(directory="book_management_application/frontend/templates")
main_router = APIRouter(tags=["main"])

@main_router.get("/",response_class=HTMLResponse)
def main(request:Request):
    return templates.TemplateResponse(request=request, name="login_registration.html")

@main_router.post("/login", response_class=HTMLResponse)
def login()