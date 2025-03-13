
from fastapi import APIRouter, Depends, HTTPException
from app.auth.auth import verify_access_token
#from app.schema.trip import CreateTrip, UpdateTrip
from app.db.model.destination import Destination
from sqlalchemy.orm import Session
from app.db.db_connection import get_db

router = APIRouter(tags=["destinations"])



@router.get("/destinations")
def get_destinations( user: dict = Depends(verify_access_token), db: Session = Depends(get_db)):
    db_destinations = db.query(Destination).all()

    if db_destinations is None:
        raise HTTPException(status_code=404, detail="No hay destinos disponibles")
    #Dependiendo de si está o no lo añado

    destinations = [
        {
        'id': db_destination.id, 
        'city': db_destination.city, 
        'country': db_destination.country,
        'description': db_destination.description,
        'image_url': db_destination.image_url} for db_destination in db_destinations
    ]
    return destinations

    


