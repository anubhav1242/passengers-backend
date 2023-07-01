from fastapi import FastAPI, Form, File, UploadFile
import models
from routes import router
from config import engine
from typing import Annotated

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router, prefix="/passengers", tags=["passengers"])

