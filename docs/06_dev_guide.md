# Development Guide

## 개발 환경 설정

### 필수 요구사항

- Python 3.8 이상
- Supabase 계정 및 프로젝트
- Git

### 초기 설정

1. **저장소 클론**
   ```bash
   git clone <repository-url>
   cd ppop_blog
   ```

2. **가상 환경 생성 및 활성화**
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # Linux/Mac
   source venv/bin/activate
   ```

3. **의존성 설치**
   ```bash
   pip install -r requirements.txt
   ```

4. **환경 변수 설정**
   - `.env` 파일을 생성하고 필요한 환경 변수를 설정합니다
   - Supabase 연결 정보 등 보안 관련 값은 `.env`에 저장합니다

5. **서버 실행**
   ```bash
   python backend/run.py
   ```
   또는
   ```bash
   uvicorn backend.main:app --reload
   ```

## 프로젝트 구조

```
ppop_blog/
├── backend/
│   ├── auth/              # 인증 모듈 (로그인 모듈 아님)
│   ├── core/              # 공통 모듈
│   │   ├── config.py      # 설정 관리
│   │   ├── database.py    # 데이터베이스 연결
│   │   ├── exceptions.py  # 커스텀 예외
│   │   ├── logger.py      # 로깅 설정
│   │   ├── models.py      # 데이터베이스 모델
│   │   └── security.py    # 보안 관련 기능
│   ├── image/             # 이미지 모듈
│   ├── keyword/           # 키워드 모듈
│   ├── login/             # 로그인 모듈
│   ├── script/            # 글 작성 모듈
│   ├── upload/            # 업로드 모듈
│   ├── main.py            # FastAPI 앱 진입점
│   ├── run.py             # 서버 실행 파일
│   └── GUIDELINES.md      # 코딩 가이드라인
├── docs/                  # 프로젝트 문서
├── requirements.txt       # Python 패키지 의존성
└── README.md             # 프로젝트 README
```

## 개발 가이드라인

### 코딩 규칙

자세한 코딩 가이드라인은 `backend/GUIDELINES.md`를 참고하세요.

**주요 규칙 요약:**

1. **타입 힌트 사용**
   - 함수, 클래스, 파라미터, 리턴 타입에 타입 힌트를 명시합니다

2. **네이밍 규칙**
   - 함수/변수명: `snake_case`
   - 클래스명: `PascalCase`
   - 파일/폴더명: 소문자 + 스네이크 케이스
   - 상수: `UPPER_SNAKE_CASE`

3. **에러 처리**
   - `core.exceptions`의 커스텀 예외를 사용합니다
   - `print` 대신 `logging` 모듈을 사용합니다

4. **모듈 구조**
   - 각 모듈은 `router.py`, `schemas.py`, `service.py`로 구성됩니다
   - 의존성 주입을 통해 서비스를 제공합니다

### 새 모듈 추가하기

1. `backend/` 디렉토리에 새 모듈 폴더를 생성합니다
2. 다음 파일들을 생성합니다:
   - `__init__.py`
   - `router.py` - API 라우트 정의
   - `schemas.py` - Pydantic 스키마 정의
   - `service.py` - 비즈니스 로직
3. `backend/main.py`에 라우터를 등록합니다

### 데이터베이스 작업

- Supabase를 데이터베이스로 사용합니다
- 데이터베이스 연결은 `core/database.py`를 통해 관리합니다
- 모델 정의는 `core/models.py`에 추가합니다

### 테스트

- 향후 테스트 프레임워크 추가 예정

### 로깅

- `core/logger.py`의 로거를 사용합니다
- 로그 레벨에 따라 적절한 메서드를 사용합니다:
  - `logger.info()` - 일반 정보
  - `logger.error()` - 에러 정보
  - `logger.debug()` - 디버깅 정보

## 개발 워크플로우

1. **기능 개발**
   - 기능별로 브랜치를 생성합니다
   - 코딩 가이드라인을 준수합니다
   - 커밋 메시지는 명확하게 작성합니다

2. **코드 리뷰**
   - Pull Request를 생성합니다
   - 리뷰 후 머지합니다

3. **배포**
   - 메인 브랜치에 머지되면 자동 배포됩니다 (향후 구현)

## 문제 해결

### 일반적인 문제

1. **의존성 오류**
   - `pip install -r requirements.txt`를 다시 실행합니다
   - 가상 환경이 활성화되어 있는지 확인합니다

2. **데이터베이스 연결 오류**
   - `.env` 파일의 Supabase 연결 정보를 확인합니다
   - 네트워크 연결을 확인합니다

3. **포트 충돌**
   - `run.py`에서 포트 번호를 변경합니다
   - 다른 프로세스가 포트를 사용 중인지 확인합니다

## 참고 자료

- [FastAPI 공식 문서](https://fastapi.tiangolo.com/)
- [Supabase 공식 문서](https://supabase.com/docs)
- [Pydantic 공식 문서](https://docs.pydantic.dev/)
- 프로젝트 내 `backend/GUIDELINES.md` 파일
