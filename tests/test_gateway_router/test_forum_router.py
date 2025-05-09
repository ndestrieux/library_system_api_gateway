import pytest

from utils.gateway_routers import ForumRouter


@pytest.mark.asyncio
class TestForumRouter:
    @pytest.fixture(scope="function")
    def topic_params(self):
        """Generate topic params."""
        return {"category": "XIXth century"}

    @pytest.fixture(scope="function")
    def body_data_create_topic(self):
        return {
            "title": "Star Wars book recommendation",
            "category": "Recommendation",
        }

    @pytest.fixture(scope="function")
    def body_data_update_topic(self):
        return {
            "category": "Science Fiction",
        }

    async def test_forum_topic_router_with_get_method(
        self,
        response_data,
    ):
        router = ForumRouter("/topics/", "get", "user_1234")
        response = await router.send_request()
        assert response.json() == response_data

    async def test_forum_topic_router_with_get_method_with_query_params(
        self,
        response_data,
        topic_params,
    ):
        router = ForumRouter("/topics/", "get", "user_1234", query_params=topic_params)
        response = await router.send_request()
        assert response.json() == response_data

    async def test_forum_topic_router_with_post_method(
        self, response_data, body_data_create_topic
    ):
        router = ForumRouter(
            "/topics/", "post", "user_1234", body=body_data_create_topic
        )
        response = await router.send_request()
        assert response.json() == response_data

    async def test_forum_topic_router_with_patch_method(
        self, response_data, body_data_update_topic
    ):
        router = ForumRouter(
            "/topics/1/", "patch", "user_1234", body=body_data_update_topic
        )
        response = await router.send_request()
        assert response.json() == response_data

    async def test_forum_topic_router_with_delete_method(
        self,
        response_data,
    ):
        router = ForumRouter("/topics/1/", "delete", "user_1234")
        response = await router.send_request()
        assert response.json() == response_data
