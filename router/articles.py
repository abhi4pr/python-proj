from fastapi import APIRouter, Depends, HTTPException
from fastapi import FastAPI, status, Response
from sqlalchemy.orm.session import Session
from schemas import ArticleBase, ArticleDisplay
from db.models import DbArticles
from db.hash import Hash
from db.database import get_db
from typing import List

router = APIRouter(
    prefix='/article',
)

@router.post('/new', response_model=ArticleDisplay, tags=['articles'])
def create_article(request: ArticleBase, db: Session = Depends(get_db)):
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
def get_article(id: int, db: Session = Depends(get_db)):
    return db.query(DbArticles).filter(DbArticles.id == id).first()
