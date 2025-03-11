from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from app.db.model.category import Category
from app.db.db_connection import get_db
from fastapi import APIRouter

from backend.app.schema.category import CategoryCreate

router = APIRouter(tags=["categories"])


@router.post("/categories/", response_model=CategoryCreate)
def create_category(category: CategoryCreate, db: Session = Depends(get_db)):
    db_category = Category(**category.dict())  # Convierte los datos Pydantic a un diccionario
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category