from fastapi import APIRouter
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="./book_management_application/frontend/templates")
view_routes = APIRouter(tags=["view_html"])

@view_routes.get("/",response_class=HTMLResponse)
def main(request:Request):
    return templates.TemplateResponse(request=request, name="login_registration.html")

@view_routes.get("/admin",response_class=HTMLResponse)
def admin_dashboard(request:Request):
    return templates.TemplateResponse(request=request, name="admin_dashboard.html")

@view_routes.get("/dashboard",response_class=HTMLResponse)
def user_dashboard(request:Request):
    return templates.TemplateResponse(request=request, name="user_dashboard.html")