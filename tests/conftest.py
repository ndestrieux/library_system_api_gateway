import pytest


@pytest.fixture(scope="function")
def author_data():
    """Generate author_data."""
    return {"first_name": "Dale", "last_name": "Cooper"}


@pytest.fixture(scope="function")
def book_data():
    """Generate author_data."""
    return {
        "title": "Dracula",
        "authors": [1],
        "publication_year": 1897,
        "language": "ENGLISH",
        "category": "Horror",
    }
