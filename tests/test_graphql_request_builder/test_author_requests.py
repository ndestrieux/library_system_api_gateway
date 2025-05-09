import pytest

from utils.graphql.request_body_builders import (
    AuthorMutationRequestBody,
    AuthorQueryRequestBody,
)


class TestAuthorRequestBuilder:
    @pytest.fixture(scope="class")
    def author_data(self):
        """Generate author data."""
        return {
            "first_name": "Dale",
            "last_name": "Cooper",
        }

    @pytest.fixture(scope="class")
    def author_requested_fields(self):
        """Generate requested_fields data for authors."""
        return ["first_name", "last_name", "middle_name"]

    @pytest.fixture(scope="class")
    def author_params(self):
        """Generate author params."""
        return {"first_name": "John"}

    def test_author_query_request_builder_when_all_args_are_present(
        self, author_requested_fields, author_params
    ):
        request = AuthorQueryRequestBody(
            requested_fields=author_requested_fields, operation_args=author_params
        ).full_request
        assert (
            str(request)
            == """query {author(first_name: "John") {first_name last_name middle_name}}"""
        )

    def test_author_query_request_builder_when_no_args_are_present(self):
        request = AuthorQueryRequestBody().full_request
        assert str(request) == "query {author {id first_name middle_name last_name}}"

    def test_author_query_request_builder_when_requested_fields_are_present(self):
        request = AuthorQueryRequestBody(
            requested_fields=["first_name", "last_name"]
        ).full_request
        assert str(request) == "query {author {first_name last_name}}"

    def test_author_query_request_builder_when_operation_args_are_present(self):
        request = AuthorQueryRequestBody(operation_args={"id": 5}).full_request
        assert (
            str(request)
            == """query {author(id: "5") {id first_name middle_name last_name}}"""
        )

    def test_author_query_request_builder_when_requested_fields_and_operation_args_are_present(
        self, author_requested_fields, author_params
    ):
        request = AuthorQueryRequestBody(
            requested_fields=author_requested_fields, operation_args=author_params
        ).full_request
        assert (
            str(request)
            == """query {author(first_name: "John") {first_name last_name middle_name}}"""
        )

    def test_author_query_request_builder_when_requested_fields_and_operation_args_are_empty(
        self,
    ):
        request = AuthorQueryRequestBody(
            requested_fields=[], operation_args={}
        ).full_request
        assert str(request) == "query {author {id first_name middle_name last_name}}"

    def test_author_mutation_request_builder_when_requested_fields_are_not_present(
        self,
        author_data,
    ):
        request = AuthorMutationRequestBody(
            "createAuthor", operation_args=author_data
        ).full_request
        assert (
            str(request)
            == """mutation createAuthor {author(first_name: "Dale", last_name: "Cooper") """
            """{id first_name middle_name last_name}}"""
        )

    def test_author_mutation_request_builder_when_all_args_are_present(
        self, author_data
    ):
        request = AuthorMutationRequestBody(
            "createAuthor",
            operation_args=author_data,
            requested_fields=["first_name", "last_name"],
        ).full_request
        assert (
            str(request)
            == """mutation createAuthor {author(first_name: "Dale", last_name: "Cooper") {first_name last_name}}"""
        )
