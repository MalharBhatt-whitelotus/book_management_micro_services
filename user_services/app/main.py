from fastapi import FastAPI
from contextlib import asynccontextmanager

from user_services.app.user_config import settings
from user_services.app.user_routes import user_router
from user_services.app.user_database import Base,engine

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    await engine.dispose()

app = FastAPI(lifespan=lifespan,
    title=settings.APP_NAME,
    version=settings.APP_VERSION
)


@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "app": settings.APP_NAME,
        "version": settings.APP_VERSION
    }


app.include_router(user_router)