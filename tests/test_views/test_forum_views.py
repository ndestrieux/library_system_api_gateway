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
    "src.utils.gateway_routers.httpx.AsyncClient.get",
    return_value=httpx.Response(200, json={"data": "Some data", "errors": []}),
)
def test_list_topic_view(asyncclient_get_mocker, response_data):
    response = client.get("/api/forum/topics/")
    assert response.status_code == 200
    assert response.json() == response_data


@patch(
    "src.utils.gateway_routers.httpx.AsyncClient.get",
    return_value=httpx.Response(200, json={"data": "Some data", "errors": []}),
)
def test_list_topic_view_with_params(
    asyncclient_get_mocker, response_data, topic_params
):
    response = client.get("/api/forum/topics/", params=topic_params)
    assert response.status_code == 200
    assert response.json() == response_data


@patch(
    "src.utils.gateway_routers.httpx.AsyncClient.get",
    return_value=httpx.Response(200, json={"data": "Some data", "errors": []}),
)
def test_detail_topic_view(asyncclient_get_mocker, response_data):
    response = client.get("/api/forum/topics/1/")
    assert response.status_code == 200
    assert response.json() == response_data


@patch(
    "src.utils.gateway_routers.httpx.AsyncClient.post",
    return_value=httpx.Response(200, json={"data": "Some data", "errors": []}),
)
def test_create_topic_view(
    asyncclient_get_mocker, response_data, body_data_create_topic
):
    response = client.post(
        "/api/forum/topics/",
        json=body_data_create_topic,
    )
    assert response.status_code == 200
    assert response.json() == response_data


@patch(
    "src.utils.gateway_routers.httpx.AsyncClient.patch",
    return_value=httpx.Response(200, json={"data": "Some data", "errors": []}),
)
def test_update_topic_view(
    asyncclient_get_mocker, response_data, body_data_update_topic
):
    response = client.patch("/api/forum/topics/1/", json=body_data_update_topic)
    assert response.status_code == 200
    assert response.json() == response_data


@patch(
    "src.utils.gateway_routers.httpx.AsyncClient.delete",
    return_value=httpx.Response(200, json={"data": "Some data", "errors": []}),
)
def test_delete_topic_view(asyncclient_get_mocker, response_data):
    response = client.delete("/api/forum/topics/1/")
    assert response.status_code == 200
    assert response.json() == response_data


@patch(
    "src.utils.gateway_routers.httpx.AsyncClient.get",
    return_value=httpx.Response(200, json={"data": "Some data", "errors": []}),
)
def test_detail_post_view(asyncclient_get_mocker, response_data):
    response = client.get("/api/forum/posts/1/")
    assert response.status_code == 200
    assert response.json() == response_data


@patch(
    "src.utils.gateway_routers.httpx.AsyncClient.post",
    return_value=httpx.Response(200, json={"data": "Some data", "errors": []}),
)
def test_create_post_view(asyncclient_get_mocker, response_data, body_data_create_post):
    response = client.post(
        "/api/forum/posts/",
        json=body_data_create_post,
    )
    assert response.status_code == 200
    assert response.json() == response_data


@patch(
    "src.utils.gateway_routers.httpx.AsyncClient.patch",
    return_value=httpx.Response(200, json={"data": "Some data", "errors": []}),
)
def test_update_post_view(asyncclient_get_mocker, response_data, body_data_update_post):
    response = client.patch("/api/forum/posts/1/", json=body_data_update_post)
    assert response.status_code == 200
    assert response.json() == response_data


@patch(
    "src.utils.gateway_routers.httpx.AsyncClient.delete",
    return_value=httpx.Response(200, json={"data": "Some data", "errors": []}),
)
def test_delete_post_view(asyncclient_get_mocker, response_data):
    response = client.delete("/api/forum/posts/1/")
    assert response.status_code == 200
    assert response.json() == response_data
