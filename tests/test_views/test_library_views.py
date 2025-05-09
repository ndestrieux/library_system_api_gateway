import pytest


@pytest.fixture(scope="module", autouse=True)
def mock_library_router(response_data):
    """Mock the router for testing."""

    with pytest.MonkeyPatch.context() as mp:

        class MockRouter:
            async def send_request(self):
                return response_data

        def mock_send_request(self):
            return MockRouter().send_request()

        mp.setattr("src.routers.library.LibraryRouter.send_request", mock_send_request)
        yield


@pytest.fixture(scope="module", autouse=True)
def mock_library_query_builder():
    """Mock the builder for testing."""

    with pytest.MonkeyPatch.context() as mp:

        class MockBuilder:
            @property
            def full_request(self):
                return "Mocked request body"

        def mock_build_request_body(self):
            return MockBuilder().full_request

        request_body_classes = [
            "AuthorQueryRequestBody",
            "AuthorMutationRequestBody",
            "BookQueryRequestBody",
            "BookMutationRequestBody",
        ]
        for request_body_class in request_body_classes:
            mp.setattr(
                f"src.routers.library.{request_body_class}.full_request",
                mock_build_request_body,
            )


@pytest.fixture(scope="module")
def author_requested_fields():
    """Generate requested_fields data for authors."""
    return {"requested_fields": ["first_name", "last_name"]}


@pytest.fixture(scope="module")
def author_params():
    """Generate author params."""
    return {"first_name": "John"}


@pytest.fixture(scope="module")
def book_requested_fields():
    """Generate requested_fields data for books."""
    return {"requested_fields": ["title", "publication_year"]}


@pytest.fixture(scope="module")
def book_params():
    """Generate book params."""
    return {"publication_year": 1999}


@pytest.mark.asyncio
class TestAuthorList:
    async def test_list_author_view(self, response_data, async_client):
        response = await async_client.get("/api/library/authors/")
        assert response.status_code == 200
        assert response.json() == response_data

    async def test_list_author_view_with_requested_fields(
        self,
        response_data,
        author_requested_fields,
        async_client,
    ):
        response = await async_client.request(
            "get", "/api/library/authors/", json=author_requested_fields
        )
        assert response.status_code == 200
        assert response.json() == response_data

    async def test_list_author_view_with_params(
        self,
        response_data,
        author_params,
        async_client,
    ):
        response = await async_client.get("/api/library/authors/", params=author_params)
        assert response.status_code == 200
        assert response.json() == response_data


@pytest.mark.asyncio
class TestAuthorDetail:
    async def test_detail_author_view(self, response_data, async_client):
        response = await async_client.get("/api/library/authors/1/")
        assert response.status_code == 200
        assert response.json() == response_data

    async def test_detail_author_view_with_requested_fields(
        self,
        response_data,
        author_requested_fields,
        async_client,
    ):
        response = await async_client.request(
            "get", "/api/library/authors/1/", json=author_requested_fields
        )
        assert response.status_code == 200
        assert response.json() == response_data


@pytest.mark.asyncio
class TestAuthorCreate:
    @pytest.fixture(scope="class")
    def body_data_create_author(self):
        """Generate body data for author creation."""
        return {"first_name": "Dale", "last_name": "Cooper"}

    async def test_create_author_view(
        self, response_data, body_data_create_author, async_client
    ):
        response = await async_client.post(
            "/api/library/authors/", json=body_data_create_author
        )
        assert response.status_code == 200
        assert response.json() == response_data

    async def test_create_author_view_with_requested_fields(
        self,
        response_data,
        body_data_create_author,
        author_requested_fields,
        async_client,
    ):
        response = await async_client.post(
            "/api/library/authors/",
            json=body_data_create_author | author_requested_fields,
        )
        assert response.status_code == 200
        assert response.json() == response_data


@pytest.mark.asyncio
class TestAuthorUpdate:
    @pytest.fixture(scope="class")
    def body_data_update_author(self):
        """Generate body data for author update."""
        return {"last_name": "Cooper"}

    async def test_update_author_view(
        self, response_data, body_data_update_author, async_client
    ):
        response = await async_client.patch(
            "/api/library/authors/1/", json=body_data_update_author
        )
        assert response.status_code == 200
        assert response.json() == response_data

    async def test_update_author_view_with_requested_fields(
        self,
        response_data,
        body_data_update_author,
        author_requested_fields,
        async_client,
    ):
        response = await async_client.patch(
            "/api/library/authors/1/",
            json=body_data_update_author | author_requested_fields,
        )
        assert response.status_code == 200
        assert response.json() == response_data


