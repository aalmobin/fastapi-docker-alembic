from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    db_url: str
    debug: bool = False
    postgres_user: str
    postgres_pass: str
    postgres_db: str

    class Config:
        env_file = ".env"


settings = Settings()
