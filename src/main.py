from fastapi import FastAPI

from routers import library

app = FastAPI()

app.include_router(library.router)
# app.include_router(forum.router)
