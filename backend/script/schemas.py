# Script Pydantic schemas

from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class ScriptBase(BaseModel):
    title: str = Field(..., description="스크립트 제목", min_length=1, max_length=200)
    content: str = Field(..., description="스크립트 내용", min_length=1)
    description: Optional[str] = Field(None, description="스크립트 설명", max_length=1000)


class ScriptCreate(ScriptBase):
    pass


class ScriptUpdate(BaseModel):
    title: Optional[str] = Field(None, description="스크립트 제목", min_length=1, max_length=200)
    content: Optional[str] = Field(None, description="스크립트 내용", min_length=1)
    description: Optional[str] = Field(None, description="스크립트 설명", max_length=1000)


class ScriptResponse(ScriptBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True
