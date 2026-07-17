from fastapi import FastAPI

from ai_based_knowledge_services.app.knowledge_routes import router

app = FastAPI()
app.include_router(router)