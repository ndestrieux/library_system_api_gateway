from enum import Enum
from functools import lru_cache

from pydantic_settings import BaseSettings


class UserType(str, Enum):
    MODERATOR = "moderator"
    EMPLOYEE = "employee"
    STANDARD = "standard"

    @classmethod
    def staff_users(cls):
        return [t.value for t in list(cls)[:2]]


class Settings(BaseSettings):
    auth0_domain: str
    auth0_api_audience: str
    auth0_issuer: str
    auth0_algorithms: str

    class Config:
        env_file = "../.env"


@lru_cache()
def get_settings():
    return Settings()
