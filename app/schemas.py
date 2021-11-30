from pydantic import BaseModel, EmailStr, conint
from datetime import datetime
from typing import Optional

# User data validation schemas
# Use inheritance to avoid code duplication i.e. "PostBase"


class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class PostBase(BaseModel):
    """
    Schemas validates the data sent to match requirements
    Some fields can have default values, then users don't have to specify them
    """
    title: str
    content: str
    is_published: bool = True


class PostCreate(PostBase):
    pass


# Response schemas
class UserResponse(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        orm_mode = True


class PostResponse(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserResponse

    class Config:
        orm_mode = True


# Token Schemas
class Token(BaseModel):
    access_token = str
    token_type = str


class TokenData(BaseModel):
    id: Optional[str] = None


# Vote schemas
class Vote(BaseModel):
    post_id: int
    dir: conint(le=1)


class PostVotes(BaseModel):
    Post: PostResponse
    votes: int

    class Config:
        orm_mode = True
