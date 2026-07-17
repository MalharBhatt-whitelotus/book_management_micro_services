from pathlib import Path
from pydantic_settings import SettingsConfigDict, BaseSettings

BASE_DIR = Path(__file__).resolve().parent.parent

class KnowledgeConfig(BaseSettings):
