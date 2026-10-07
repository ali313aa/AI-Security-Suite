from pydantic import BaseModel


class Settings(BaseModel):
    app_name: str = "AI Security Suite"
    environment: str = "development"
    debug: bool = True
    api_version: str = "v1"


settings = Settings()
