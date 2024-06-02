from abc import ABC
from typing import Dict, List, Optional


class AuthorParamsMixin:
    """Basic data for building GraphQL requests for author endpoints"""

    OBJ_NAME = "author"
    DEFAULT_REQUESTED_FIELD = ["id", "first_name", "middle_name", "last_name"]


class BookParamsMixin:
    """Basic data for building GraphQL requests for book endpoints"""

    OBJ_NAME = "book"
    DEFAULT_REQUESTED_FIELD = [
        "id",
        "title",
        {"authors": ["first_name", "middle_name", "last_name"]},
        "publication_year",
        "language",
        "category",
    ]


class BaseRequestBody(ABC):
    """Abstract class for building GraphQL requests"""

    REQUEST_TYPE: str = None
    OBJ_NAME: str = None
    DEFAULT_REQUESTED_FIELD: List[str | Dict] = []

    def __init__(
        self,
        *,
        operation_args: Optional[Dict[str, str | int]] = None,
        requested_fields: Optional[List[str | Dict]] = None,
    ):
        self.requested_fields = (
            requested_fields if requested_fields else self.DEFAULT_REQUESTED_FIELD
        )
        self.operation_args = operation_args

    @staticmethod
    def _build_operation_args(operation_args: Dict[str, str | int]):
        """Returns a string representing of operation arguments for the request."""
        args_list = [f'{k}: "{v}"' for k, v in operation_args.items()]
        return f"({", ".join(args_list)})"

    def _requested_fields2graphql(
        self,
        fields: Dict[str, str | Dict],
        operation_args: Optional[Dict[str, str | int]] = None,
    ):
        """Builds the whole string chain of requested fields for GraphQL."""
        item = list(fields.keys())[0]
        op_args = self._build_operation_args(operation_args) if operation_args else ""
        result = f"{{{item}{op_args} {{"
        for c, f in enumerate(list(fields.values())[0]):
            if c > 0:
                result += " "
            result += (
                f"{f}" if isinstance(f, str) else self._requested_fields2graphql(f)
            )
        result += "}}"
        return result

    def _build_request(self):
        """Builds GraphQL request for string representation."""
        return self._requested_fields2graphql(
            {self.OBJ_NAME: self.requested_fields}, self.operation_args
        )


class QueryRequestBody(BaseRequestBody, ABC):
    """Abstract class for building GraphQL requests for query types."""

    REQUEST_TYPE = "query"

    def __str__(self):
        return f"{self.REQUEST_TYPE} {self._build_request()}"


class MutationRequestBody(BaseRequestBody, ABC):
    """Abstract class for building GraphQL requests for mutation types."""

    REQUEST_TYPE = "mutation"

    def __init__(
        self,
        mutation_operation_name: str,
        *,
        operation_args: Dict[str, str | int],
        requested_fields: List[str | Dict] | None = None,
    ):
        super().__init__(
            operation_args=operation_args, requested_fields=requested_fields
        )
        self.mutation_operation_name = mutation_operation_name

    def __str__(self):
        return f"{self.REQUEST_TYPE} {self.mutation_operation_name} {self._build_request()}"


class AuthorQueryRequestBody(AuthorParamsMixin, QueryRequestBody):
    """Class for GraphQL query-type author items."""


class AuthorMutationRequestBody(AuthorParamsMixin, MutationRequestBody):
    """Class for GraphQL mutation-type author items."""


class BookQueryRequestBody(BookParamsMixin, QueryRequestBody):
    """Class for GraphQL query-type book items."""


class BookMutationRequestBody(BookParamsMixin, MutationRequestBody):
    """Class for GraphQL mutation-type book items."""
