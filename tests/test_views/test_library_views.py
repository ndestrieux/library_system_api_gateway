from unittest.mock import patch

import httpx
from fastapi.testclient import TestClient

from params import auth_all, auth_staff
from src.main import app


async def mock_verify_token():
    return {"sub": "user1234"}


app.dependency_overrides[auth_all.verify] = mock_verify_token
app.dependency_overrides[auth_staff.verify] = mock_verify_token


client = TestClient(app)


@patch(
    "src.dependencies.gateway_routers.httpx.AsyncClient.get",
    return_value=httpx.Response(200, json={"data": "Some data", "errors": []}),
)
def test_list_author_view(asyncclient_get_mocker, response_data):
    response = client.get("/api/library/authors/")
    assert response.status_code == 200
    assert response.json() == response_data


@patch(
    "src.dependencies.gateway_routers.httpx.AsyncClient.get",
    return_value=httpx.Response(200, json={"data": "Some data", "errors": []}),
)
def test_list_author_view_with_requested_fields(
    asyncclient_get_mocker, response_data, author_requested_fields
):
    response = client.request(
        "get", "/api/library/authors/", json=author_requested_fields
    )
    assert response.status_code == 200
    assert response.json() == response_data


@patch(
    "src.dependencies.gateway_routers.httpx.AsyncClient.get",
    return_value=httpx.Response(200, json={"data": "Some data", "errors": []}),
)
def test_list_author_view_with_params(
    asyncclient_get_mocker, response_data, author_params
):
    response = client.request("get", "/api/library/authors/", params=author_params)
    assert response.status_code == 200
    assert response.json() == response_data


@patch(
    "src.dependencies.gateway_routers.httpx.AsyncClient.get",
    return_value=httpx.Response(200, json={"data": "Some data", "errors": []}),
)
def test_detail_author_view(asyncclient_get_mocker, response_data):
    response = client.get("/api/library/authors/1/")
    assert response.status_code == 200
    assert response.json() == response_data


@patch(
    "src.dependencies.gateway_routers.httpx.AsyncClient.get",
    return_value=httpx.Response(200, json={"data": "Some data", "errors": []}),
)
def test_detail_author_view_with_requested_fields(
    asyncclient_get_mocker, response_data, author_requested_fields
):
    response = client.request(
        "get", "/api/library/authors/1/", json=author_requested_fields
    )
    assert response.status_code == 200
    assert response.json() == response_data


@patch(
    "src.dependencies.gateway_routers.httpx.AsyncClient.post",
    return_value=httpx.Response(200, json={"data": "Some data", "errors": []}),
)
def test_create_author_view(
    asyncclient_get_mocker, response_data, body_data_create_author
):
    response = client.post("/api/library/authors/", json=body_data_create_author)
    assert response.status_code == 200
    assert response.json() == response_data


@patch(
    "src.dependencies.gateway_routers.httpx.AsyncClient.post",
    return_value=httpx.Response(200, json={"data": "Some data", "errors": []}),
)
def test_create_author_view_with_requested_fields(
    asyncclient_get_mocker,
    response_data,
    body_data_create_author,
    author_requested_fields,
):
    response = client.post(
        "/api/library/authors/", json=body_data_create_author | author_requested_fields
    )
    assert response.status_code == 200
    assert response.json() == response_data


@patch(
    "src.dependencies.gateway_routers.httpx.AsyncClient.post",
    return_value=httpx.Response(200, json={"data": "Some data", "errors": []}),
)
def test_update_author_view(
    asyncclient_get_mocker, response_data, body_data_update_author
):
    response = client.patch("/api/library/authors/1/", json=body_data_update_author)
    assert response.status_code == 200
    assert response.json() == response_data


@patch(
    "src.dependencies.gateway_routers.httpx.AsyncClient.post",
    return_value=httpx.Response(200, json={"data": "Some data", "errors": []}),
)
def test_update_author_view_with_requested_fields(
    asyncclient_get_mocker,
    response_data,
    body_data_update_author,
    author_requested_fields,
):
    response = client.patch(
        "/api/library/authors/1/",
        json=body_data_update_author | author_requested_fields,
    )
    assert response.status_code == 200
    assert response.json() == response_data


@patch(
    "src.dependencies.gateway_routers.httpx.AsyncClient.post",
    return_value=httpx.Response(200, json={"data": "Some data", "errors": []}),
)
def test_delete_author_view(asyncclient_get_mocker, response_data):
    response = client.delete("/api/library/authors/1/")
    assert response.status_code == 200
    assert response.json() == response_data


