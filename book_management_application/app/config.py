from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    USER_SERVICE: str
    BOOK_SERVICE: str
    BILL_SERVICE: str
    FILE_SERVICE: str

    class Config:
        env_file = "book_management_application/.env"

settings = Settings()