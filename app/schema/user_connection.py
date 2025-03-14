
from datetime import datetime
from pydantic import BaseModel


class UserConnectionBase(BaseModel):
    user_id_1: int
    user_id_2: int
    status: str  # Puede ser 'pending', 'accepted', o 'rejected'

    class Config:
        orm_mode = True

class UserConnectionResponse(UserConnectionBase):
    created_at: datetime
    class Config:
        orm_mode = True