from fastapi import FastAPI, status, Response
from router import blogs
from router import users
from router import articles
from router import files
from auth import authentication
from db import models
from db.database import engine
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.include_router(blogs.router)
app.include_router(files.router)
app.include_router(users.router)
app.include_router(articles.router)
app.include_router(authentication.router)

@app.get('/hello', tags=['hello'])
def index():
    return 'hello world'

models.Base.metadata.create_all(engine)
app.mount('/uploaded_files', StaticFiles(directory="uploaded_files"), name="files")