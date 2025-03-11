from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache

class Settings(BaseSettings):
    jwt_secret_key: str
    jwt_refresh_secret_key: str 
    web_client_id: str
    ios_client_id: str
    android_client_id: str
    smtp_server: str
    smtp_port: int
    sender_email: str
    sender_password: str
    database_url: str
    algorithm_token: str
    model_config = SettingsConfigDict(env_file=".env")

@lru_cache
def get_settings():
    return Settings()