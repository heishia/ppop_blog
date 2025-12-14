# Environment configuration management module

from pydantic_settings import BaseSettings
from typing import List
from functools import lru_cache


class Settings(BaseSettings):
    """애플리케이션 설정"""
    
    # 서버 설정
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    DEBUG: bool = False
    
    # CORS 설정
    CORS_ORIGINS: List[str] = ["http://localhost:3000", "http://localhost:8000"]
    
    # 데이터베이스 설정 (Supabase)
    SUPABASE_URL: str = ""
    SUPABASE_KEY: str = ""
    
    # 기타 설정
    SECRET_KEY: str = ""
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True


@lru_cache()
def get_settings() -> Settings:
    """설정 인스턴스를 반환합니다 (싱글톤 패턴)"""
    return Settings()


settings = get_settings()
