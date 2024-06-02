from unittest.mock import patch

import httpx
import pytest

from src.dependencies.gateway_routers import LibraryRouter
from src.dependencies.graphql.request_body_builders import (
    AuthorMutationRequestBody,
    AuthorQueryRequestBody,
)


class MockQueryRequestBody:
    def __str__(self):
        return "query {author { Dale Cooper }}"


class MockMutationRequestBody:
    def __str__(self):
        return """mutation createAuthor {author(first_name: "Dale", last_name: "Cooper")
        {id first_name middle_name last_name}}"""


@pytest.mark.anyio
@patch(
    "src.dependencies.gateway_routers.httpx.AsyncClient.get",
    return_value=httpx.Response(200, json={"data": "Some data", "errors": []}),
)
@patch(
    "tests.test_gateway_router.test_library_router.AuthorQueryRequestBody",
    return_value=MockQueryRequestBody,
)
async def test_library_router_with_get_method(
    graphql_query_mocker, asyncclient_get_mocker, response_data
):
    author_data_obj = AuthorQueryRequestBody()
    router = LibraryRouter("/authors/", "get", "user_1234", author_data_obj)
    response = await router.send_request()
    assert response.json() == response_data


@pytest.mark.anyio
@patch(
    "src.dependencies.gateway_routers.httpx.AsyncClient.post",
    return_value=httpx.Response(200, json={"data": "Some data", "errors": []}),
)
@patch(
    "tests.test_gateway_router.test_library_router.AuthorMutationRequestBody",
    return_value=MockMutationRequestBody,
)
async def test_library_router_with_post_method(
    graphql_query_mocker, asyncclient_get_mocker, response_data
):
    author_data_obj = AuthorMutationRequestBody()
    router = LibraryRouter("/authors/", "post", "user_1234", author_data_obj)
    response = await router.send_request()
    assert response.json() == response_data
