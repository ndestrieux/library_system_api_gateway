from fastapi import FastAPI

from routers import forum, library

app = FastAPI()

app.include_router(library.router)
app.include_router(forum.router)
