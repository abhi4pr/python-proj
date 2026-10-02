from fastapi import APIRouter, Depends, HTTPException
from fastapi import FastAPI, status, Response
from sqlalchemy.orm.session import Session
from schemas import UserBase, UserDisplay
from db.models import Dbuser
from db.hash import Hash
from db.database import get_db
from typing import List

router = APIRouter(
    prefix='/user',
)

@router.post('/new', response_model=UserDisplay, tags=['users'])
def create_user(request: UserBase, db: Session = Depends(get_db)):
    new_user = Dbuser(
        username = request.username,
        email = request.email,
        password = Hash.bcrypt(request.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get('/get_all_users', response_model=List[UserDisplay], tags=['users'])
def get_all_users(db: Session = Depends(get_db)):
    return db.query(Dbuser).all()

@router.get('/get_user/{id}', response_model=UserDisplay, tags=['users'])
def get_user(id: int, db: Session = Depends(get_db)):
    return db.query(Dbuser).filter(Dbuser.id == id).first()

@router.post('/update/{id}', tags=['users'])
def update_user(id: int, request: UserBase, db: Session = Depends(get_db)):
    user = db.query(Dbuser).filter(Dbuser.id == id)
    if not user.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'User with id {id} not found'
        )
    user.update({
        Dbuser.username: request.username,
        Dbuser.email: request.email,
        Dbuser.password: Hash.bcrypt(request.password)
    })
    db.commit()
    return {'message': f'User with id {id} updated'}

@router.delete('/delete/{id}', tags=['users'])
def delete_user(id: int, db: Session = Depends(get_db)):
    user = db.query(Dbuser).filter(Dbuser.id == id)
    if not user.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'User with id {id} not found'
        )
    user.delete(synchronize_session=False)
    db.commit()
    return {'message': f'User with id {id} deleted'}

def required_functionality():
    return{ 'message': 'this is required functionality'}