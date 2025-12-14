# Image API router

from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from typing import List
from core.logger import logger
from core.exceptions import CustomException
from .schemas import ImageCreate, ImageResponse, ImageUpdate
from .service import ImageService, get_image_service

router = APIRouter(prefix="/api/images", tags=["images"])


@router.post("/", response_model=ImageResponse)
def upload_image(
    file: UploadFile = File(...),
    service: ImageService = Depends(get_image_service)
) -> ImageResponse:
    """이미지를 업로드합니다."""
    try:
        logger.info(f"Uploading image: {file.filename}")
        image = service.upload_image(file)
        return image
    except CustomException as e:
        logger.error(f"Error uploading image: {e}")
        raise HTTPException(status_code=e.status_code, detail=str(e))


@router.post("/create", response_model=ImageResponse)
def create_image(
    image_data: ImageCreate,
    service: ImageService = Depends(get_image_service)
) -> ImageResponse:
    """이미지 정보를 생성합니다."""
    try:
        logger.info(f"Creating image: {image_data.url}")
        image = service.create_image(image_data)
        return image
    except CustomException as e:
        logger.error(f"Error creating image: {e}")
        raise HTTPException(status_code=e.status_code, detail=str(e))


@router.get("/", response_model=List[ImageResponse])
def get_images(
    skip: int = 0,
    limit: int = 100,
    service: ImageService = Depends(get_image_service)
) -> List[ImageResponse]:
    """이미지 목록을 조회합니다."""
    try:
        logger.info(f"Fetching images: skip={skip}, limit={limit}")
        images = service.get_images(skip=skip, limit=limit)
        return images
    except CustomException as e:
        logger.error(f"Error fetching images: {e}")
        raise HTTPException(status_code=e.status_code, detail=str(e))


@router.get("/{image_id}", response_model=ImageResponse)
def get_image(
    image_id: int,
    service: ImageService = Depends(get_image_service)
) -> ImageResponse:
    """특정 이미지를 조회합니다."""
    try:
        logger.info(f"Fetching image: id={image_id}")
        image = service.get_image_by_id(image_id)
        if not image:
            raise HTTPException(status_code=404, detail="Image not found")
        return image
    except CustomException as e:
        logger.error(f"Error fetching image: {e}")
        raise HTTPException(status_code=e.status_code, detail=str(e))


@router.put("/{image_id}", response_model=ImageResponse)
def update_image(
    image_id: int,
    image_data: ImageUpdate,
    service: ImageService = Depends(get_image_service)
) -> ImageResponse:
    """이미지를 업데이트합니다."""
    try:
        logger.info(f"Updating image: id={image_id}")
        image = service.update_image(image_id, image_data)
        if not image:
            raise HTTPException(status_code=404, detail="Image not found")
        return image
    except CustomException as e:
        logger.error(f"Error updating image: {e}")
        raise HTTPException(status_code=e.status_code, detail=str(e))


@router.delete("/{image_id}")
def delete_image(
    image_id: int,
    service: ImageService = Depends(get_image_service)
) -> dict[str, str]:
    """이미지를 삭제합니다."""
    try:
        logger.info(f"Deleting image: id={image_id}")
        success = service.delete_image(image_id)
        if not success:
            raise HTTPException(status_code=404, detail="Image not found")
        return {"message": "Image deleted successfully"}
    except CustomException as e:
        logger.error(f"Error deleting image: {e}")
        raise HTTPException(status_code=e.status_code, detail=str(e))
