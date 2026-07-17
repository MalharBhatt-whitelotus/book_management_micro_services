from sqlalchemy.pool import NullPool
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession

from ai_based_knowledge_services.app.knowledge_config import settings

engine = create_async_engine(
    settings.DATABASE_URL,
    echo= True,
    pool_pin_ping=True,
    poolclass = NullPool
    )

AsyncSessionLocal = sessionmaker(
    autoflush=False, 
    autocommit=False, 
    bind=engine, 
    class_=AsyncSession,
    expire_on_commit=False
    )

Base = declarative_base()
print("=" * 80)
print("KNOWLEDGE DB URL:", settings.DATABASE_URL)
print("=" * 80)

async def get_db():
    db = AsyncSessionLocal()
    try:
        yield db
    finally:
        await db.close()