from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app import models

router = APIRouter(
    prefix="/authors",
    tags=["Authors"]
)

@router.post("/")
def create_author(name: str, email: str | None = None, db: Session = Depends(get_db)):
    author = models.Author(name=name, email=email)
    db.add(author)
    db.commit()
    db.refresh(author)
    return author

@router.get("/")
def get_authors(db: Session = Depends(get_db)):
    return db.query(models.Author).all()

@router.get("/{author_id}")
def get_author(author_id: int, db: Session = Depends(get_db)):
    author = db.query(models.Author).filter(models.Author.id == author_id).first()
    if not author:
        raise HTTPException(status_code=404, detail="Author not found")
    return author

@router.get("/{author_id}/posts")
def get_author_posts(author_id: int, db: Session = Depends(get_db)):
    author = db.query(models.Author).filter(models.Author.id == author_id).first()
    if not author:
        raise HTTPException(status_code=404, detail="Author not found")

    return author.posts

