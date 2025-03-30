from pydantic import BaseModel


class PaginationInfo(BaseModel):
    page: int
    per_page: int
    has_more: bool