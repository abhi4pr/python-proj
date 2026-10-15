from fastapi import APIRouter, Depends, HTTPException
from fastapi import FastAPI, status, Response
from sqlalchemy.orm.session import Session
from schemas import ArticleBase, ArticleDisplay, UserBase
from db.models import DbArticles
from db.hash import Hash
from db.database import get_db
from typing import List
from auth.oauth2 import get_current_user

router = APIRouter(
    prefix='/article',
)

@router.post('/new', response_model=ArticleDisplay, tags=['articles'])
def create_article(request: ArticleBase, db: Session = Depends(get_db), current_user: UserBase = Depends(get_current_user)):
    new_article = DbArticles(
        title = request.title,
        content = request.content,
        published = request.published,
        user_id = request.creator_id
    )
    db.add(new_article)
    db.commit()
    db.refresh(new_article)
    return new_article

@router.get('/get_article/{id}', response_model=ArticleDisplay, tags=['articles'])
def get_article(id: int, db: Session = Depends(get_db), current_user: UserBase = Depends(get_current_user)):
    article = db.query(DbArticles).filter(DbArticles.id == id).first()
    if not article:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail=f'article not found with id {id}')
    return article