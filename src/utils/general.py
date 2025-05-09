from typing import Any, Dict, List

import jwt
from pydantic import BaseModel

from conf import get_settings


class UserInfo(BaseModel):
    id: str
    groups: List[str]

    def to_jwt(self) -> str:
        """Convert to JWT token"""
        return jwt.encode(
            self.model_dump(), get_settings().jwt_secret, get_settings().jwt_algorithm
        )


def get_user_info_from_token(token: Dict[str, Any]) -> UserInfo:
    user_id = token.get("sub")
    roles = token.get(f"{get_settings().auth0_api_audience}roles", [])
    return UserInfo(id=user_id, groups=roles)
