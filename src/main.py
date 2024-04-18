from fastapi import FastAPI, Security

from auth import VerifyToken

app = FastAPI()
auth = VerifyToken()


@app.get("/api/private")
def private(auth_result: str = Security(auth.verify)):
    return auth_result
