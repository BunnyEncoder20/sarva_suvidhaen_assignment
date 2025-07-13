# pydantic
from pydantic_settings import BaseSettings

'''------------------------------------------------------------------'''

# for validation of env variables
class Settings(BaseSettings):

    # postgres DB env variables
    HOSTNAME: str
    DBNAME: str
    USERNAME: str
    PASSWORD: str
    PORT: int

    class Config:
        env_file = ".env"

settings = Settings()
