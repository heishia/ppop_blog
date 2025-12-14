# 백엔드 코딩 가이드라인

이 문서는 백엔드 개발 시 참고할 기본 규칙과 작성 규칙을 정의합니다.

## 기본 규칙

### 전역 에러 처리

에러 처리는 `core.exceptions`에 정의된 커스텀 예외를 사용하도록 합니다. 필요한 예외 클래스는 자동으로 import합니다.

```python
from core.exceptions import CustomException
```

### 이모티콘 사용 금지

코드 내에서 이모티콘을 사용하지 않습니다.

### 타입 힌트 활용

함수, 클래스, 파라미터, 리턴 타입에는 가능한 한 타입 힌트를 명시합니다.

```python
def load_data(user_id: int) -> dict[str, Any]:
    pass
```

### 주석 스타일

주석은 설명이 필요한 핵심 로직에만 최소한으로 작성합니다.
주석 대신 함수명과 변수명으로 의도를 드러내는 방식을 우선합니다.

### 터미널 출력 최소화

`print` 문은 사용자가 요청하기 전에는 정말 필수적인 것만 작성하여 최소화합니다. 대신 `logging` 모듈을 사용합니다. 기본 로깅 설정은 `core/logger.py`를 참고합니다.

```python
from core.logger import logger

logger.info("Processing request")
logger.error("Error occurred", exc_info=True)
```

### Config 및 Env 활용

보안 및 환경별 값은 `.env`에 두고, `config.py`에서는 이를 로드하거나 기본 설정값만 정의하도록 구성합니다.

### Main 실행 방식

`main.py`는 앱의 진입점 역할만 담당합니다.
라우터 등록, 예외 핸들러 등록, config 로드 정도만 작성합니다.

### 네이밍 규칙

- 함수/변수명: `snake_case`
- 클래스명: `PascalCase`
- 파일/폴더명: 소문자 + 스네이크 케이스
- 상수: `UPPER_SNAKE_CASE`

### Requirements.txt

새로운 패키지를 추가할 때는 `requirements.txt`를 업데이트합니다.

## 작성 규칙

함수, 클래스, 실행부로 구성된 모듈 파일 구조를 따릅니다.

### 함수

- 한 함수 = 단일 책임 원칙(SRP)
- 네이밍 = 기능을 잘 알 수 있게 명사+목적어 형태 (예: `load_data()`, `create_user()`)

```python
def load_user_data(user_id: int) -> dict[str, Any]:
    """사용자 데이터를 로드합니다."""
    pass
```

### 클래스

- 하나의 역할(주제) = 변경의 축 + 데이터 소유권
- 역할이 다르다면 분리합니다

```python
class UserService:
    """사용자 관련 비즈니스 로직을 처리합니다."""
    
    def __init__(self, db: Database):
        self.db = db
    
    def create_user(self, user_data: dict) -> User:
        pass
```

### 실행부

- 항상 맨 하단에 작성
- 실행부는 흐름만 작성
- 세부 로직은 함수/클래스 안에 넣습니다

```python
if __name__ == "__main__":
    # 실행 흐름만 작성
    data = load_data()
    result = process_data(data)
    save_result(result)
```

### run.py

`uvicorn` 서버를 실행하는 파일입니다. `main.py`의 `app`을 불러와 서버로 실행합니다.

### 데이터베이스

Supabase를 사용합니다.

### 서버

Uvicorn을 사용합니다.

## 모듈 구조

각 기능 모듈은 다음과 같은 구조를 가집니다:

```
module_name/
    __init__.py
    router.py      # API 라우트 정의
    schemas.py     # Pydantic 스키마 정의
    service.py     # 비즈니스 로직
```

### Router 예시

```python
from fastapi import APIRouter, Depends
from core.exceptions import CustomException
from core.logger import logger

router = APIRouter(prefix="/api/module", tags=["module"])

@router.get("/")
def get_items():
    try:
        # 로직
        pass
    except CustomException as e:
        logger.error(f"Error: {e}")
        raise
```

### Schemas 예시

```python
from pydantic import BaseModel
from typing import Optional

class ItemCreate(BaseModel):
    name: str
    description: Optional[str] = None

class ItemResponse(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
```

### Service 예시

```python
from core.logger import logger
from core.exceptions import CustomException
from core.database import get_db

def get_item_service():
    """ItemService 의존성 함수"""
    db = next(get_db())
    return ItemService(db=db)

class ItemService:
    def __init__(self, db):
        self.db = db
    
    def create_item(self, item_data: dict) -> dict:
        try:
            # 비즈니스 로직
            logger.info("Creating item")
            return result
        except Exception as e:
            logger.error(f"Failed to create item: {e}")
            raise CustomException("Failed to create item")
```

### 의존성 주입

FastAPI의 의존성 주입을 사용하여 서비스를 주입합니다. 각 서비스 모듈에는 `get_<service_name>_service()` 함수를 정의하여 의존성을 제공합니다.

```python
# router.py
from .service import ItemService, get_item_service

@router.post("/")
def create_item(
    item_data: ItemCreate,
    service: ItemService = Depends(get_item_service)
):
    pass
```
