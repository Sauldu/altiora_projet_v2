# app/gateway/config.py
from pydantic import BaseSettings, SecretStr

class Settings(BaseSettings):
    openai_api_key: SecretStr
    db_password: SecretStr

    class Config:
        env_file = ".env"   # non commité
        env_file_encoding = "utf-8"

settings = Settings()