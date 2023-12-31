from typing import Optional
from pydantic import BaseModel,Field


class CreateUser(BaseModel):
    name: str = Field(min_length=1, max_length=30)
    profession: str = Field(min_length=1, max_length=30)
    phone : str
    imageUrl: str
    created_at : str
    updated_at : str
    isActive: Optional[bool] = False