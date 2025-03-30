from pydantic import BaseModel, ConfigDict
from typing import Optional

class CategoryBase(BaseModel):
    name: str
    description: Optional[str] = None
    icon_url: Optional[str] = None
    model_config = ConfigDict(from_attributes=True)

class CategoryCreate(CategoryBase):
    pass

class CategoryResponse(CategoryBase):
    id: int