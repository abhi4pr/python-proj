from fastapi import APIRouter
from fastapi import FastAPI, status, Response

router = APIRouter(
    prefix='/blog',
)

@router.get('/all', tags=['blogs'], summary='to retrieve all blogs', description='this api is use to get all blogs')
def get_all_blogs():
    return {'message':'all blogs returned'}

@router.get('/{id}', status_code=status.HTTP_200_OK, tags=['blogs'])
def get_blog(id:int, response: Response):
    if id > 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'error':f'blog {id} not found'}
    else:
        response.status_code = status.HTTP_200_OK
        return {'message':f'blog with id {id}'}

@router.get('/params', tags=['blogs'])
# can pass default params
def get_blog_params(page=1, data=10):
    return {'message':f' all {data} on page {page}'}