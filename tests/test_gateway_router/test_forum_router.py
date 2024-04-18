from unittest.mock import patch

import httpx
import pytest

from utils.gateway_routers import ForumRouter


@pytest.mark.anyio
@patch(
    "src.utils.gateway_routers.httpx.AsyncClient.get",
    return_value=httpx.Response(200, json={"data": "Some data", "errors": []}),
)
async def test_forum_topic_router_with_get_method(
    asyncclient_get_mocker, response_data
):
    router = ForumRouter("/topics/", "get", "user_1234")
    response = await router.send_request()
    assert response.json() == response_data


@pytest.mark.anyio
@patch(
    "src.utils.gateway_routers.httpx.AsyncClient.get",
    return_value=httpx.Response(200, json={"data": "Some data", "errors": []}),
)
async def test_forum_topic_router_with_get_method_with_query_params(
    asyncclient_get_mocker, response_data, topic_params
):
    router = ForumRouter("/topics/", "get", "user_1234", query_params=topic_params)
    response = await router.send_request()
    assert response.json() == response_data


@pytest.mark.anyio
@patch(
    "src.utils.gateway_routers.httpx.AsyncClient.post",
    return_value=httpx.Response(200, json={"data": "Some data", "errors": []}),
)
async def test_forum_topic_router_with_post_method(
    asyncclient_get_mocker, response_data, body_data_create_topic
):
    router = ForumRouter("/topics/", "post", "user_1234", body=body_data_create_topic)
    response = await router.send_request()
    assert response.json() == response_data


@pytest.mark.anyio
@patch(
    "src.utils.gateway_routers.httpx.AsyncClient.patch",
    return_value=httpx.Response(200, json={"data": "Some data", "errors": []}),
)
async def test_forum_topic_router_with_patch_method(
    asyncclient_get_mocker, response_data, body_data_update_topic
):
    router = ForumRouter(
        "/topics/1/", "patch", "user_1234", body=body_data_update_topic
    )
    response = await router.send_request()
    assert response.json() == response_data


@pytest.mark.anyio
@patch(
    "src.utils.gateway_routers.httpx.AsyncClient.delete",
    return_value=httpx.Response(200, json={"data": "Some data", "errors": []}),
)
async def test_forum_topic_router_with_patch_method(
    asyncclient_get_mocker, response_data
):
    router = ForumRouter("/topics/1/", "delete", "user_1234")
    response = await router.send_request()
    assert response.json() == response_data
