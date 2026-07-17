from sqlalchemy.orm import declarative_base
from sqlalchemy.ext.asyncio import create_async_engine, async_session
from sqlalchemy import NullPool

from knowledge_config import settings

engine = create_async_engine(settings.DATABASE_URL, 
                             )