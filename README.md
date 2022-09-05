## :mag_right: 프로젝트 내용
회원 정보 내용을 포함하는 테이블을 설계하고 다음과 같은 기능을 제공하는 서버 개발<br>
출처 : Wayne_Hills_Ventures

## :bulb: Stacks
<img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white"> <img src="https://img.shields.io/badge/django-092E20?style=for-the-badge&logo=django&logoColor=white"> <img src="https://img.shields.io/badge/django-003B57?style=for-the-badge&logo=django&logoColor=white"> 

## :alien: 팀원
- 이대영
- 이민석
- 최관호
- 정재균
- 황유정

## :baby: 역할
:thumbsup: 이대영
    - 회원가입, 회원탈퇴 API 구현 <br>
:thumbsup: 이민석
    - 로그인 API 구현 <br>
:thumbsup: 최관호
    - 공지사항 게시판 API 구현 <br>
:thumbsup: 황유정
    - 자유게시판 API 구현 <br>
:thumbsup: 정재균
    - 운영게시판 API 구현 <br>

## :+1: 요구사항 분석

- 회원 정보 내용을 포함하는 테이블 설계 후, 각 조건에 맞는 REST API 기능을 제공한다.

1. 로그인/회원가입/회원탈퇴
   - simplejwt 토큰을 이용한 회원가입, 로그인
   
2. 회원 등급에 따른 게시판 기능 접근제어
   - 공지 게시판
        - 글 목록 조회 : 모든 접속자 가능
        - 글 등록/수정/삭제 : superuser만 가능
        
   - 자유 게시판:
        - 목록조회/글 등록 / 수정 / 삭제 : 모두 가능
        
   - 운영 게시판:
         - 글 목록 조회 : 모든 접속자 가능
         - 글 등록/수정/삭제 : superuser만 가능

3. 본 사이트 이용 통계 집계
   - 남/여별, 나이별, 접속 시간별


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
- username(아이디),gender(성별),age(나이),password(비밀번호)를 입력하여 회원가입
![register](https://user-images.githubusercontent.com/99165573/188481506-30cf4cab-c28b-4b23-95d4-31ae58897a7e.jpg)

### 로그인

- username(아이디),password(비밀번호)를 입력하여 로그인 후, 토큰 부여
![login](https://user-images.githubusercontent.com/99165573/188481728-e3784a06-9d7f-48e6-b857-1c6ba93b2197.jpg)

### 회원탈퇴

![user delete](https://user-images.githubusercontent.com/99165573/188481945-95f825c3-11bd-4075-ac37-0364f0414f6c.jpg)

### (자유게시판을 대표로, 다른 항목 게시판과 API 구현은 동일합니다.)

### 게시판 게시글 등록
- title(제목), content(내용)을 입력하여 글 등록

![freepost create](https://user-images.githubusercontent.com/99165573/188482352-bc31c6b2-31c7-4781-9513-7c921a580dda.jpg)

### 게시판 게시글 목록 조회

![freepost read](https://user-images.githubusercontent.com/99165573/188483176-d20e98bc-c981-4a77-a826-06561fe402b3.jpg)

### 게시판 게시글 삭제
- title(제목), content(내용) 에 기재되어 있는 'test' -> 'test2'로 변경

![freepost delete](https://user-images.githubusercontent.com/99165573/188483571-c5bdb45a-4673-4f51-8f3c-ae32a39087b6.jpg)

### 게시판 게시글 삭제

![freepost delete](https://user-images.githubusercontent.com/99165573/188483415-c0c463b7-7eb3-487e-9c34-10ee3ed32cfd.jpg)

## sql 쿼리문을 이용한 항목 별 이용 통계

### - Dummydata 약 500개를 이용

### 이용통계 1 - 남여
- sql 쿼리문 : [gender = 0 or 1] select count (gender) from users where gender=[0 or 1];

  - 남자 -> 0 / 여자 -> 1 , 남자 248명 / 여자 252명 인 것을 알 수 있음
  
![image](https://user-images.githubusercontent.com/99165573/188484798-0d64ea4c-667e-4858-9c7d-956b02b33938.png)

### 이용통계 2 - 나이
- [나이(int) and 나이(int)] select count (age) from users where age between [나이 and 나이];

    - 10 ~ 19 = 청소년(teenager) -> 39명
    - 20 ~ 34 = 청년(youth) -> 135명
    - 35 ~ 50 = 중장년(middle_adged) -> 130명
    - 51 ~ 80 = 노인(old_man) -> 196명
    
![image](https://user-images.githubusercontent.com/99165573/188486839-e37713cc-4cdd-4788-b560-733e1e090eed.png)

### 이용통계 3- 접속 날짜,시간별 [시간 and 시간]

- date=datetime.datetime(randint(2022,2022), randint(9,9), randint(1,4), randint(0,23), randint(0,59))
- 2022/09/04 00:00:00 ~ 2022/09/04 24:00:00 , 2022/09/05 00:00:00 ~ 2022/09/05 24:00:00

![image](https://user-images.githubusercontent.com/99165573/188487224-f362435b-30e1-4705-81c1-bfefea7e4238.png)


## branch 컨벤션 

- 브랜치는 삭제하지 않는다
    - 추후에 해당 브랜치를 다시 사용해야 할 일이 있다면 토의 후에 사용
    - (참고) 브랜치 네이밍 전략 ex) feature/ `{app이름}` / `{기능}`-api




