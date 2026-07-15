from fastapi import FastAPI
from book_management_application.app.api_routes import main_router
app = FastAPI()
app.include_router(main_router)