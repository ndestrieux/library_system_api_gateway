from src.dependencies.graphql.request_builders import (
    GraphQLBookMutationRequest,
    GraphQLBookQueryRequest,
)


def test_book_query_request_builder_when_required_fields_and_operation_args_are_not_present():
    request = GraphQLBookQueryRequest()
    assert (
        str(request)
        == """query {book {id title {authors {first_name middle_name last_name}} """
        """publication_year language category}}"""
    )


def test_book_query_request_builder_when_required_fields_are_not_present():
    request = GraphQLBookQueryRequest(operation_args={"id": 5})
    assert (
        str(request)
        == """query {book(id: "5") {id title {authors {first_name middle_name last_name}} """
        """publication_year language category}}"""
    )


def test_author_query_request_builder_when_operation_args_are_not_present():
    request = GraphQLBookQueryRequest(required_fields=["title", "publication_year"])
    assert str(request) == "query {book {title publication_year}}"


def test_author_query_request_builder_when_all_args_are_present():
    request = GraphQLBookQueryRequest(
        required_fields=["title", "publication_year"],
        operation_args={"title": "Dracula"},
    )
    assert str(request) == """query {book(title: "Dracula") {title publication_year}}"""


def test_book_mutation_request_builder_when_required_fields_are_not_present(
    book_data,
):
    request = GraphQLBookMutationRequest("createBook", operation_args=book_data)
    assert (
        str(request) == """mutation createBook {book"""
        """(title: "Dracula", authors: "[1]", publication_year: "1897", language: "ENGLISH", category: "Horror") """
        """{id title {authors {first_name middle_name last_name}} publication_year language category}}"""
    )


def test_book_mutation_request_builder_when_all_args_are_present(book_data):
    request = GraphQLBookMutationRequest(
        "createBook",
        operation_args=book_data,
        required_fields=["title", "publication_year"],
    )
    assert (
        str(request)
        == """mutation createBook {book(title: "Dracula", authors: "[1]", publication_year: "1897", """
        """language: "ENGLISH", category: "Horror") {title publication_year}}"""
    )
