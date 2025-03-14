from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from app.db.model.category import Category
from app.db.db_connection import get_db
from fastapi import APIRouter
from app.auth.auth import verify_access_token

router = APIRouter(tags=["categories"])


@router.get("/categories")
def get_categories( idinfo: dict = Depends(verify_access_token),db: Session = Depends(get_db)):
    categories_db = db.query(Category).all()

    return categories_db