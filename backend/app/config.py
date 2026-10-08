from pydantic import BaseModel
import os


class Settings(BaseModel):
    app_name: str = "AI Security Suite"
    environment: str = os.getenv("ENVIRONMENT", "development")
    debug: bool = os.getenv("DEBUG", "true").lower() == "true"
    api_version: str = "v1"
    openai_api_key: str | None = os.getenv("OPENAI_API_KEY")


settings = Settings()
