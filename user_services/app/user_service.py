from datetime import timedelta

from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from user_services.app.user_repo import UserRepository
from user_services.app.user_schema import UserRegister, UserLogin, Token
from user_services.app.user_config import settings
from user_services.app.security import (
    hash_password,
    authenticate_user,
    create_access_token
)


class UserService:
    """
    Handles user registration, login and user-related business logic.
    """

    @staticmethod
    async def register_user(db: AsyncSession, user_data: UserRegister):
        # Check duplicate username
        existing_username = await UserRepository.get_user_by_username(db, user_data.username)
        if existing_username:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Username already exists"
            )

        # Check duplicate email
        existing_email = await UserRepository.get_user_by_email(db, user_data.email)
        if existing_email:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already exists"
            )

        hashed_password = hash_password(user_data.password)

        user = await UserRepository.create_user(
            db=db,
            name=user_data.name,
            username=user_data.username,
            dial_code=user_data.dial_code,
            phone_number=user_data.phone_number,
            email=user_data.email,
            password_hash=hashed_password,
            role="user"
        )
        return user

    @staticmethod
    async def login_user(db: AsyncSession, login_data: UserLogin) -> Token:
        user = await authenticate_user(db, login_data.username, login_data.password)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid username or password"
            )

        access_token_expires = timedelta(
            minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
        )

        access_token = create_access_token(
            data={
                "sub": user.username,
                "role": user.role,
                "user_id": user.id
            },
            expires_delta=access_token_expires
        )

        return Token(
            access_token=access_token,
            token_type="bearer",
            role=user.role,
            username=user.username
        )

    @staticmethod
    async def get_user_profile(user):
        return user
    
    @staticmethod
    async def get_all_user(db: AsyncSession):
        return await UserRepository.get_all_users(db)
        
    @staticmethod
    async def get_user_by_id(db: AsyncSession, user_id: int):
        return await UserRepository.get_user_by_id(db, user_id)
    
    @staticmethod
    async def get_user_by_username_or_email(db: AsyncSession, value: str):
        return await UserRepository.get_user_by_username_or_email(db, value)