from typing import Optional, List
from fastapi import APIRouter, Query, Body
from fastapi import FastAPI, status, Response, Depends
from pydantic import BaseModel
from router.users import required_functionality

router = APIRouter(
    prefix='/blog',
)

class BlogModel(BaseModel):
    title: str
    content: str
    published: Optional[bool]
    tags: List[str] = []

@router.get('/all', tags=['blogs'], summary='to retrieve all blogs', description='this api is use to get all blogs')
def get_all_blogs(req_parameter: dict = Depends(required_functionality)):
    return {'message':'all blogs returned', 'req': req_parameter}

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

@router.post('/new', tags=['blogs'])
def create_blog(blog: BlogModel):
    return {'data':blog}

@router.post('/new/{id}/comment', tags=['blogs'])
def create_comment(
        blog: BlogModel, 
        id:int,
        comment_id: int = Query(None, alias='commentId', deprecated=True),
        content: str = Body(..., min_length=1,max_length=10)
    ):
    return {'data':blog, 'id':id, 'comment_id':comment_id, 'content': content}