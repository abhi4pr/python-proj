from pydantic import BaseModel
from typing import List

class Article(BaseModel):
    title: str
    content: str
    published: bool
    model_config = {"from_attributes": True}
class UserBase(BaseModel):
    username: str
    email: str
    password: str

#user inside articles
class User(BaseModel):
    id: int
    username: str
    model_config = {"from_attributes": True}
class UserDisplay(BaseModel):
    username: str
    email: str
    items: List[Article] = []
    model_config = {"from_attributes": True}

class ArticleBase(BaseModel):
    title: str
    content: str
    published: bool
    creator_id: int

class ArticleDisplay(BaseModel):
    title: str
    content: str
    published: bool
    user: User
    model_config = {"from_attributes": True}