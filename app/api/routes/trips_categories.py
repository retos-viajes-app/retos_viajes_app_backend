
from fastapi import APIRouter, Depends
from app.auth.auth import verify_access_token
from sqlalchemy.orm import Session
from app.db.db_connection import get_db
from app.schema.trip_category import TripCategoryCreate
from app.db.model.trip_category import TripCategory

router = APIRouter(tags=["trips-categories"])


@router.post("/trips-categories")
def create_trip(tripCategory: TripCategoryCreate, idinfo: dict = Depends(verify_access_token), db: Session = Depends(get_db)):
    new_trip_category = TripCategory(trip_id = tripCategory.trip_id, category_id = tripCategory.category_id)
    db.add(new_trip_category)
    db.commit()
    db.refresh(new_trip_category)
    return {"suceess": "trip category created"}


    


