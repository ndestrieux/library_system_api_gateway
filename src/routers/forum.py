from typing import Any, Dict

from fastapi import APIRouter, Depends, Security

from datastructures.forum import (
    PostCreateForm,
    PostUpdateForm,
    TopicCreateForm,
    TopicQueryParams,
    TopicUpdateForm,
)
from router_params import SUB_PATH, auth_all
from utils.gateway_routers import ForumRouter
from utils.general import get_user_info_from_token

router = APIRouter(prefix="/api/forum", tags=["forum"])


@router.get("/topics/")
async def topic_list(
    query_params: TopicQueryParams = Depends(),
    auth_result: Dict[str, Any] = Security(auth_all.verify),
):
    user_info = get_user_info_from_token(auth_result)
    topic_router = ForumRouter(
        SUB_PATH["topic"],
        "get",
        user_info,
        query_params=query_params.model_dump(exclude_none=True),
    )
    response = await topic_router.send_request()
    return response


@router.get("/topics/{item_id}/")
async def topic_details(
    item_id: int, auth_result: Dict[str, Any] = Security(auth_all.verify)
):
    user_info = get_user_info_from_token(auth_result)
    topic_router = ForumRouter(f"{SUB_PATH["topic"]}{user_info}/", "get", user_info)
    response = await topic_router.send_request()
    return response


@router.post("/topics/")
async def create_topic(
    form: TopicCreateForm, auth_result: Dict[str, Any] = Security(auth_all.verify)
):
    user_info = get_user_info_from_token(auth_result)
    topic_router = ForumRouter(
        SUB_PATH["topic"], "post", user_info, body=form.model_dump(exclude_none=True)
    )
    response = await topic_router.send_request()
    return response


@router.patch("/topics/{item_id}/")
async def update_topic(
    item_id: int,
    form: TopicUpdateForm,
    auth_result: Dict[str, Any] = Security(auth_all.verify),
):
    user_info = get_user_info_from_token(auth_result)
    topic_router = ForumRouter(
        f"{SUB_PATH["topic"]}{item_id}/",
        "patch",
        user_info,
        body=form.model_dump(exclude_none=True),
    )
    response = await topic_router.send_request()
    return response


@router.delete("/topics/{item_id}/")
async def delete_topic(
    item_id: int, auth_result: Dict[str, Any] = Security(auth_all.verify)
):
    user_info = get_user_info_from_token(auth_result)
    topic_router = ForumRouter(f"{SUB_PATH["topic"]}{item_id}/", "delete", user_info)
    response = await topic_router.send_request()
    return response


@router.get("/posts/{item_id}/")
async def post_details(
    item_id: int, auth_result: Dict[str, Any] = Security(auth_all.verify)
):
    user_info = get_user_info_from_token(auth_result)
    forum_router = ForumRouter(f"{SUB_PATH["post"]}{item_id}/", "get", user_info)
    response = await forum_router.send_request()
    return response


@router.post("/posts/")
async def create_post(
    form: PostCreateForm, auth_result: Dict[str, Any] = Security(auth_all.verify)
):
    user_info = get_user_info_from_token(auth_result)
    forum_router = ForumRouter(
        SUB_PATH["post"], "post", user_info, body=form.model_dump(exclude_none=True)
    )
    response = await forum_router.send_request()
    return response


@router.patch("/posts/{item_id}/")
async def update_post(
    item_id: int,
    form: PostUpdateForm,
    auth_result: Dict[str, Any] = Security(auth_all.verify),
):
    user_info = get_user_info_from_token(auth_result)
    forum_router = ForumRouter(
        f"{SUB_PATH["post"]}{item_id}/",
        "patch",
        user_info,
        body=form.model_dump(exclude_none=True),
    )
    response = await forum_router.send_request()
    return response


@router.delete("/posts/{item_id}/")
async def delete_post(
    item_id: int, auth_result: Dict[str, Any] = Security(auth_all.verify)
):
    user_info = get_user_info_from_token(auth_result)
    forum_router = ForumRouter(f"{SUB_PATH["post"]}{item_id}/", "delete", user_info)
    response = await forum_router.send_request()
    return response