@pytest.mark.asyncio
class TestAuthorDelete:
    async def test_delete_author_view(self, response_data, async_client):
        response = await async_client.delete("/api/library/authors/1/")
        assert response.status_code == 200
        assert response.json() == response_data

    async def test_delete_author_view_with_requested_fields(
        self,
        response_data,
        author_requested_fields,
        async_client,
    ):
        response = await async_client.request(
            "delete", "/api/library/authors/1/", json=author_requested_fields
        )
        assert response.status_code == 200
        assert response.json() == response_data


@pytest.mark.asyncio
class TestBookList:
    async def test_list_book_view(self, response_data, async_client):
        response = await async_client.get("/api/library/books/")
        assert response.status_code == 200
        assert response.json() == response_data

    async def test_list_book_view_with_requested_fields(
        self,
        response_data,
        book_requested_fields,
        async_client,
    ):
        response = await async_client.request(
            "get", "/api/library/books/", json=book_requested_fields
        )
        assert response.status_code == 200
        assert response.json() == response_data

    async def test_list_book_view_with_params(
        self,
        response_data,
        book_params,
        async_client,
    ):
        response = await async_client.get("/api/library/books/", params=book_params)
        assert response.status_code == 200
        assert response.json() == response_data


@pytest.mark.asyncio
class TestBookDetail:
    async def test_detail_book_view(self, response_data, async_client):
        response = await async_client.get("/api/library/books/1/")
        assert response.status_code == 200
        assert response.json() == response_data

    async def test_detail_book_view_with_requested_fields(
        self,
        response_data,
        book_requested_fields,
        async_client,
    ):
        response = await async_client.request(
            "get", "/api/library/books/1/", json=book_requested_fields
        )
        assert response.status_code == 200
        assert response.json() == response_data


@pytest.mark.asyncio
class TestBookCreate:
    @pytest.fixture(scope="class")
    def body_data_create_book(self):
        return {
            "title": "The Hobbit",
            "authors": [1],
            "publication_year": 1937,
            "language": "EN",
            "category": "Fantasy",
        }

    async def test_create_book_view(
        self, response_data, body_data_create_book, async_client
    ):
        response = await async_client.post(
            "/api/library/books/", json=body_data_create_book
        )
        assert response.status_code == 200
        assert response.json() == response_data

    async def test_create_book_view_with_requested_fields(
        self,
        response_data,
        body_data_create_book,
        book_requested_fields,
        async_client,
    ):
        response = await async_client.post(
            "/api/library/books/",
            json=body_data_create_book | book_requested_fields,
        )
        assert response.status_code == 200
        assert response.json() == response_data


@pytest.mark.asyncio
class TestBookUpdate:
    @pytest.fixture(scope="class")
    def body_data_update_book(self):
        return {
            "category": "Epic",
        }

    async def test_update_book_view(
        self, response_data, body_data_update_book, async_client
    ):
        response = await async_client.patch(
            "/api/library/books/1/", json=body_data_update_book
        )
        assert response.status_code == 200
        assert response.json() == response_data

    async def test_update_book_view_with_requested_fields(
        self,
        response_data,
        body_data_update_book,
        book_requested_fields,
        async_client,
    ):
        response = await async_client.patch(
            "/api/library/books/1/",
            json=body_data_update_book | book_requested_fields,
        )
        assert response.status_code == 200
        assert response.json() == response_data


@pytest.mark.asyncio
class TestBookDelete:
    async def test_delete_book_view(self, response_data, async_client):
        response = await async_client.delete("/api/library/books/1/")
        assert response.status_code == 200
        assert response.json() == response_data

    async def test_delete_book_view_with_requested_fields(
        self,
        response_data,
        book_requested_fields,
        async_client,
    ):
        response = await async_client.request(
            "delete", "/api/library/books/1/", json=book_requested_fields
        )
        assert response.status_code == 200
        assert response.json() == response_data
