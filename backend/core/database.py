# Supabase or SQL database connection management

from supabase import create_client, Client
from core.config import settings
from core.logger import logger
from typing import Generator

# Supabase 클라이언트 인스턴스
_supabase_client: Client | None = None


def get_supabase_client() -> Client:
    """Supabase 클라이언트를 반환합니다."""
    global _supabase_client
    if _supabase_client is None:
        if not settings.SUPABASE_URL or not settings.SUPABASE_KEY:
            raise ValueError("Supabase URL and Key must be set in environment variables")
        _supabase_client = create_client(settings.SUPABASE_URL, settings.SUPABASE_KEY)
        logger.info("Supabase client initialized")
    return _supabase_client


def get_db() -> Generator[Client, None, None]:
    """데이터베이스 연결을 반환합니다 (의존성 주입용)."""
    try:
        db = get_supabase_client()
        yield db
    except Exception as e:
        logger.error(f"Database connection error: {e}", exc_info=True)
        raise
    finally:
        # 필요시 정리 작업
        pass
