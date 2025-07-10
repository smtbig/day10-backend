from pydantic import BaseModel, EmailStr
from typing import Optional, List

# --- User ---
class UserBase(BaseModel):
    username: str
    email: EmailStr

class UserCreate(UserBase):
    pass

class UserOut(UserBase):
    id: int
    class Config:
        orm_mode = True

# --- Task ---
class TaskBase(BaseModel):
    title: str

class TaskCreate(TaskBase):
    user_id: int

class TaskOut(TaskBase):
    id: int
    is_complete: bool
    user_id: int
    class Config:
        orm_mode = True

# --- BlogPost ---
class BlogPostBase(BaseModel):
    title: str
    content: Optional[str] = None

class BlogPostCreate(BlogPostBase):
    user_id: int

class BlogPostOut(BlogPostBase):
    id: int
    user_id: int
    class Config:
        orm_mode = True
