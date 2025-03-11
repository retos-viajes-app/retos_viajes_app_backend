from pydantic import BaseModel
from typing import Optional

class CategoryBase(BaseModel):
    name: str
    description: str
    icon_url: Optional[str]

class CategoryCreate(CategoryBase):
    pass

class CategoryResponse(CategoryBase):
    id: int

    class Config:
        orm_mode = True