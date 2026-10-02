from fastapi import FastAPI, status, Response
from router import blogs
from router import users
from db import models
from db.database import engine

app = FastAPI()
app.include_router(blogs.router)
app.include_router(users.router)

@app.get('/hello', tags=['hello'])
def index():
    return 'hello world'

models.Base.metadata.create_all(engine)