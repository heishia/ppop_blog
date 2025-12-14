# Script business logic service

from typing import List, Optional
from core.logger import logger
from core.exceptions import CustomException
from core.database import get_db
from .schemas import ScriptCreate, ScriptUpdate, ScriptResponse


def get_script_service():
    """ScriptService 의존성 함수"""
    db = next(get_db())
    return ScriptService(db=db)


class ScriptService:
    """스크립트 관련 비즈니스 로직을 처리합니다."""
    
    def __init__(self, db=None):
        self.db = db
    
    def get_scripts(self, skip: int = 0, limit: int = 100) -> List[ScriptResponse]:
        """스크립트 목록을 조회합니다."""
        try:
            logger.info(f"Fetching scripts from database: skip={skip}, limit={limit}")
            # TODO: 데이터베이스에서 스크립트 목록 조회 로직 구현
            return []
        except Exception as e:
            logger.error(f"Failed to fetch scripts: {e}", exc_info=True)
            raise CustomException("Failed to fetch scripts")
    
    def get_script_by_id(self, script_id: int) -> Optional[ScriptResponse]:
        """ID로 스크립트를 조회합니다."""
        try:
            logger.info(f"Fetching script by id: {script_id}")
            # TODO: 데이터베이스에서 스크립트 조회 로직 구현
            return None
        except Exception as e:
            logger.error(f"Failed to fetch script: {e}", exc_info=True)
            raise CustomException("Failed to fetch script")
    
    def create_script(self, script_data: ScriptCreate) -> ScriptResponse:
        """새 스크립트를 생성합니다."""
        try:
            logger.info(f"Creating script: {script_data.title}")
            # TODO: 데이터베이스에 스크립트 생성 로직 구현
            raise NotImplementedError("Script creation not implemented")
        except Exception as e:
            logger.error(f"Failed to create script: {e}", exc_info=True)
            raise CustomException("Failed to create script")
    
    def update_script(self, script_id: int, script_data: ScriptUpdate) -> Optional[ScriptResponse]:
        """스크립트를 업데이트합니다."""
        try:
            logger.info(f"Updating script: id={script_id}")
            # TODO: 데이터베이스에서 스크립트 업데이트 로직 구현
            return None
        except Exception as e:
            logger.error(f"Failed to update script: {e}", exc_info=True)
            raise CustomException("Failed to update script")
    
    def delete_script(self, script_id: int) -> bool:
        """스크립트를 삭제합니다."""
        try:
            logger.info(f"Deleting script: id={script_id}")
            # TODO: 데이터베이스에서 스크립트 삭제 로직 구현
            return False
        except Exception as e:
            logger.error(f"Failed to delete script: {e}", exc_info=True)
            raise CustomException("Failed to delete script")
