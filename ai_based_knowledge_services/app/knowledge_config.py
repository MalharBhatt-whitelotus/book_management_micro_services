from pathlib import Path
from pydantic_settings import SettingsConfigDict, BaseSettings

BASE_DIR = Path(__file__).resolve().parent.parent

class KnowledgeSettings(BaseSettings):
    APP_NAME: str = "Book Management System"
    APP_VERSION: str = "1.0.0"
    
    DATABASE_URL: str

    SECRET_KEY: str = "super-secret-key-change-me"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRES_MINUTES: int = 5

    ADMIN_DEFAULT_USERNAME: str = "admin"
    ADMIN_DEFAULT_EMAIL: str = "admin@example.com"
    ADMIN_DEFAULT_PASSWORD: str = "admin123"

    model_config = SettingsConfigDict(
        env_file=BASE_DIR / ".env",
        extra = "ignore"
        )

settings = KnowledgeSettings()