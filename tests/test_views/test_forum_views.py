import pytest


@pytest.fixture(scope="module", autouse=True)
def mock_forum_router(response_data):
    """Mock the router for testing."""

    with pytest.MonkeyPatch.context() as mp:

        class MockRouter:
            async def send_request(self):
                return response_data

        def mock_send_request(self):
            return MockRouter().send_request()

        mp.setattr("src.routers.forum.ForumRouter.send_request", mock_send_request)
        yield


@pytest.mark.asyncio
class TestForumList:
    async def test_list_topic_view(self, response_data, async_client):
        response = await async_client.get("/api/forum/topics/")
        assert response.status_code == 200
        assert response.json() == response_data

    async def test_list_topic_view_with_params(
        self, response_data, topic_params, async_client
    ):
        response = await async_client.get("/api/forum/topics/", params=topic_params)
        assert response.status_code == 200
        assert response.json() == response_data


@pytest.mark.asyncio
class TestForumDetail:
    async def test_detail_topic_view(self, response_data, async_client):
        response = await async_client.get("/api/forum/topics/1/")
        assert response.status_code == 200
        assert response.json() == response_data


@pytest.mark.asyncio
class TestForumCreate:
    async def test_create_topic_view(
        self, response_data, body_data_create_topic, async_client
    ):
        response = await async_client.post(
            "/api/forum/topics/",
            json=body_data_create_topic,
        )
        assert response.status_code == 200
        assert response.json() == response_data


@pytest.mark.asyncio
class TestForumUpdate:
    async def test_update_topic_view(
        self, response_data, body_data_update_topic, async_client
    ):
        response = await async_client.patch(
            "/api/forum/topics/1/", json=body_data_update_topic
        )
        assert response.status_code == 200
        assert response.json() == response_data


@pytest.mark.asyncio
class TestForumDelete:
    async def test_delete_topic_view(self, response_data, async_client):
        response = await async_client.delete("/api/forum/topics/1/")
        assert response.status_code == 200
        assert response.json() == response_data


@pytest.mark.asyncio
class TestForumPostDetail:
    async def test_detail_post_view(self, response_data, async_client):
        response = await async_client.get("/api/forum/posts/1/")
        assert response.status_code == 200
        assert response.json() == response_data


@pytest.mark.asyncio
class TestForumPostCreate:
    async def test_create_post_view(
        self, response_data, body_data_create_post, async_client
    ):
        response = await async_client.post(
            "/api/forum/posts/",
            json=body_data_create_post,
        )
        assert response.status_code == 200
        assert response.json() == response_data


@pytest.mark.asyncio
class TestForumPostUpdate:
    async def test_update_post_view(
        self, response_data, body_data_update_post, async_client
    ):
        response = await async_client.patch(
            "/api/forum/posts/1/", json=body_data_update_post
        )
        assert response.status_code == 200
        assert response.json() == response_data


@pytest.mark.asyncio
class TestForumPostDelete:
    async def test_delete_post_view(self, response_data, async_client):
        response = await async_client.delete("/api/forum/posts/1/")
        assert response.status_code == 200
        assert response.json() == response_data
