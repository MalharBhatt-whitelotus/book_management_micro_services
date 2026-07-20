from fastapi import FastAPI
from contextlib import asynccontextmanager

from book_management_application.app.service_manager import ServiceManager
from book_management_application.app.routers.view_router import view_routes
from book_management_application.app.routers.user_service_routes import user_routes
from book_management_application.app.routers.book_service_routes import book_routes
from book_management_application.app.routers.bill_service_routes import bill_routes
from book_management_application.app.routers.file_service_routes import file_routes

manager = ServiceManager()

@asynccontextmanager
async def lifespan(app : FastAPI):
    manager.start_service("user","user_services.app.main",8001)
    manager.start_service("book","book_services.app.main",8002)
    manager.start_service("bill","bill_services.app.main",8003)
    manager.start_service("file","file_services.app.main",8004)

    print("ALL SERVICES STARTED ...")
    manager.start_monitor()

    yield
    print("STOPPING SERVICES ...")
    manager.stop_all()

app = FastAPI(title="API Gateway", lifespan=lifespan)

app.include_router(view_routes)
app.include_router(user_routes)
app.include_router(book_routes)
app.include_router(bill_routes)
app.include_router(file_routes)