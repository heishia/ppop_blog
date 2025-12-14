# Domain

## 도메인 모델

### 기본 도메인

#### Post (포스팅)

블로그 포스팅을 나타내는 도메인 모델입니다.

**주요 속성**
- id: 포스팅 고유 식별자
- title: 포스팅 제목
- content: 포스팅 내용
- keyword_id: 연관된 키워드 ID
- image_ids: 첨부된 이미지 ID 목록
- status: 포스팅 상태 (draft, reviewed, published)
- created_at: 생성 일시
- updated_at: 수정 일시

**관계**
- Keyword와 다대일 관계
- Image와 다대다 관계

#### Keyword (키워드)

블로그 포스팅에 사용될 키워드를 나타내는 도메인 모델입니다.

**키워드 종류**
- **황금키워드 (golden)**: 검색량과 문서수 조건을 필터링했을 때 나온 키워드
- **일반키워드 (normal)**: 일반적인 키워드
- **연관키워드 (related)**: 주제 선택 시 조회되는 연관 키워드 (프로그램 로직상 연관키워드를 조회한 후 필터를 거쳐 황금키워드를 추출하기 위해 구분)

**주요 속성**
- id: 키워드 고유 식별자
- name: 키워드 이름
- type: 키워드 종류 (golden, normal, related)
- description: 키워드 설명 (선택)
- search_volume: 검색량
- view_count: 조회수
- document_count: 문서량
- is_golden: 황금키워드 여부 (검색량 및 문서수 조건 통과 여부)
- subject_id: 연관된 주제 ID (연관키워드인 경우)
- related_keyword_id: 연관된 키워드 ID (연관키워드인 경우)
- created_at: 생성 일시
- updated_at: 수정 일시

**관계**
- Post와 일대다 관계
- Subject와 다대일 관계 (연관키워드인 경우)
- Keyword와 자기 자신과의 다대일 관계 (연관키워드 관계)

#### Subject (주제)

황금키워드 추출을 위한 주제를 나타내는 도메인 모델입니다.

**주요 속성**
- id: 주제 고유 식별자
- name: 주제 이름
- description: 주제 설명 (선택)
- created_at: 생성 일시
- updated_at: 수정 일시

**관계**
- Keyword와 일대다 관계 (연관키워드)

### 추가 추천 도메인

#### Image (이미지)

포스팅에 첨부되는 이미지의 메타데이터를 나타내는 도메인 모델입니다.

**주요 속성**
- id: 이미지 고유 식별자
- url: 이미지 파일 경로 또는 URL
- filename: 원본 파일명
- file_size: 파일 크기
- mime_type: MIME 타입
- created_at: 생성 일시
- updated_at: 수정 일시

**관계**
- Post와 다대다 관계

#### User (사용자)

시스템 사용자 정보를 나타내는 도메인 모델입니다.

**주요 속성**
- id: 사용자 고유 식별자
- username: 사용자명
- email: 이메일 주소
- created_at: 생성 일시
- updated_at: 수정 일시

**관계**
- BlogAccount와 일대일 관계

#### BlogAccount (블로그 계정)

네이버 블로그 계정 정보를 나타내는 도메인 모델입니다.

**주요 속성**
- id: 계정 고유 식별자
- user_id: 사용자 ID
- blog_id: 네이버 블로그 ID
- login_status: 로그인 상태
- session_data: 세션 데이터 (암호화)
- last_login_at: 마지막 로그인 일시
- created_at: 생성 일시
- updated_at: 수정 일시

**관계**
- User와 일대일 관계

## 도메인 관계도

```
Subject (1) ----< (N) Keyword (N) ----< (1) Post (N) >---- (N) Image
                              |
                              |
                         (1) User (1) ---- (1) BlogAccount
```

## 참고사항

도메인 모델은 프로그램 개발 과정에서 점차 업데이트되며, 실제 구현에 따라 속성과 관계가 변경될 수 있습니다.
