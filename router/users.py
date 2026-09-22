from fastapi import APIRouter
from fastapi import FastAPI, status, Response

router = APIRouter(
    prefix='/user',
)

@router.get('/all', tags=['users'], summary='to retrieve all users', description='this api is use to get all users')
def get_all_users():
    return {'message':'all users returned'}

@router.get('/{id}', status_code=status.HTTP_200_OK, tags=['users'])
def get_user(id:int, response: Response):
    if id > 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'error':f'user {id} not found'}
    else:
        response.status_code = status.HTTP_200_OK
        return {'message':f'user with id {id}'}
