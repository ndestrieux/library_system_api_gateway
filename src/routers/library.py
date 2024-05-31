from typing import Any, Dict, Optional

from fastapi import APIRouter, Depends, Security
from fastapi.responses import JSONResponse

from datastructures.library import (
    AuthorCreateForm,
    AuthorQueryParams,
    AuthorUpdateForm,
    BookCreateForm,
    BookQueryParams,
    BookUpdateForm,
    LibraryBaseModel,
)
from dependencies.gateway_routers import LibraryRouter
from dependencies.graphql.request_body_builders import (
    AuthorMutationRequestBody,
    AuthorQueryRequestBody,
    BookMutationRequestBody,
    BookQueryRequestBody,
)
from dependencies.utils import get_user_id_from_token
from params import auth_all, auth_staff

router = APIRouter(prefix="/api/library", tags=["library"])

AUTHOR_PATH = "/authors/"
BOOK_PATH = "/books/"


@router.get("/authors/")
async def author_list(
    form: Optional[LibraryBaseModel] = None,
    query_params: AuthorQueryParams = Depends(),
    auth_result: Dict[str, Any] = Security(auth_all.verify),
):
    request_data = {"operation_args": query_params.model_dump(exclude_none=True)}
    if form:
        request_data |= form.model_dump(include={"requested_fields"})
    body_obj = AuthorQueryRequestBody(**request_data)
    user_id = get_user_id_from_token(auth_result)
    author_router = LibraryRouter(AUTHOR_PATH, "get", user_id, body_obj)
    response = await author_router.send_request()
    return JSONResponse(content=response.json())


@router.get("/authors/{item_id}/")
async def author_details(
    item_id: int,
    form: Optional[LibraryBaseModel] = None,
    auth_result: Dict[str, Any] = Security(auth_all.verify),
):
    request_data = {"operation_args": {"id": item_id}}
    if form:
        request_data |= form.model_dump(include={"requested_fields"})
    body_obj = AuthorQueryRequestBody(**request_data)
    user_id = get_user_id_from_token(auth_result)
    author_router = LibraryRouter(AUTHOR_PATH, "get", user_id, body_obj)
    response = await author_router.send_request()
    return response.json()


@router.post("/authors/")
async def create_author(
    form: AuthorCreateForm, auth_result: Dict[str, Any] = Security(auth_staff.verify)
):
    request_data = {
        "mutation_operation_name": "createAuthor",
        "operation_args": form.model_dump(
            exclude={"requested_fields"}, exclude_none=True
        ),
    } | form.model_dump(include={"requested_fields"})
    body_obj = AuthorMutationRequestBody(**request_data)
    user_id = get_user_id_from_token(auth_result)
    author_router = LibraryRouter(AUTHOR_PATH, "post", user_id, body_obj)
    response = await author_router.send_request()
    return response.json()


@router.patch("/authors/{item_id}/")
async def update_author(
    item_id: int,
    form: AuthorUpdateForm,
    auth_result: Dict[str, Any] = Security(auth_staff.verify),
):
    request_data = {
        "mutation_operation_name": "updateAuthor",
        "operation_args": {"id": item_id}
        | form.model_dump(exclude={"requested_fields"}, exclude_none=True),
    } | form.model_dump(include={"requested_fields"})
    body_obj = AuthorMutationRequestBody(**request_data)
    user_id = get_user_id_from_token(auth_result)
    author_router = LibraryRouter(AUTHOR_PATH, "post", user_id, body_obj)
    response = await author_router.send_request()
    return response.json()


@router.delete("/authors/{item_id}/")
async def delete_author(
    item_id: int, auth_result: Dict[str, Any] = Security(auth_staff.verify)
):
    request_data = {
        "mutation_operation_name": "deleteAuthor",
        "operation_args": {"id": item_id},
    }
    body_obj = AuthorMutationRequestBody(**request_data)
    user_id = get_user_id_from_token(auth_result)
    author_router = LibraryRouter(AUTHOR_PATH, "post", user_id, body_obj)
    response = await author_router.send_request()
    return response.json()


@router.get("/books/")
async def book_list(
    form: Optional[LibraryBaseModel] = None,
    query_params: BookQueryParams = Depends(),
    auth_result: Dict[str, Any] = Security(auth_all.verify),
):
    request_data = {"operation_args": query_params.model_dump(exclude_none=True)}
    if form:
        request_data |= form.model_dump(include={"requested_fields"})
    body_obj = BookQueryRequestBody(**request_data)
    user_id = get_user_id_from_token(auth_result)
    book_router = LibraryRouter(BOOK_PATH, "get", user_id, body_obj)
    response = await book_router.send_request()
    return response.json()


@router.get("/books/{item_id}/")
async def book_details(
    item_id: int,
    form: Optional[LibraryBaseModel] = None,
    auth_result: Dict[str, Any] = Security(auth_all.verify),
):
    request_data = {"operation_args": {"id": item_id}}
    if form:
        request_data |= form.model_dump(include={"requested_fields"})
    body_obj = BookQueryRequestBody(**request_data)
    user_id = get_user_id_from_token(auth_result)
    book_router = LibraryRouter(BOOK_PATH, "get", user_id, body_obj)
    response = await book_router.send_request()
    return response.json()


@router.post("/books/")
async def create_book(
    form: BookCreateForm, auth_result: Dict[str, Any] = Security(auth_staff.verify)
):
    request_data = {
        "mutation_operation_name": "createBook",
        "operation_args": form.model_dump(
            exclude={"requested_fields"}, exclude_none=True
        ),
    } | form.model_dump(include={"requested_fields"})
    body_obj = BookMutationRequestBody(**request_data)
    user_id = get_user_id_from_token(auth_result)
    book_router = LibraryRouter(BOOK_PATH, "post", user_id, body_obj)
    response = await book_router.send_request()
    return response.json()


@router.patch("/books/{item_id}/")
async def update_book(
    item_id: int,
    form: BookUpdateForm,
    auth_result: Dict[str, Any] = Security(auth_staff.verify),
):
    request_data = {
        "mutation_operation_name": "updateBook",
        "operation_args": {"id": item_id}
        | form.model_dump(exclude={"requested_fields"}, exclude_none=True),
    } | form.model_dump(include={"requested_fields"})
    body_obj = AuthorMutationRequestBody(**request_data)
    user_id = get_user_id_from_token(auth_result)
    book_router = LibraryRouter(BOOK_PATH, "post", user_id, body_obj)
    response = await book_router.send_request()
    return response.json()


@router.delete("/books/{item_id}/")
async def delete_book(
    item_id: int, auth_result: Dict[str, Any] = Security(auth_staff.verify)
):
    request_data = {
        "mutation_operation_name": "deleteBook",
        "operation_args": {"id": item_id},
    }
    body_obj = BookMutationRequestBody(**request_data)
    user_id = get_user_id_from_token(auth_result)
    book_router = LibraryRouter(BOOK_PATH, "post", user_id, body_obj)
    response = await book_router.send_request()
    return response.json()
