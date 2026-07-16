import asyncio
from datetime import datetime

from passlib.context import CryptContext
from sqlalchemy import select
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from user_services.app.user_config import settings
from user_services.app.user_model import User

# Password hashing
pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)

# Database engine
engine = create_async_engine(
    settings.DATABASE_URL,
    echo=False
)

SessionLocal = async_sessionmaker(
    bind=engine,
    expire_on_commit=False
)


async def create_admin():
    async with SessionLocal() as session:

        # Check if admin already exists
        existing_admin = await session.scalar(
            select(User).where(User.username == "admin")
        )

        if existing_admin:
            print("Admin user already exists.")
            return

        admin = User(
            name="Administrator",
            username="admin",
            email="admin@gmail.com",
            password_hash=pwd_context.hash("admin123"),
            role="admin",
            created_at=datetime.utcnow(),
            dial_code = 91,
            phone_number= 1234567890
        )

        session.add(admin)
        await session.commit()

        print("✅ Admin user inserted successfully.")


if __name__ == "__main__":
    asyncio.run(create_admin())