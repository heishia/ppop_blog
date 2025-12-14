# Script API router

from fastapi import APIRouter, Depends, HTTPException
from typing import List
from core.logger import logger
from core.exceptions import CustomException
from .schemas import ScriptCreate, ScriptResponse, ScriptUpdate
from .service import ScriptService, get_script_service

router = APIRouter(prefix="/api/scripts", tags=["scripts"])


@router.get("/", response_model=List[ScriptResponse])
def get_scripts(
    skip: int = 0,
    limit: int = 100,
    service: ScriptService = Depends(get_script_service)
) -> List[ScriptResponse]:
    """스크립트 목록을 조회합니다."""
    try:
        logger.info(f"Fetching scripts: skip={skip}, limit={limit}")
        scripts = service.get_scripts(skip=skip, limit=limit)
        return scripts
    except CustomException as e:
        logger.error(f"Error fetching scripts: {e}")
        raise HTTPException(status_code=e.status_code, detail=str(e))


@router.get("/{script_id}", response_model=ScriptResponse)
def get_script(
    script_id: int,
    service: ScriptService = Depends(get_script_service)
) -> ScriptResponse:
    """특정 스크립트를 조회합니다."""
    try:
        logger.info(f"Fetching script: id={script_id}")
        script = service.get_script_by_id(script_id)
        if not script:
            raise HTTPException(status_code=404, detail="Script not found")
        return script
    except CustomException as e:
        logger.error(f"Error fetching script: {e}")
        raise HTTPException(status_code=e.status_code, detail=str(e))


@router.post("/", response_model=ScriptResponse)
def create_script(
    script_data: ScriptCreate,
    service: ScriptService = Depends(get_script_service)
) -> ScriptResponse:
    """새 스크립트를 생성합니다."""
    try:
        logger.info(f"Creating script: {script_data.title}")
        script = service.create_script(script_data)
        return script
    except CustomException as e:
        logger.error(f"Error creating script: {e}")
        raise HTTPException(status_code=e.status_code, detail=str(e))


@router.put("/{script_id}", response_model=ScriptResponse)
def update_script(
    script_id: int,
    script_data: ScriptUpdate,
    service: ScriptService = Depends(get_script_service)
) -> ScriptResponse:
    """스크립트를 업데이트합니다."""
    try:
        logger.info(f"Updating script: id={script_id}")
        script = service.update_script(script_id, script_data)
        if not script:
            raise HTTPException(status_code=404, detail="Script not found")
        return script
    except CustomException as e:
        logger.error(f"Error updating script: {e}")
        raise HTTPException(status_code=e.status_code, detail=str(e))


@router.delete("/{script_id}")
def delete_script(
    script_id: int,
    service: ScriptService = Depends(get_script_service)
) -> dict[str, str]:
    """스크립트를 삭제합니다."""
    try:
        logger.info(f"Deleting script: id={script_id}")
        success = service.delete_script(script_id)
        if not success:
            raise HTTPException(status_code=404, detail="Script not found")
        return {"message": "Script deleted successfully"}
    except CustomException as e:
        logger.error(f"Error deleting script: {e}")
        raise HTTPException(status_code=e.status_code, detail=str(e))
