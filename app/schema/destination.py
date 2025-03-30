from pydantic import BaseModel
from typing import Optional

class DestinationBase(BaseModel):
    city: str
    country: str
    description: Optional[str] = None
    image_url: Optional[str] = None
    active: Optional[bool] = None

class DestinationCreate(DestinationBase):
    pass

class DestinationResponse(DestinationBase):
    id: int

