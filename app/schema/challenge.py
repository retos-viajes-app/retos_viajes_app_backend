from typing import Optional
from pydantic import BaseModel
from app.schema.category import CategoryResponse
from app.schema.destination import DestinationResponse


class ChallengeResponse(BaseModel):
    id: int
    category: CategoryResponse
    destination: DestinationResponse
    title: str
    short_description: Optional[str] = None
    long_description: Optional[str] = None
    image_url: Optional[str] = None
    points: Optional[int] = None
    difficulty: Optional[int] = None
    active: Optional[bool] = None