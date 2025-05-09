import pytest

from utils.graphql.request_body_builders import (
    BookMutationRequestBody,
    BookQueryRequestBody,
)


class TestBookRequestBuilder:
    @pytest.fixture(scope="class")
    def book_data(self):
        return {
            "title": "Dracula",
            "authors": "[1]",
            "publication_year": "1897",
            "language": "ENGLISH",
            "category": "Horror",
        }

    def test_book_query_request_builder_when_all_args_are_present(self):
        request = BookQueryRequestBody(
            requested_fields=["title", "publication_year"],
            operation_args={"title": "Dracula"},
        ).full_request
        assert (
            str(request)
            == """query {book(title: "Dracula") {title publication_year}}"""
        )

    def test_book_query_request_builder_when_requested_fields_are_present(self):
        request = BookQueryRequestBody(
            requested_fields=["title", "publication_year"],
            operation_args={"id": 5},
        ).full_request
        assert str(request) == """query {book(id: "5") {title publication_year}}"""

    def test_book_query_request_builder_when_requested_fields_and_operation_args_are_not_present(
        self,
    ):
        request = BookQueryRequestBody().full_request
        assert (
            str(request)
            == """query {book {id title {authors {first_name middle_name last_name}} """
            """publication_year language category}}"""
        )

    def test_book_query_request_builder_when_requested_fields_are_not_present(self):
        request = BookQueryRequestBody(operation_args={"id": 5}).full_request
        assert (
            str(request)
            == """query {book(id: "5") {id title {authors {first_name middle_name last_name}} """
            """publication_year language category}}"""
        )

    def test_book_query_request_builder_when_operation_args_are_not_present(self):
        request = BookQueryRequestBody(
            requested_fields=["title", "publication_year"]
        ).full_request
        assert str(request) == "query {book {title publication_year}}"

    def test_book_mutation_request_builder_when_requested_fields_are_not_present(
        self, book_data
    ):
        request = BookMutationRequestBody(
            "createBook", operation_args=book_data
        ).full_request
        assert (
            str(request) == """mutation createBook {book"""
            """(title: "Dracula", authors: "[1]", publication_year: "1897", language: "ENGLISH", category: "Horror") """
            """{id title {authors {first_name middle_name last_name}} publication_year language category}}"""
        )

    def test_book_mutation_request_builder_when_all_args_are_present(self, book_data):
        request = BookMutationRequestBody(
            "createBook",
            operation_args=book_data,
            requested_fields=["title", "publication_year"],
        ).full_request
        assert (
            str(request)
            == """mutation createBook {book(title: "Dracula", authors: "[1]", publication_year: "1897", """
            """language: "ENGLISH", category: "Horror") {title publication_year}}"""
        )
