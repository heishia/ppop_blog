# Utils 모듈 가이드

## 목적
재활용 가능한 공통 유틸리티 함수들을 공통 로직별로 분리하여 관리하여 코드 중복을 방지하고 메모리를 절약합니다.

## 구조
공통 로직별로 파일을 분리하여 관리합니다.

### 예시 파일 구조
```
utils/
    __init__.py
    string_utils.py    # 문자열 변환, 슬러그, ID 생성 등
    time_utils.py      # 현재 시각, 포맷 변환, 시간 차이 계산
    validation_utils.py # 이메일, 전화번호, 비밀번호 등 입력 검증
    hash_utils.py      # 해시 생성, 비교, 토큰 생성
    file_utils.py      # 파일/폴더 생성, 읽기/쓰기
    json_utils.py      # JSON 직렬화/역직렬화, 안전 변환
    env_utils.py       # 환경 변수 로드 및 접근
    math_utils.py      # 단순 수학 계산, 비율, 반올림 등
```

## 사용 규칙

1. **공통 로직별 분리**: 비슷한 기능의 함수들은 같은 파일에 모아 관리합니다.
2. **재사용성 우선**: 여러 곳에서 사용될 가능성이 있는 함수는 utils 폴더에 배치합니다.
3. **순수 함수**: 가능한 한 부작용이 없는 순수 함수로 작성합니다.
4. **타입 힌트 필수**: 모든 함수에 타입 힌트를 명시합니다.
5. **문서화**: 각 함수에 docstring을 작성합니다.

## 사용 예시

```python
from backend.utils.string_utils import slugify
from backend.utils.time_utils import now_str

# 문자열 변환 시 수동 regex 대신 utils 함수 사용
slug = slugify("Hello World")  # "hello-world"

# 현재 시간 문자열은 datetime.now() 대신 utils 함수 사용
current_time = now_str()
```
