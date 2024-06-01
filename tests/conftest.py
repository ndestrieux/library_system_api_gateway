import pytest


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


@pytest.fixture(scope="function")
def response_data():
    """Generate response data."""
    return {"data": "Some data", "errors": []}


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
