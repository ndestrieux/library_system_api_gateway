import json
from typing import Any, Dict, Generator

import pytest
from httpx import ASGITransport, AsyncClient

from src.main import app
from src.routers.library import auth_all, auth_staff


@pytest.fixture(scope="session")
def response_data():
    """Generate response data."""
    return json.dumps({"data": "Some data", "errors": []})


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
