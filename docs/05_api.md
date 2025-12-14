# API

## API 개요

PPOP Blog API는 RESTful API 설계 원칙을 따르며, 각 모듈별로 엔드포인트를 제공합니다.

## 기본 정보

- **Base URL**: `/api`
- **Content-Type**: `application/json`
- **인증**: 향후 구현 예정

## 모듈별 API 엔드포인트

### 키워드 모듈 (keywords)

**Base Path**: `/api/keywords`

- `GET /api/keywords` - 키워드 목록 조회
  - Query Parameters: `skip` (int), `limit` (int)
  - Response: `List[KeywordResponse]`

- `GET /api/keywords/{keyword_id}` - 특정 키워드 조회
  - Path Parameters: `keyword_id` (int)
  - Response: `KeywordResponse`

- `POST /api/keywords` - 새 키워드 생성
  - Request Body: `KeywordCreate`
  - Response: `KeywordResponse`

- `PUT /api/keywords/{keyword_id}` - 키워드 수정
  - Path Parameters: `keyword_id` (int)
  - Request Body: `KeywordUpdate`
  - Response: `KeywordResponse`

- `DELETE /api/keywords/{keyword_id}` - 키워드 삭제
  - Path Parameters: `keyword_id` (int)
  - Response: `{"message": "Keyword deleted successfully"}`

### 글 작성 모듈 (scripts)

**Base Path**: `/api/scripts`

- `GET /api/scripts` - 글 목록 조회
  - Query Parameters: `skip` (int), `limit` (int)
  - Response: `List[ScriptResponse]`

- `GET /api/scripts/{script_id}` - 특정 글 조회
  - Path Parameters: `script_id` (int)
  - Response: `ScriptResponse`

- `POST /api/scripts` - 새 글 생성
  - Request Body: `ScriptCreate`
  - Response: `ScriptResponse`

- `PUT /api/scripts/{script_id}` - 글 수정
  - Path Parameters: `script_id` (int)
  - Request Body: `ScriptUpdate`
  - Response: `ScriptResponse`

- `DELETE /api/scripts/{script_id}` - 글 삭제
  - Path Parameters: `script_id` (int)
  - Response: `{"message": "Script deleted successfully"}`

### 이미지 모듈 (images)

**Base Path**: `/api/images`

- `POST /api/images` - 이미지 파일 업로드
  - Request: `multipart/form-data` (file: UploadFile)
  - Response: `ImageResponse`

- `POST /api/images/create` - 이미지 정보 생성
  - Request Body: `ImageCreate`
  - Response: `ImageResponse`

- `GET /api/images` - 이미지 목록 조회
  - Query Parameters: `skip` (int), `limit` (int)
  - Response: `List[ImageResponse]`

- `GET /api/images/{image_id}` - 특정 이미지 조회
  - Path Parameters: `image_id` (int)
  - Response: `ImageResponse`

- `PUT /api/images/{image_id}` - 이미지 정보 수정
  - Path Parameters: `image_id` (int)
  - Request Body: `ImageUpdate`
  - Response: `ImageResponse`

- `DELETE /api/images/{image_id}` - 이미지 삭제
  - Path Parameters: `image_id` (int)
  - Response: `{"message": "Image deleted successfully"}`

### 업로드 모듈 (uploads)

**Base Path**: `/api/uploads`

- `POST /api/uploads` - 파일 업로드
  - Request: `multipart/form-data` (file: UploadFile)
  - Response: `UploadResponse`

- `GET /api/uploads` - 업로드 목록 조회
  - Query Parameters: `skip` (int), `limit` (int)
  - Response: `List[UploadListResponse]`

- `GET /api/uploads/{upload_id}` - 특정 업로드 조회
  - Path Parameters: `upload_id` (int)
  - Response: `UploadResponse`

- `DELETE /api/uploads/{upload_id}` - 업로드 삭제
  - Path Parameters: `upload_id` (int)
  - Response: `{"message": "Upload deleted successfully"}`

### 로그인 모듈 (login)

**Base Path**: `/api/login`

- 향후 구현 예정

## 공통 엔드포인트

- `GET /` - 루트 엔드포인트
  - Response: `{"message": "PPOP Blog API"}`

- `GET /health` - 헬스 체크
  - Response: `{"status": "ok"}`

## 에러 응답

모든 API는 표준 에러 응답 형식을 따릅니다:

```json
{
  "detail": "에러 메시지"
}
```

에러 상태 코드:
- `400`: 잘못된 요청
- `404`: 리소스를 찾을 수 없음
- `500`: 서버 내부 오류

## 참고사항

- API 명세는 프로그램 개발 과정에서 점차 업데이트됩니다
- 각 모듈의 스키마 정의는 `schemas.py` 파일을 참고하세요
- 상세한 API 문서는 FastAPI의 자동 생성 문서 (`/docs`)를 참고하세요
