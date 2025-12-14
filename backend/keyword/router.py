# Keyword API router

from fastapi import APIRouter, Depends, HTTPException
from typing import List
from core.logger import logger
from core.exceptions import CustomException
from .schemas import KeywordCreate, KeywordResponse, KeywordUpdate
from .service import KeywordService, get_keyword_service

router = APIRouter(prefix="/api/keywords", tags=["keywords"])


@router.get("/", response_model=List[KeywordResponse])
def get_keywords(
    skip: int = 0,
    limit: int = 100,
    service: KeywordService = Depends(get_keyword_service)
) -> List[KeywordResponse]:
    """키워드 목록을 조회합니다."""
    try:
        logger.info(f"Fetching keywords: skip={skip}, limit={limit}")
        keywords = service.get_keywords(skip=skip, limit=limit)
        return keywords
    except CustomException as e:
        logger.error(f"Error fetching keywords: {e}")
        raise HTTPException(status_code=e.status_code, detail=str(e))


@router.get("/{keyword_id}", response_model=KeywordResponse)
def get_keyword(
    keyword_id: int,
    service: KeywordService = Depends(get_keyword_service)
) -> KeywordResponse:
    """특정 키워드를 조회합니다."""
    try:
        logger.info(f"Fetching keyword: id={keyword_id}")
        keyword = service.get_keyword_by_id(keyword_id)
        if not keyword:
            raise HTTPException(status_code=404, detail="Keyword not found")
        return keyword
    except CustomException as e:
        logger.error(f"Error fetching keyword: {e}")
        raise HTTPException(status_code=e.status_code, detail=str(e))


@router.post("/", response_model=KeywordResponse)
def create_keyword(
    keyword_data: KeywordCreate,
    service: KeywordService = Depends(get_keyword_service)
) -> KeywordResponse:
    """새 키워드를 생성합니다."""
    try:
        logger.info(f"Creating keyword: {keyword_data.name}")
        keyword = service.create_keyword(keyword_data)
        return keyword
    except CustomException as e:
        logger.error(f"Error creating keyword: {e}")
        raise HTTPException(status_code=e.status_code, detail=str(e))


@router.put("/{keyword_id}", response_model=KeywordResponse)
def update_keyword(
    keyword_id: int,
    keyword_data: KeywordUpdate,
    service: KeywordService = Depends(get_keyword_service)
) -> KeywordResponse:
    """키워드를 업데이트합니다."""
    try:
        logger.info(f"Updating keyword: id={keyword_id}")
        keyword = service.update_keyword(keyword_id, keyword_data)
        if not keyword:
            raise HTTPException(status_code=404, detail="Keyword not found")
        return keyword
    except CustomException as e:
        logger.error(f"Error updating keyword: {e}")
        raise HTTPException(status_code=e.status_code, detail=str(e))


@router.delete("/{keyword_id}")
def delete_keyword(
    keyword_id: int,
    service: KeywordService = Depends(get_keyword_service)
) -> dict[str, str]:
    """키워드를 삭제합니다."""
    try:
        logger.info(f"Deleting keyword: id={keyword_id}")
        success = service.delete_keyword(keyword_id)
        if not success:
            raise HTTPException(status_code=404, detail="Keyword not found")
        return {"message": "Keyword deleted successfully"}
    except CustomException as e:
        logger.error(f"Error deleting keyword: {e}")
        raise HTTPException(status_code=e.status_code, detail=str(e))
