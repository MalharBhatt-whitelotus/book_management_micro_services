from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.pool import NullPool

from bill_services.app.bill_config import settings

# SQLite needs this connect arg for multithreaded FastAPI usage
engine = create_async_engine(
    settings.DATABASE_URL,
    echo=True,
    pool_pre_ping=True,
    poolclass=NullPool
)

AsyncSessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

Base = declarative_base()
print("=" * 80)
print("BILL DB URL:", settings.DATABASE_URL)
print("=" * 80)

async def get_db():
    """
    FastAPI dependency for database session
    """
    db = AsyncSessionLocal()
    try:
        yield db
    finally:
      await db.close()