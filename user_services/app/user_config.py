from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).resolve().parent.parent

class UserSettings(BaseSettings):
    APP_NAME: str = "Book Management System"
    APP_VERSION: str = "1.0.0"

    DATABASE_URL: str

    SECRET_KEY: str = "super-secret-key-change-me"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24

    ADMIN_DEFAULT_USERNAME: str = "admin"
    ADMIN_DEFAULT_EMAIL: str = "admin@example.com"
    ADMIN_DEFAULT_PASSWORD: str = "admin123"

    model_config = SettingsConfigDict(
        env_file=BASE_DIR / ".env",
        extra="ignore",
    )

settings = UserSettings()