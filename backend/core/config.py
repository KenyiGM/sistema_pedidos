from pydantic import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "Sistema de Pedidos"
    VERSION: str = "1.0.0"
    DATABASE_URL: str
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    class Config: 
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()