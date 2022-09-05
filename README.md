## 프로젝트 내용
회원 정보 내용을 포함하는 테이블을 설계하고 다음과 같은 기능을 제공하는 서버 개발


## Stacks
- Python 3.10
- django 4.1
- sqlite3


## 데이터
### 회원정보
- 고객명, 회원등급, 성별, 나이, 연락처, 가입일, 마지막 작속일


## REST API 기능 개발
- [x]  회원가입
- [x]  로그인
- [x]  회원탈퇴
- [x]  공지사항
- [x]  자유게시판
- [x]  운영게시판
- [ ]  이용통계 1 - 남여
- [ ]  이용통계 2 - 나이
- [ ]  이용통계 3- 시간


## 코드 패키지 구조
- accounts 앱: 회원가입, 로그인, 회원탈퇴
- boards 앱: 공지사항, 자유게시판, 운영게시판
```
C:.
│  .env
│  .gitignore
│  COMMUNITY_SERVICE.txt
│  db.sqlite3
│  manage.py
│  Pipfile
│  Pipfile.lock
│  tree_view(commnity_service).txt
│  
├─accounts
│  │  admin.py
│  │  apps.py
│  │  models.py
│  │  serializers.py
│  │  tests.py
│  │  token.py
│  │  urls.py
│  │  views.py
│  │  __init__.py
│  │  
│  └─migrations
│          0001_initial.py
│          0003_alter_user_is_superuser.py
│          0004_alter_user_phone.py
│          0005_remove_user_teamgroup_alter_user_age_and_more.py
│          __init__.py
│          
├─boards
│  │  admin.py
│  │  apps.py
│  │  models.py
│  │  permissions.py
│  │  serializers.py
│  │  tests.py
│  │  urls.py
│  │  views.py
│  │  __init__.py
│  │  
│  └─migrations
│          0001_initial.py
│          0002_alter_comment_created_at.py
│          __init__.py
│          
└─community_service
    │  asgi.py
    │  urls.py
    │  wsgi.py
    │  __init__.py
    │  
    ├─settings
    │  │  common.py
    │  │  development.py
    │  │  production.py
    │  │  __init__.py
    │  │  
    │  └─__pycache__
    │          common.cpython-39.pyc
    │          development.cpython-39.pyc
    │          __init__.cpython-39.pyc
    │          
    └─__pycache__
            __init__.cpython-39.pyc
```


## API 정상동작 여부
### 회원가입
- 회원명

### 로그인
- 

### 회원탈퇴
- 

### 공지사항
- 

### 자유게시판
- 

### 운영게시판
- 

### 이용통계 1 - 남여
- 

### 이용통계 2 - 나이
- 

### 이용통계 3- 시간
- 



