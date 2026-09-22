from fastapi import FastAPI, status, Response
from router import blogs
from router import users

app = FastAPI()
app.include_router(blogs.router)
app.include_router(users.router)

@app.get('/hello', tags=['hello'])
def index():
    return 'hello world'