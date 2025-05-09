from typing import Any, Dict, Optional

from fastapi import APIRouter, Depends, Response, Security

from datastructures.library import (
    AuthorCreateForm,
    AuthorQueryParams,
    AuthorUpdateForm,
    BookCreateForm,
    BookQueryParams,
    BookUpdateForm,
    LibraryBaseModel,
)
from router_params import SUB_PATH, auth_all, auth_staff
from utils.gateway_routers import LibraryRouter
from utils.general import get_user_info_from_token
from utils.graphql.request_body_builders import (
    AuthorMutationRequestBody,
    AuthorQueryRequestBody,
    BookMutationRequestBody,
    BookQueryRequestBody,
)

router = APIRouter(prefix="/api/library", tags=["library"])


@router.get("/authors/")
async def author_list(
    form: Optional[LibraryBaseModel] = None,
    query_params: AuthorQueryParams = Depends(),
    auth_result: Dict[str, Any] = Security(auth_all.verify),
) -> Response:
    request_data = {"operation_args": query_params.model_dump(exclude_none=True)}
    if form:
        request_data |= form.model_dump(include={"requested_fields"})
    body_obj = AuthorQueryRequestBody(**request_data).full_request
    user_info = get_user_info_from_token(auth_result)
    author_router = LibraryRouter(SUB_PATH["author"], "get", user_info, body_obj)
    response = await author_router.send_request()
    return response


@router.get("/authors/{item_id}/")
async def author_details(
    item_id: int,
    form: Optional[LibraryBaseModel] = None,
    auth_result: Dict[str, Any] = Security(auth_all.verify),
) -> Response:
    request_data = {"operation_args": {"id": item_id}}
    if form:
        request_data |= form.model_dump(include={"requested_fields"})
    body_obj = AuthorQueryRequestBody(**request_data).full_request
    user_info = get_user_info_from_token(auth_result)
    author_router = LibraryRouter(
        f"{SUB_PATH["author"]}{item_id}/", "get", user_info, body_obj
    )
    response = await author_router.send_request()
    return response


@router.post("/authors/")
async def create_author(
    form: AuthorCreateForm, auth_result: Dict[str, Any] = Security(auth_staff.verify)
) -> Response:
    request_data = {
        "mutation_operation_name": "createAuthor",
        "operation_args": form.model_dump(
            exclude={"requested_fields"}, exclude_none=True
        ),
    } | form.model_dump(include={"requested_fields"})
    body_obj = AuthorMutationRequestBody(**request_data).full_request
    user_info = get_user_info_from_token(auth_result)
    author_router = LibraryRouter(SUB_PATH["author"], "post", user_info, body_obj)
    response = await author_router.send_request()
    return response


@router.patch("/authors/{item_id}/")
async def update_author(
    item_id: int,
    form: AuthorUpdateForm,
    auth_result: Dict[str, Any] = Security(auth_staff.verify),
) -> Response:
    request_data = {
        "mutation_operation_name": "updateAuthor",
        "operation_args": {"id": item_id}
        | form.model_dump(exclude={"requested_fields"}, exclude_none=True),
    } | form.model_dump(include={"requested_fields"})
    body_obj = AuthorMutationRequestBody(**request_data).full_request
    user_info = get_user_info_from_token(auth_result)
    author_router = LibraryRouter(
        f"{SUB_PATH["author"]}{item_id}/", "post", user_info, body_obj
    )
    response = await author_router.send_request()
    return response


@router.delete("/authors/{item_id}/")
async def delete_author(
    item_id: int, auth_result: Dict[str, Any] = Security(auth_staff.verify)
) -> Response:
    request_data = {
        "mutation_operation_name": "deleteAuthor",
        "operation_args": {"id": item_id},
    }
    body_obj = AuthorMutationRequestBody(**request_data).full_request
    user_info = get_user_info_from_token(auth_result)
    author_router = LibraryRouter(
        f"{SUB_PATH["author"]}{item_id}/", "post", user_info, body_obj
    )
    response = await author_router.send_request()
    return response


@router.get("/books/")
async def book_list(
    form: Optional[LibraryBaseModel] = None,
    query_params: BookQueryParams = Depends(),
    auth_result: Dict[str, Any] = Security(auth_all.verify),
) -> Response:
    request_data = {"operation_args": query_params.model_dump(exclude_none=True)}
    if form:
        request_data |= form.model_dump(include={"requested_fields"})
    body_obj = BookQueryRequestBody(**request_data).full_request
    user_info = get_user_info_from_token(auth_result)
    book_router = LibraryRouter(SUB_PATH["book"], "get", user_info, body_obj)
    response = await book_router.send_request()
    return response


@router.get("/books/{item_id}/")
async def book_details(
    item_id: int,
    form: Optional[LibraryBaseModel] = None,
    auth_result: Dict[str, Any] = Security(auth_all.verify),
) -> Response:
    request_data = {"operation_args": {"id": item_id}}
    if form:
        request_data |= form.model_dump(include={"requested_fields"})
    body_obj = BookQueryRequestBody(**request_data).full_request
    user_info = get_user_info_from_token(auth_result)
    book_router = LibraryRouter(
        f"{SUB_PATH["book"]}{item_id}/", "get", user_info, body_obj
    )
    response = await book_router.send_request()
    return response


@router.post("/books/")
async def create_book(
    form: BookCreateForm, auth_result: Dict[str, Any] = Security(auth_staff.verify)
) -> Response:
    request_data = {
        "mutation_operation_name": "createBook",
        "operation_args": form.model_dump(
            exclude={"requested_fields"}, exclude_none=True
        ),
    } | form.model_dump(include={"requested_fields"})
    body_obj = BookMutationRequestBody(**request_data).full_request
    user_info = get_user_info_from_token(auth_result)
    book_router = LibraryRouter(SUB_PATH["book"], "post", user_info, body_obj)
    response = await book_router.send_request()
    return response


@router.patch("/books/{item_id}/")
async def update_book(
    item_id: int,
    form: BookUpdateForm,
    auth_result: Dict[str, Any] = Security(auth_staff.verify),
) -> Response:
    request_data = {
        "mutation_operation_name": "updateBook",
        "operation_args": {"id": item_id}
        | form.model_dump(exclude={"requested_fields"}, exclude_none=True),
    } | form.model_dump(include={"requested_fields"})
    body_obj = AuthorMutationRequestBody(**request_data).full_request
    user_info = get_user_info_from_token(auth_result)
    book_router = LibraryRouter(
        f"{SUB_PATH["book"]}{item_id}/", "post", user_info, body_obj
    )
    response = await book_router.send_request()
    return response


@router.delete("/books/{item_id}/")
async def delete_book(
    item_id: int, auth_result: Dict[str, Any] = Security(auth_staff.verify)
) -> Response:
    request_data = {
        "mutation_operation_name": "deleteBook",
        "operation_args": {"id": item_id},
    }
    body_obj = BookMutationRequestBody(**request_data).full_request
    user_info = get_user_info_from_token(auth_result)
    book_router = LibraryRouter(
        f"{SUB_PATH["book"]}{item_id}/", "post", user_info, body_obj
    )
    response = await book_router.send_request()
    return response
