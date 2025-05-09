from abc import ABC, abstractmethod
from typing import Any, Dict, Optional

import httpx
from fastapi import Response

from conf import get_settings
from utils.graphql.request_body_builders import BaseRequestBody


class BaseRouter(ABC):
    """Abstract class for router"""

    BASE_URL: str = None

    def __init__(self, path: str, request_method: str, user_id: str):
        self.path = path
        self.request_method = request_method
        self.user_id = user_id

    @property
    def full_path(self) -> str:
        return self.BASE_URL + self.path

    def _get_headers(self) -> Dict[str, str]:
        """Retrieve headers"""
        return {"requester": self.user_id}

    @abstractmethod
    def _get_body(self) -> Dict[str, str | int]:
        """Retrieve request data"""

    def _build_request(self) -> Dict[str, Any]:
        """Retrieve all elements for HTTP request"""
        return {
            "url": self.full_path,
            "headers": self._get_headers(),
            "data": self._get_body(),
        }

    async def send_request(self) -> Response:
        """Route request to specified microservice."""
        async with httpx.AsyncClient() as client:
            response = await getattr(client, self.request_method)(
                **self._build_request()
            )
        return response


class GraphqlRouter(BaseRouter, ABC):
    def __init__(
        self, path, request_method: str, user_id: str, graphql_body_obj: BaseRequestBody
    ):
        super().__init__(path, request_method, user_id)
        self.graphql_body_obj = graphql_body_obj

    def _get_body(self) -> Dict:
        return {"query": self.graphql_body_obj}


class RESTRouter(BaseRouter, ABC):
    def __init__(
        self,
        path: str,
        request_method: str,
        user_id: str,
        *,
        body: Optional[Dict[str, str | int]] = None,
        query_params: Optional[Dict[str, str]] = None,
    ):
        super().__init__(path, request_method, user_id)
        self.body = body
        self.query_params = query_params

    def _get_body(self):
        return self.body or ""

    def _build_request(self):
        req_dict = super()._build_request()
        if self.query_params:
            return req_dict | {"params": self.query_params}
        return req_dict


class LibraryRouter(GraphqlRouter):
    BASE_URL = get_settings().library_endpoint


class ForumRouter(RESTRouter):
    BASE_URL = get_settings().forum_endpoint
