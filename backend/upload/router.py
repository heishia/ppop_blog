# Upload API router

from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from typing import List
from core.logger import logger
from core.exceptions import CustomException
from .schemas import UploadResponse, UploadListResponse
from .service import UploadService, get_upload_service

router = APIRouter(prefix="/api/uploads", tags=["uploads"])


@router.post("/", response_model=UploadResponse)
def upload_file(
    file: UploadFile = File(...),
    service: UploadService = Depends(get_upload_service)
) -> UploadResponse:
    """파일을 업로드합니다."""
    try:
        logger.info(f"Uploading file: {file.filename}")
        upload_result = service.upload_file(file)
        return upload_result
    except CustomException as e:
        logger.error(f"Error uploading file: {e}")
        raise HTTPException(status_code=e.status_code, detail=str(e))


@router.get("/", response_model=List[UploadListResponse])
def get_uploads(
    skip: int = 0,
    limit: int = 100,
    service: UploadService = Depends(get_upload_service)
) -> List[UploadListResponse]:
    """업로드된 파일 목록을 조회합니다."""
    try:
        logger.info(f"Fetching uploads: skip={skip}, limit={limit}")
        uploads = service.get_uploads(skip=skip, limit=limit)
        return uploads
    except CustomException as e:
        logger.error(f"Error fetching uploads: {e}")
        raise HTTPException(status_code=e.status_code, detail=str(e))


@router.get("/{upload_id}", response_model=UploadResponse)
def get_upload(
    upload_id: int,
    service: UploadService = Depends(get_upload_service)
) -> UploadResponse:
    """특정 업로드 파일을 조회합니다."""
    try:
        logger.info(f"Fetching upload: id={upload_id}")
        upload = service.get_upload_by_id(upload_id)
        if not upload:
            raise HTTPException(status_code=404, detail="Upload not found")
        return upload
    except CustomException as e:
        logger.error(f"Error fetching upload: {e}")
        raise HTTPException(status_code=e.status_code, detail=str(e))


@router.delete("/{upload_id}")
def delete_upload(
    upload_id: int,
    service: UploadService = Depends(get_upload_service)
) -> dict[str, str]:
    """업로드된 파일을 삭제합니다."""
    try:
        logger.info(f"Deleting upload: id={upload_id}")
        success = service.delete_upload(upload_id)
        if not success:
            raise HTTPException(status_code=404, detail="Upload not found")
        return {"message": "Upload deleted successfully"}
    except CustomException as e:
        logger.error(f"Error deleting upload: {e}")
        raise HTTPException(status_code=e.status_code, detail=str(e))
