from fastapi import FastAPI
from contextlib import asynccontextmanager

from bill_services.app.bill_config import settings
from bill_services.app.bill_routes import bill_router
from bill_services.app.bill_database import Base,engine

"""

port ==== 8001


"""

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


app.include_router(bill_router)