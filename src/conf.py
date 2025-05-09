from enum import Enum
from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class UserType(str, Enum):
    MODERATOR = "moderator"
    EMPLOYEE = "employee"
    STANDARD = "standard"

    @classmethod
    def staff_users(cls):
        return [t.value for t in list(cls)[:2]]


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")

    auth0_domain: str
    auth0_api_audience: str
    auth0_issuer: str
    auth0_algorithms: str

    library_endpoint: str
    forum_endpoint: str

    jwt_secret: str
    jwt_algorithm: str


@lru_cache()
def get_settings():
    return Settings()
