from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    OPENROUTER_API_KEY: str
    OPENROUTER_MODEL: str = "meta-llama/llama-3.3-70b-instruct"

    DATABASE_URL: str

    class Config:
        env_file = ".env"


settings = Settings()