import json
from typing import Any, Dict, Generator

import pytest
from httpx import ASGITransport, AsyncClient, Response

from src.main import app
from src.routers.library import auth_all, auth_staff


@pytest.fixture(scope="function")
def author_data():
    """Generate author data."""
    return {"first_name": "Dale", "last_name": "Cooper"}


@pytest.fixture(scope="function")
def book_data():
    """Generate book data."""
    return {
        "title": "Dracula",
        "authors": [1],
        "publication_year": 1897,
        "language": "ENGLISH",
        "category": "Horror",
    }


@pytest.fixture(scope="session")
def response_data():
    """Generate response data."""
    return json.dumps({"data": "Some data", "errors": []})


@pytest.fixture(scope="function")
def author_requested_fields():
    """Generate requested_fields data for authors."""
    return {"requested_fields": ["first_name", "last_name"]}


@pytest.fixture(scope="function")
def author_params():
    """Generate author params."""
    return {"first_name": "John"}


@pytest.fixture(scope="function")
def body_data_create_author():
    """Generate body data for author creation."""
    return {"first_name": "Dale", "last_name": "Cooper"}


@pytest.fixture(scope="function")
def body_data_update_author():
    """Generate body data for author update."""
    return {"last_name": "Cooper"}


@pytest.fixture(scope="function")
def book_requested_fields():
    """Generate requested_fields data for books."""
    return {"requested_fields": ["title", "publication_year"]}


@pytest.fixture(scope="function")
def book_params():
    """Generate book params."""
    return {"publication_year": 1999}


@pytest.fixture(scope="function")
def body_data_create_book():
    return {
        "title": "The Hobbit",
        "authors": [1],
        "publication_year": 1937,
        "language": "EN",
        "category": "Fantasy",
    }


@pytest.fixture(scope="function")
def body_data_update_book():
    return {"category": "Epic"}


@pytest.fixture(scope="function")
def body_data_create_topic():
    return {
        "title": "Star Wars book recommendation",
        "category": "Recommendation",
    }


@pytest.fixture(scope="function")
def body_data_update_topic():
    return {
        "category": "Science Fiction",
    }


@pytest.fixture(scope="function")
def topic_params():
    """Generate topic params."""
    return {"category": "XIXth century"}


@pytest.fixture(scope="function")
def body_data_create_post():
    return {
        "content": "I have a question...",
        "topic": 1,
    }


@pytest.fixture(scope="function")
def body_data_update_post():
    return {
        "content": "I was wondering...",
        "topic": 1,
    }


@pytest.fixture
def mock_httpx_requests(response_data):
    class MockAsyncClient:
        @classmethod
        async def get(cls, *args, **kwargs):
            return Response(200, json=response_data)

    return MockAsyncClient


@pytest.fixture(scope="session", autouse=True)
def override_auth_verify(request) -> Generator[None, Any, None]:
    """
    Overrides the authentication verification dependencies for testing purposes.
    """

    def mock_verify() -> Generator[Dict[str, str], None, None]:
        yield {"sub": "user1234"}

    app.dependency_overrides[auth_all.verify] = mock_verify
    app.dependency_overrides[auth_staff.verify] = mock_verify
    yield
    del app.dependency_overrides[auth_all.verify]
    del app.dependency_overrides[auth_staff.verify]


@pytest.fixture(scope="session")
def async_client() -> Generator[AsyncClient, None, None]:
    """Create a test async client."""
    yield AsyncClient(transport=ASGITransport(app=app), base_url="http://test/")
