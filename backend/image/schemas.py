# Image Pydantic schemas

from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class ImageBase(BaseModel):
    url: str = Field(..., description="이미지 URL", max_length=500)
    alt_text: Optional[str] = Field(None, description="이미지 대체 텍스트", max_length=200)
    width: Optional[int] = Field(None, description="이미지 너비", ge=0)
    height: Optional[int] = Field(None, description="이미지 높이", ge=0)


class ImageCreate(ImageBase):
    pass


class ImageUpdate(BaseModel):
    url: Optional[str] = Field(None, description="이미지 URL", max_length=500)
    alt_text: Optional[str] = Field(None, description="이미지 대체 텍스트", max_length=200)
    width: Optional[int] = Field(None, description="이미지 너비", ge=0)
    height: Optional[int] = Field(None, description="이미지 높이", ge=0)


class ImageResponse(ImageBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True
