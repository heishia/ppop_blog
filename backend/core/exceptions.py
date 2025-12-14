# Common exception handling module

from typing import Optional


class CustomException(Exception):
    """기본 커스텀 예외 클래스"""
    
    def __init__(self, message: str, status_code: int = 500):
        self.message = message
        self.status_code = status_code
        super().__init__(self.message)


class NotFoundException(CustomException):
    """리소스를 찾을 수 없을 때 발생하는 예외"""
    
    def __init__(self, message: str = "Resource not found"):
        super().__init__(message, status_code=404)


class ValidationException(CustomException):
    """유효성 검증 실패 시 발생하는 예외"""
    
    def __init__(self, message: str = "Validation failed"):
        super().__init__(message, status_code=400)


class UnauthorizedException(CustomException):
    """인증 실패 시 발생하는 예외"""
    
    def __init__(self, message: str = "Unauthorized"):
        super().__init__(message, status_code=401)


class ForbiddenException(CustomException):
    """권한 없음 시 발생하는 예외"""
    
    def __init__(self, message: str = "Forbidden"):
        super().__init__(message, status_code=403)
