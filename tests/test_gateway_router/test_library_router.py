from unittest.mock import patch

import httpx
import pytest

from src.dependencies.gateway_routers import LibraryRouter
from src.dependencies.graphql.request_body_builders import (
    AuthorMutationRequestBody,
    AuthorQueryRequestBody,
    BookMutationRequestBody,
    BookQueryRequestBody,
)


class MockRequestBody:
    def __str__(self):
        return "query {author { Dale Cooper }}"


@pytest.mark.anyio
@patch(
    "src.dependencies.gateway_routers.httpx.AsyncClient.get",
    return_value=httpx.Response(200, json={"data": "Some data", "errors": []}),
)
@patch(
    "tests.test_gateway_router.test_library_router.AuthorQueryRequestBody",
    return_value=MockRequestBody,
)
async def test_library_author_query_router(
    graphql_query_mocker, asyncclient_get_mocker
):
    author_data_obj = AuthorQueryRequestBody()
    router = LibraryRouter("/authors/", "get", "user_1234", author_data_obj)
    response = await router.send_request()
    assert response.json() == {"data": "Some data", "errors": []}


@pytest.mark.anyio
@patch(
    "src.dependencies.gateway_routers.httpx.AsyncClient.post",
    return_value=httpx.Response(200, json={"data": "Some data", "errors": []}),
)
@patch(
    "tests.test_gateway_router.test_library_router.AuthorMutationRequestBody",
    return_value=MockRequestBody,
)
async def test_library_author_mutation_router(
    graphql_query_mocker, asyncclient_get_mocker
):
    author_data_obj = AuthorMutationRequestBody()
    router = LibraryRouter("/authors/", "post", "user_1234", author_data_obj)
    response = await router.send_request()
    assert response.json() == {"data": "Some data", "errors": []}


@pytest.mark.anyio
@patch(
    "src.dependencies.gateway_routers.httpx.AsyncClient.get",
    return_value=httpx.Response(200, json={"data": "Some data", "errors": []}),
)
@patch(
    "tests.test_gateway_router.test_library_router.BookQueryRequestBody",
    return_value=MockRequestBody,
)
async def test_library_book_query_router(graphql_query_mocker, asyncclient_get_mocker):
    author_data_obj = BookQueryRequestBody()
    router = LibraryRouter("/books/", "get", "user_1234", author_data_obj)
    response = await router.send_request()
    assert response.json() == {"data": "Some data", "errors": []}


@pytest.mark.anyio
@patch(
    "src.dependencies.gateway_routers.httpx.AsyncClient.post",
    return_value=httpx.Response(200, json={"data": "Some data", "errors": []}),
)
@patch(
    "tests.test_gateway_router.test_library_router.BookMutationRequestBody",
    return_value=MockRequestBody,
)
async def test_library_book_mutation_router(
    graphql_query_mocker, asyncclient_get_mocker
):
    author_data_obj = BookMutationRequestBody()
    router = LibraryRouter("/authors/", "post", "user_1234", author_data_obj)
    response = await router.send_request()
    assert response.json() == {"data": "Some data", "errors": []}
