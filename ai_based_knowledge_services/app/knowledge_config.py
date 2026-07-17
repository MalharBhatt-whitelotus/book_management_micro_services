from pathlib import Path
from pydantic_settings import SettingsConfigDict, BaseSettings

BASE_DIR = Path(__file__).resolve().parent.parent

class KnowledgeSettings(BaseSettings):
    APP_NAME: str
    APP_VERSION: str
    
    DATABASE_URL: str
    UPLOADS_DIR: str

    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRES_MINUTES: int

    GEMINI_AI_KEY: str

    model_config = SettingsConfigDict(
        env_file=BASE_DIR / ".env",
        extra = "ignore"
        )

settings = KnowledgeSettings()