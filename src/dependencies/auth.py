from typing import List, Optional

import jwt
from fastapi import Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer, SecurityScopes

import conf
from conf import get_settings
from exceptions import UnauthenticatedException, UnauthorizedException


class VerifyToken:
    """Does all the token verification using PyJWT"""

    def __init__(self, authorized_user_roles: Optional[List] = None):
        self.config = get_settings()
        jwks_url = f"https://{self.config.auth0_domain}/.well-known/jwks.json"
        self.jwks_client = jwt.PyJWKClient(jwks_url)
        self.authorized_user_roles = (
            authorized_user_roles if authorized_user_roles else list(conf.UserType)
        )

    async def verify(
        self,
        security_scopes: SecurityScopes,
        token: Optional[HTTPAuthorizationCredentials] = Depends(HTTPBearer()),
    ):
        if token is None:
            raise UnauthenticatedException
        try:
            signing_key = self.jwks_client.get_signing_key_from_jwt(
                token.credentials
            ).key
        except jwt.exceptions.PyJWKClientError as error:
            raise UnauthorizedException(str(error))
        except jwt.exceptions.DecodeError as error:
            raise UnauthorizedException(str(error))
        try:
            payload = jwt.decode(
                token.credentials,
                signing_key,
                algorithms=self.config.auth0_algorithms,
                audience=self.config.auth0_api_audience,
                issuer=self.config.auth0_issuer,
            )
        except Exception as error:
            raise UnauthorizedException(str(error))
        if not (
            set(payload.get(f"{self.config.auth0_api_audience}roles", []))
            & set(self.authorized_user_roles)
        ):
            raise UnauthorizedException(
                "You do not have enough rights to access this resource."
            )
        return payload
