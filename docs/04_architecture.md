# Architecture

## 시스템 아키텍처 개요

PPOP Blog는 FastAPI 기반의 RESTful API 서버로 구성되어 있습니다. 모듈화된 구조로 각 기능을 독립적으로 관리하며, Supabase를 데이터베이스로 사용합니다.

## 모듈 구조

### 주요 모듈

프로그램은 다음 5개의 주요 기능 모듈로 구성됩니다:

1. **keyword**: 키워드 추출 및 관리
2. **script**: 글 작성 및 관리
3. **image**: 이미지 첨부 및 관리
4. **login**: 네이버 블로그 로그인 처리
5. **upload**: 포스팅 업로드 처리

### 공통 모듈 (core)

- **config**: 설정 관리
- **database**: 데이터베이스 연결 및 관리
- **exceptions**: 커스텀 예외 정의
- **logger**: 로깅 설정
- **models**: 데이터베이스 모델
- **security**: 보안 관련 기능

## 모듈 구조 패턴

각 기능 모듈은 다음과 같은 표준 구조를 따릅니다:

```
module_name/
    __init__.py
    router.py      # API 라우트 정의
    schemas.py     # Pydantic 스키마 정의
    service.py     # 비즈니스 로직
```

### Router (router.py)
- FastAPI의 APIRouter를 사용하여 API 엔드포인트를 정의합니다
- 요청/응답 검증 및 에러 처리를 담당합니다

### Schemas (schemas.py)
- Pydantic 모델을 사용하여 요청/응답 데이터 구조를 정의합니다
- 데이터 검증 및 직렬화를 처리합니다

### Service (service.py)
- 비즈니스 로직을 구현합니다
- 데이터베이스 접근 및 외부 API 호출을 담당합니다
- 의존성 주입을 통해 Router에 제공됩니다

## 데이터 흐름

```
Client Request
    |
    v
[Router] -> 요청 검증
    |
    v
[Service] -> 비즈니스 로직 처리
    |
    v
[Database] -> 데이터 저장/조회
    |
    v
[Service] -> 응답 데이터 구성
    |
    v
[Router] -> 응답 반환
    |
    v
Client Response
```

## 모듈 간 의존성

- 모든 모듈은 `core` 모듈의 공통 기능을 사용합니다
- `upload` 모듈은 `login` 모듈의 로그인 기능을 사용합니다
- `script` 모듈은 `keyword` 모듈의 키워드 정보를 참조합니다
- `upload` 모듈은 `script`와 `image` 모듈의 데이터를 사용합니다

## 기술 스택

- **웹 프레임워크**: FastAPI
- **데이터베이스**: Supabase (PostgreSQL)
- **서버 실행**: Uvicorn
- **데이터 검증**: Pydantic
- **로깅**: Python logging 모듈

## 아키텍처 다이어그램

```
┌─────────────────────────────────────────┐
│           Client (Frontend)             │
└─────────────────┬───────────────────────┘
                  │
                  │ HTTP Request/Response
                  │
┌─────────────────▼───────────────────────┐
│         FastAPI Application              │
│  ┌───────────────────────────────────┐  │
│  │         Router Layer              │  │
│  │  keyword │ script │ image │ etc   │  │
│  └──────────┬────────────────────────┘  │
│             │                           │
│  ┌──────────▼────────────────────────┐  │
│  │        Service Layer              │  │
│  │  Business Logic & Processing     │  │
│  └──────────┬────────────────────────┘  │
│             │                           │
│  ┌──────────▼────────────────────────┐  │
│  │         Core Modules              │  │
│  │  config │ database │ logger │ etc │  │
│  └──────────┬────────────────────────┘  │
└─────────────┼───────────────────────────┘
              │
              │ Database Connection
              │
┌─────────────▼───────────────────────────┐
│         Supabase (PostgreSQL)           │
└─────────────────────────────────────────┘
```
