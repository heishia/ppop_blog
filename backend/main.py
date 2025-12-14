# FastAPI app definition file
# Server execution code should not be included here

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from core.config import settings
from core.logger import logger
from core.exceptions import CustomException
from keyword.router import router as keyword_router
from script.router import router as script_router
from upload.router import router as upload_router
from image.router import router as image_router

app = FastAPI(
    title="PPOP Blog API",
    description="PPOP Blog Backend API",
    version="1.0.0"
)

# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 라우터 등록
app.include_router(keyword_router)
app.include_router(script_router)
app.include_router(upload_router)
app.include_router(image_router)


# 전역 예외 핸들러 등록
@app.exception_handler(CustomException)
async def custom_exception_handler(request, exc: CustomException):
    logger.error(f"CustomException: {exc.message}")
    from fastapi.responses import JSONResponse
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.message}
    )


@app.get("/")
def root():
    """루트 엔드포인트"""
    return {"message": "PPOP Blog API"}


@app.get("/health")
def health_check():
    """헬스 체크 엔드포인트"""
    return {"status": "ok"}
