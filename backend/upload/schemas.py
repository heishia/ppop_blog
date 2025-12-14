# Upload Pydantic schemas

from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class UploadBase(BaseModel):
    filename: str = Field(..., description="파일명", max_length=255)
    file_path: str = Field(..., description="파일 경로", max_length=500)
    file_size: int = Field(..., description="파일 크기 (bytes)", ge=0)
    content_type: Optional[str] = Field(None, description="파일 MIME 타입", max_length=100)


class UploadResponse(UploadBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True


class UploadListResponse(BaseModel):
    id: int
    filename: str
    file_size: int
    content_type: Optional[str] = None
    created_at: datetime

    class Config:
        from_attributes = True
