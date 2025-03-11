
from fastapi import APIRouter, Depends, HTTPException
from app.auth.auth import verify_access_token
from app.schema.trip import CreateTrip, UpdateTrip
from app.db.model.trip import Trip
from sqlalchemy.orm import Session
from app.db.db_connection import get_db

router = APIRouter(tags=["trips"])


@router.post("/trips")
def create_trip(trip: CreateTrip, user: dict = Depends(verify_access_token), db: Session = Depends(get_db)):
    new_trip = Trip(destination_id = trip.destination_id, user_id = trip.user_id, start_date = trip.start_date, end_date = trip.end_date, status = trip.status)
    db.add(new_trip)
    db.commit()
    db.refresh(new_trip)
    return {"id_viaje": new_trip.id}

@router.put("/trips/{trip_id}")
def update_trip(trip_id: int,trip: UpdateTrip, user: dict = Depends(verify_access_token), db: Session = Depends(get_db)):
    db_trip = db.query(Trip).filter(Trip.id == trip_id).first()

    if db_trip is None:
        raise HTTPException(status_code=404, detail="El viaje no existe")
    #Dependiendo de si está o no lo añado
    for key, value in dict(trip).items():
        if value is not None:
         setattr(db_trip, key, value)

    db.commit()
    return {"message": "viaje actualizado correctamente"}

@router.delete("/trips/{trip_id}")
def delete_trip(trip_id: int, user: dict = Depends(verify_access_token), db: Session = Depends(get_db)):
    db_trip = db.query(Trip).filter(Trip.id == trip_id).first()

    if db_trip is None:
        raise HTTPException(status_code=404, detail="El viaje no existe")

    db.delete(db_trip)
    db.commit()
    return {"message": "viaje eliminado correctamente"}
    


