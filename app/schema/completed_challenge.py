
from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel
from app.schema.pagination_info import PaginationInfo
from app.schema.user import UserResponse
from app.schema.challenge import ChallengeResponse


class CompletedChallengeResponse(BaseModel):
    id: int
    user: UserResponse
    challenge: ChallengeResponse
    trip_id: Optional[int] = None
    completed_at: datetime
    proof_photo_url: Optional[str] = None
    description: Optional[str] = None

class CompletedChallengesSuggestedResponse(BaseModel):
    completed_challenges: List[CompletedChallengeResponse]
    pagination: PaginationInfo