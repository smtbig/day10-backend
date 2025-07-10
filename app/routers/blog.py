from fastapi import APIRouter, Depends
from typing import List
from sqlalchemy.orm import Session
from app import crud, schemas
from app.database import SessionLocal

router = APIRouter(prefix="/blog", tags=["BlogPosts"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.BlogPostOut)
def create(post: schemas.BlogPostCreate, db: Session = Depends(get_db)):
    return crud.create_post(db, post)

@router.get("/", response_model=List[schemas.BlogPostOut])
def read(db: Session = Depends(get_db)):
    return crud.get_posts(db)
