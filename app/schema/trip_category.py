from pydantic import BaseModel, EmailStr, Field

class TripCategoryCreate(BaseModel):
    trip_id: int
    category_id: int