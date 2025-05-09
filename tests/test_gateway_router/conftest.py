from unittest.mock import AsyncMock, patch

import pytest
from httpx import Response


@pytest.fixture(scope="module", autouse=True)
def mock_httpx_client(response_data):
    """Fixture to mock httpx.AsyncClient."""
    with patch("httpx.AsyncClient") as MockClient:
        mock_client_instance = MockClient.return_value
        mock_client_instance.__aenter__.return_value = mock_client_instance
        mock_client_instance.get = AsyncMock(
            return_value=Response(200, json=response_data)
        )
        mock_client_instance.post = AsyncMock(
            return_value=Response(200, json=response_data)
        )
        mock_client_instance.patch = AsyncMock(
            return_value=Response(200, json=response_data)
        )
        mock_client_instance.delete = AsyncMock(
            return_value=Response(200, json=response_data)
        )
        yield mock_client_instance
