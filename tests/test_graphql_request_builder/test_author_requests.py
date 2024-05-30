from src.dependencies.graphql.request_body_builders import (
    AuthorMutationRequestBody,
    AuthorQueryRequestBody,
)


def test_author_query_request_builder_when_requested_fields_and_operation_args_are_not_present():
    request = AuthorQueryRequestBody()
    assert str(request) == "query {author {id first_name middle_name last_name}}"


def test_author_query_request_builder_when_requested_fields_are_not_present():
    request = AuthorQueryRequestBody(operation_args={"id": 5})
    assert (
        str(request)
        == """query {author(id: "5") {id first_name middle_name last_name}}"""
    )


def test_author_query_request_builder_when_operation_args_are_not_present():
    request = AuthorQueryRequestBody(requested_fields=["first_name", "last_name"])
    assert str(request) == "query {author {first_name last_name}}"


def test_author_query_request_builder_when_all_args_are_present():
    request = AuthorQueryRequestBody(
        requested_fields=["first_name", "last_name"],
        operation_args={"last_name": "Cooper"},
    )
    assert (
        str(request) == """query {author(last_name: "Cooper") {first_name last_name}}"""
    )


def test_author_mutation_request_builder_when_requested_fields_are_not_present(
    author_data,
):
    request = AuthorMutationRequestBody("createAuthor", operation_args=author_data)
    assert (
        str(request)
        == """mutation createAuthor {author(first_name: "Dale", last_name: "Cooper") """
        """{id first_name middle_name last_name}}"""
    )


def test_author_mutation_request_builder_when_all_args_are_present(author_data):
    request = AuthorMutationRequestBody(
        "createAuthor",
        operation_args=author_data,
        requested_fields=["first_name", "last_name"],
    )
    assert (
        str(request)
        == """mutation createAuthor {author(first_name: "Dale", last_name: "Cooper") {first_name last_name}}"""
    )
