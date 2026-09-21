from fastapi import FastAPI

app = FastAPI()

@app.get('/hello')
def index():
    return 'hello world'

@app.get('/blog/all')
def get_all_blogs():
    return {'message':'all blogs returned'}

@app.get('/blog/{id}')
def get_blog(id:int):
    return {'message':f'blog with id {id}'}

@app.get('/blog-with-params')
# can pass default params
def get_blog_params(page=1, data=10):
    return {'message':f' all {data} on page {page}'}
