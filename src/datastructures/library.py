from typing import List, Optional

from fastapi import Query
from pydantic import BaseModel, Field


class AuthorQueryParams(BaseModel):
    first_name: Optional[str] = Field(Query(None))
    middle_name: Optional[str] = Field(Query(None))
    last_name: Optional[str] = Field(Query(None))


class BookQueryParams(BaseModel):
    title: Optional[str] = Field(Query(None))
    authors: Optional[List[int]] = Field(Query(None))
    publication_year: Optional[int] = Field(Query(None))
    language: Optional[str] = Field(Query(None))
    category: Optional[str] = Field(Query(None))


class LibraryBaseModel(BaseModel):
    """Required fields can be passed in every request."""

    requested_fields: Optional[List[str]] = None


class AuthorCreateForm(LibraryBaseModel):
    first_name: str
    middle_name: Optional[str] = None
    last_name: str


class AuthorUpdateForm(LibraryBaseModel):
    first_name: Optional[str] = None
    middle_name: Optional[str] = None
    last_name: Optional[str] = None


class BookCreateForm(LibraryBaseModel):
    title: str
    authors: List[int]
    publication_year: int
    language: str
    category: str


class BookUpdateForm(LibraryBaseModel):
    title: Optional[str] = None
    authors: Optional[List[int]] = None
    publication_year: Optional[int] = None
    language: Optional[str] = None
    category: Optional[str] = None
