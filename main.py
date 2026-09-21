from fastapi import FastAPI, status, Response

app = FastAPI()

@app.get('/hello')
def index():
    return 'hello world'

@app.get('/blog/all')
def get_all_blogs():
    return {'message':'all blogs returned'}

@app.get('/blog/{id}', status_code=status.HTTP_200_OK)
def get_blog(id:int, response: Response):
    if id > 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'error':f'blog {id} not found'}
    else:
        response.status_code = status.HTTP_200_OK
        return {'message':f'blog with id {id}'}

@app.get('/blog-with-params')
# can pass default params
def get_blog_params(page=1, data=10):
    return {'message':f' all {data} on page {page}'}
# we can also combine path and query params in one api