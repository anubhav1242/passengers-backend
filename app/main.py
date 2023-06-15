from fastapi import FastAPI, Form, File, UploadFile
from . import models
from .routes import router
from .config import engine
from typing import Annotated

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router, prefix="/passengers", tags=["passengers"])

@app.post("/login")
async def login(username: Annotated[str, Form()], password: Annotated[str, Form()]):
    return {"username": username}


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile | None = None):
    if not file:
        return{"message": "No file sent"}
    else:
        return{"filename": file.filename} 
        