from pydantic_settings import BaseSettings


class EnvValidation(BaseSettings):
    TELEGRAM_API_PUBLIC_ID: int
    TELEGRAM_API_SECRET_HASH: str
