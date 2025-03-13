from pydantic import BaseModel
from datetime import datetime
#Para manejar el inicio propi

class CreateTrip(BaseModel):
    user_id: int 
    destination_id: int 
    start_date: datetime
    end_date: datetime
    status: str = "pending"

class UpdateTrip(BaseModel):
    user_id: int = None
    destination_id: int = None
    start_date: datetime = None
    end_date: datetime = None
    status: str = None  