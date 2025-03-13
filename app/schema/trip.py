from pydantic import BaseModel
from datetime import datetime
#Para manejar el inicio propi

class CreateTrip(BaseModel):
    user_id: int 
    destination_id: int 
    start_date: datetime
    end_date: datetime
    status: str = "pending"
