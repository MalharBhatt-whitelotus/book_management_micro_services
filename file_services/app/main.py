from fastapi import FastAPI

from file_services.app.file_routes import router

app = FastAPI()
app.include_router(router)