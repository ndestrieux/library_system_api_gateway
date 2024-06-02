from typing import Optional

from fastapi import Query
from pydantic import BaseModel, Field


class TopicQueryParams(BaseModel):
    title: Optional[str] = Field(Query(None))
    category: Optional[str] = Field(Query(None))


class TopicCreateForm(BaseModel):
    title: str
    description: Optional[str] = None
    category: str


class TopicUpdateForm(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    category: Optional[str] = None


class PostCreateForm(BaseModel):
    content: str
    topic: int


class PostUpdateForm(BaseModel):
    content: Optional[str] = None
    topic: Optional[int] = None