@patch(
    "src.dependencies.gateway_routers.httpx.AsyncClient.post",
    return_value=httpx.Response(200, json={"data": "Some data", "errors": []}),
)
def test_delete_author_view_with_requested_fields(
    asyncclient_get_mocker, response_data, author_requested_fields
):
    response = client.request(
        "delete", "/api/library/authors/1/", json=author_requested_fields
    )
    assert response.status_code == 200
    assert response.json() == response_data


@patch(
    "src.dependencies.gateway_routers.httpx.AsyncClient.get",
    return_value=httpx.Response(200, json={"data": "Some data", "errors": []}),
)
def test_list_book_view(asyncclient_get_mocker, response_data):
    response = client.get("/api/library/books/")
    assert response.status_code == 200
    assert response.json() == response_data


@patch(
    "src.dependencies.gateway_routers.httpx.AsyncClient.get",
    return_value=httpx.Response(200, json={"data": "Some data", "errors": []}),
)
def test_list_book_view_with_requested_fields(
    asyncclient_get_mocker, response_data, book_requested_fields
):
    response = client.request("get", "/api/library/books/", json=book_requested_fields)
    assert response.status_code == 200
    assert response.json() == response_data


@patch(
    "src.dependencies.gateway_routers.httpx.AsyncClient.get",
    return_value=httpx.Response(200, json={"data": "Some data", "errors": []}),
)
def test_list_book_view_with_params(asyncclient_get_mocker, response_data, book_params):
    response = client.request("get", "/api/library/books/", params=book_params)
    assert response.status_code == 200
    assert response.json() == response_data


@patch(
    "src.dependencies.gateway_routers.httpx.AsyncClient.get",
    return_value=httpx.Response(200, json={"data": "Some data", "errors": []}),
)
def test_detail_book_view(asyncclient_get_mocker, response_data):
    response = client.get("/api/library/books/1/")
    assert response.status_code == 200
    assert response.json() == response_data


@patch(
    "src.dependencies.gateway_routers.httpx.AsyncClient.get",
    return_value=httpx.Response(200, json={"data": "Some data", "errors": []}),
)
def test_detail_book_view_with_requested_fields(
    asyncclient_get_mocker, response_data, book_requested_fields
):
    response = client.request(
        "get", "/api/library/books/1/", json=book_requested_fields
    )
    assert response.status_code == 200
    assert response.json() == response_data


@patch(
    "src.dependencies.gateway_routers.httpx.AsyncClient.post",
    return_value=httpx.Response(200, json={"data": "Some data", "errors": []}),
)
def test_create_book_view(asyncclient_get_mocker, response_data, body_data_create_book):
    response = client.post("/api/library/books/", json=body_data_create_book)
    assert response.status_code == 200
    assert response.json() == response_data


@patch(
    "src.dependencies.gateway_routers.httpx.AsyncClient.post",
    return_value=httpx.Response(200, json={"data": "Some data", "errors": []}),
)
def test_create_book_view_with_requested_fields(
    asyncclient_get_mocker, response_data, body_data_create_book, book_requested_fields
):
    response = client.post(
        "/api/library/books/", json=body_data_create_book | book_requested_fields
    )
    assert response.status_code == 200
    assert response.json() == response_data


@patch(
    "src.dependencies.gateway_routers.httpx.AsyncClient.post",
    return_value=httpx.Response(200, json={"data": "Some data", "errors": []}),
)
def test_update_book_view(asyncclient_get_mocker, response_data, body_data_update_book):
    response = client.patch("/api/library/books/1/", json=body_data_update_book)
    assert response.status_code == 200
    assert response.json() == response_data


@patch(
    "src.dependencies.gateway_routers.httpx.AsyncClient.post",
    return_value=httpx.Response(200, json={"data": "Some data", "errors": []}),
)
def test_update_book_view_with_requested_fields(
    asyncclient_get_mocker, response_data, body_data_update_book, book_requested_fields
):
    response = client.patch(
        "/api/library/books/1/", json=body_data_update_book | book_requested_fields
    )
    assert response.status_code == 200
    assert response.json() == response_data


@patch(
    "src.dependencies.gateway_routers.httpx.AsyncClient.post",
    return_value=httpx.Response(200, json={"data": "Some data", "errors": []}),
)
def test_delete_book_view(asyncclient_get_mocker, response_data):
    response = client.delete("/api/library/books/1/")
    assert response.status_code == 200
    assert response.json() == response_data


@patch(
    "src.dependencies.gateway_routers.httpx.AsyncClient.post",
    return_value=httpx.Response(200, json={"data": "Some data", "errors": []}),
)
def test_delete_book_view_with_requested_fields(
    asyncclient_get_mocker, response_data, book_requested_fields
):
    response = client.request(
        "delete", "/api/library/books/1/", json=book_requested_fields
    )
    assert response.status_code == 200
    assert response.json() == response_data
