
from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, ConfigDict

from app.schema.user import UserResponse

class UserConnectionRequest(BaseModel):
    user_id_1: int
    user_id_2: int

class UserConnectionBase(BaseModel):
    user_id_1: int
    user_id_2: int
    status: str  # Puede ser 'pending', 'accepted', o 'rejected'
    model_config = ConfigDict(from_attributes=True)

class UserConnectionResponse(UserConnectionBase):
    created_at: Optional[datetime] = None

class PaginationInfo(BaseModel):
    page: int
    per_page: int
    has_more: bool

class UsersSuggestedResponse(BaseModel):
    users: List[UserResponse]
    pagination: PaginationInfo
    