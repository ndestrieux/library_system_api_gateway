import pytest

from utils.gateway_routers import LibraryRouter


@pytest.mark.asyncio
class TestLibraryRouter:
    @pytest.fixture(scope="function")
    def author_data_obj(self):
        """Generate author data object."""
        return "query {author { Dale Cooper }}"

    @pytest.fixture(scope="function")
    def body_data_create_author(self):
        """Generate body data for author creation."""
        return """mutation createAuthor {author(first_name: "Dale", last_name: "Cooper")
        {id first_name middle_name last_name}}"""

    async def test_library_router_with_get_method(
        self,
        author_data_obj,
        response_data,
    ):
        router = LibraryRouter("/authors/", "get", "user_1234", author_data_obj)
        response = await router.send_request()
        assert response.json() == response_data

    async def test_library_router_with_post_method(
        self, body_data_create_author, response_data
    ):
        router = LibraryRouter(
            "/authors/", "post", "user_1234", body_data_create_author
        )
        response = await router.send_request()
        assert response.json() == response_data
