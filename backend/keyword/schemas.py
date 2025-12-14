# Keyword Pydantic schemas

from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class KeywordBase(BaseModel):
    name: str = Field(..., description="키워드 이름", min_length=1, max_length=100)
    description: Optional[str] = Field(None, description="키워드 설명", max_length=500)


class KeywordCreate(KeywordBase):
    pass


class KeywordUpdate(BaseModel):
    name: Optional[str] = Field(None, description="키워드 이름", min_length=1, max_length=100)
    description: Optional[str] = Field(None, description="키워드 설명", max_length=500)


class KeywordResponse(KeywordBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True
