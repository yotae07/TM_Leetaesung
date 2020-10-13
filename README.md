# 이태성의 티켓플레이스 테스트 과제

### 프로젝트 테스트 방법
git clone으로 프로젝트를 받은후 requirments.txt의 패키지들을 설치한다. pip install -r requirments.txt
manage.py가 있는 디렉토리에서 python manage.py test를 입력하면 각 앱 tests.py에 등록된 테스트들이 실행된다.

### 프로젝트 실행 방법
manage.py가 있는 디렉토리에서 python manage.py runserver를 입력하면 서버가 가동되면서 프로젝트가 실행된다.

## Assigment

### 문제1

#### GET /movie
Success 200
{
    "id": "1",
    "title": "영화제목",
    "year": "개봉연도"
}

Not Found 404
{
    "message": "INVALID_REQUEST"
}

#### GET /movie/{movie_id}
Success 200
{
    "id": "1",
    "title": "영화제목",
    "year": "개봉연도",
    "rating": "영화평점",
    "genres": "영화장르",
    "country": "제작국가",
    "runtime": "작품시간",
    "summary": "영화줄거리",
    "poster": "영화포스터"
}

Not Found 400
{
    "message": "INVALID_REQUEST"
}

I'm a teapot 418
{
    "message": "The requested entity body is short and stout"
}

#### POST /movie
Created 201
{
    "message": "SUCCESS"
}

Conflict 409
{
    "message": "EXISTS_MOVIE"
}

#### PUT /movie
Accepted 202
{
    "message": "SUCCESS"
}

Not Accepted 406
{
    "message": "INVALID_REQUEST"
}

#### DELETE /movie
202 202
{
    "message": "SUCCESS"
}

Method Not Allowed 405
{
    "message": "INVALID_METHOD"
}
