# from pydantic import BaseSettings
# from pydantic_settings import BaseSettings # NEW
from pydantic.v1 import BaseSettings


class Settings(BaseSettings):
    app_name: str
    mongo_url: str
    
    class Config:
        env_file = ".env"