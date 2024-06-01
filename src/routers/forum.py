from typing import Any, Dict

from fastapi import APIRouter, Depends, Security

from datastructures.forum import (
    PostCreateForm,
    PostUpdateForm,
    TopicCreateForm,
    TopicQueryParams,
    TopicUpdateForm,
)
from dependencies.gateway_routers import ForumRouter
from dependencies.utils import get_user_id_from_token
from params import auth_all

router = APIRouter(prefix="/api/forum", tags=["forum"])


@router.get("/topics/")
async def topic_list(
    query_params: TopicQueryParams = Depends(),
    auth_result: Dict[str, Any] = Security(auth_all.verify),
):
    user_id = get_user_id_from_token(auth_result)
    topic_router = ForumRouter(
        "/topics/",
        "get",
        user_id,
        query_params=query_params.model_dump(exclude_none=True),
    )
    response = await topic_router.send_request()
    return response.json()


@router.get("/topics/{item_id}/")
async def topic_details(
    item_id: int, auth_result: Dict[str, Any] = Security(auth_all.verify)
):
    user_id = get_user_id_from_token(auth_result)
    topic_router = ForumRouter(f"/topics/{user_id}/", "get", user_id)
    response = await topic_router.send_request()
    return response.json()


@router.post("/topics/")
async def create_topic(
    form: TopicCreateForm, auth_result: Dict[str, Any] = Security(auth_all.verify)
):
    user_id = get_user_id_from_token(auth_result)
    topic_router = ForumRouter(
        "/topics/", "post", user_id, body=form.model_dump(exclude_none=True)
    )
    response = await topic_router.send_request()
    return response.json()


@router.patch("/topics/{item_id}/")
async def update_topic(
    item_id: int,
    form: TopicUpdateForm,
    auth_result: Dict[str, Any] = Security(auth_all.verify),
):
    user_id = get_user_id_from_token(auth_result)
    topic_router = ForumRouter(
        f"/topics/{item_id}/", "patch", user_id, body=form.model_dump(exclude_none=True)
    )
    response = await topic_router.send_request()
    return response.json()


@router.delete("/topics/{item_id}/")
async def delete_topic(
    item_id: int, auth_result: Dict[str, Any] = Security(auth_all.verify)
):
    user_id = get_user_id_from_token(auth_result)
    topic_router = ForumRouter(f"/topics/{item_id}/", "delete", user_id)
    response = await topic_router.send_request()
    return response.json()


@router.get("/posts/{item_id}/")
async def post_details(
    item_id: int, auth_result: Dict[str, Any] = Security(auth_all.verify)
):
    user_id = get_user_id_from_token(auth_result)
    forum_router = ForumRouter(f"/posts/{item_id}/", "get", user_id)
    response = await forum_router.send_request()
    return response.json()


@router.post("/posts/")
async def create_post(
    form: PostCreateForm, auth_result: Dict[str, Any] = Security(auth_all.verify)
):
    user_id = get_user_id_from_token(auth_result)
    forum_router = ForumRouter(
        "/posts/", "post", user_id, body=form.model_dump(exclude_none=True)
    )
    response = await forum_router.send_request()
    return response.json()


@router.patch("/posts/{item_id}/")
async def update_post(
    item_id: int,
    form: PostUpdateForm,
    auth_result: Dict[str, Any] = Security(auth_all.verify),
):
    user_id = get_user_id_from_token(auth_result)
    forum_router = ForumRouter(
        f"/posts/{item_id}/", "patch", user_id, body=form.model_dump(exclude_none=True)
    )
    response = await forum_router.send_request()
    return response.json()


@router.delete("/posts/{item_id}/")
async def delete_post(
    item_id: int, auth_result: Dict[str, Any] = Security(auth_all.verify)
):
    user_id = get_user_id_from_token(auth_result)
    forum_router = ForumRouter(f"/posts/{item_id}/", "delete", user_id)
    response = await forum_router.send_request()
    return response.json()
