from typing import Any, Dict


def get_user_id_from_token(token: Dict[str, Any]) -> str:
    return token.get("sub")
