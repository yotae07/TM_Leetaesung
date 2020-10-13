import json

from django.test  import (
    TestCase,
    Client
)

from .models      import (
    Year,
    Genres,
    Country,
    Movie
)

class MovieViewTest(TestCase):
    def setUp(self):
        year = Year.objects.create(
            year       = 2019,
            is_deleted = 0
        )
        Year.objects.create(
            year       = 2020,
            is_deleted = 0
        )
        Genres.objects.create(
            genres     = "SF",
            is_deleted = 0
        )
        genres = Genres.objects.create(
            genres     = "코메디",
            is_deleted = 0
        )
        Country.objects.create(
            country    = "미국",
            is_deleted = 0
        )
        Country.objects.create(
            country    = "일본",
            is_deleted = 0
        )
        country = Country.objects.create(
            country    = "한국",
            is_deleted = 0
        )
        Movie.objects.create(
            id      = 2,
            title   = "극한직업",
            year    = year,
            rating  = 4,
            genres  = genres,
            country = country,
            runtime = 111,
            summary = "고반장은 국제 범죄조직의 국내 마약 밀반입 정황을 포착하고 장형사, 마형사, 영호, 재훈까지 4명의 팀원들과 함께 잠복 수사에 나선다. 마약반은 24시간 감시를 위해 범죄조직의 아지트 앞 치킨집을 인수해 위장 창업을 하게 되고, 수사는 뒷전, 치킨장사로 눈코 뜰 새 없이 바빠진 마약반에게 어느 날 절호의 기회가 찾아오는데…",
            poster  = "극한직업_포스터",
        )

    def tearDown(self):
        Movie.objects.all().delete()
        Country.objects.all().delete()
        Genres.objects.all().delete()
        Year.objects.all().delete()

    def test_get_success(self):

        response = self.client.get('/movie')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {
            "data": [
                {
                    "id": 2,
                    "title": "극한직업",
                    "year": 2019,
                }]})

    def test_get_fail(self):

        response = self.client.get('/moive')
        self.assertEqual(response.status_code, 404)

    def test_post_success(self):
        movie = {
            "title": "테넷",
            "year": 2020,
            "rating": 5,
            "genres": "SF",
            "country": "미국",
            "runtime": 150,
            "summary": "시간의 흐름을 뒤집는 인버전을 통해 현재와 미래를 오가며 세상을 파괴하려는 사토르(케네스 브래너)를 막기 위해 투입된 작전의 주도자(존 데이비드 워싱턴). 인버전에 대한 정보를 가진 닐(로버트 패틴슨)과 미술품 감정사이자 사토르에 대한 복수심이 가득한 그의 아내 캣(엘리자베스 데비키)과 협력해 미래의 공격에 맞서 제3차 세계대전을 막아야 한다!",
            "poster": "테넷_포스터"
            }

        response = self.client.post('/movie', json.dumps(movie), content_type="application/json")
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(), {
            "message": "SUCCESS"
            })

    def test_post_fail_400(self):
        movie = {
            "title": "테넷",
            "year": 2020,
            "genres": "SF",
            "country": "미국",
            "runtime": 150,
            "summary": "시간의 흐름을 뒤집는 인버전을 통해 현재와 미래를 오가며 세상을 파괴하려는 사토르(케네스 브래너)를 막기 위해 투입된 작전의 주도자(존 데이비드 워싱턴). 인버전에 대한 정보를 가진 닐(로버트 패틴슨)과 미술품 감정사이자 사토르에 대한 복수심이 가득한 그의 아내 캣(엘리자베스 데비키)과 협력해 미래의 공격에 맞서 제3차 세계대전을 막아야 한다!",
            "poster": "테넷_포스터"
            }

        response = self.client.post('/movie', json.dumps(movie), content_type="application/json")
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {
            "message": "INVALID_REQUEST"
            })

    def test_post_fail_409(self):
        movie = {
            "title": "극한직업",
            "year": 2020,
            "genres": "코메디",
            "rating": 3,
            "country": "일본",
            "runtime": 111,
            "summary": "전혀 다른 내용",
            "poster": "또 다른 포스터"
            }

        response = self.client.post('/movie', json.dumps(movie), content_type="application/json")
        self.assertEqual(response.status_code, 409)
        self.assertEqual(response.json(), {
            "message": "EXISTS_MOVIE"
            })

    def test_put_success(self):
        movie = {
            "title": "극한직업",
            "runtime": 111,
            "rating": 2
            }

        response = self.client.put('/movie', json.dumps(movie), content_type="application/json")
        self.assertEqual(response.status_code, 202)
        self.assertEqual(response.json(), {
            "message": "SUCCESS"
            })

    def test_put_fail_406(self):
        movie = {
            "title": "극한작업",
            "runtime": 111,
            "rating": 4
            }

        response = self.client.put('/movie', json.dumps(movie), content_type="application/json")
        self.assertEqual(response.status_code, 406)
        self.assertEqual(response.json(), {
            "message": "INVALID_REQUEST"
            })

    def test_put_fail_400(self):
        movie = {
            "title": "극한직업",
            "rating": 4
            }

        response = self.client.put('/movie', json.dumps(movie), content_type="application/json")
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {
            "message": "INVALID_REQUEST"
            })

    def test_delete_success(self):
        movie = {
             "title": "극한직업",
            "runtime": 111
            }

        response = self.client.delete('/movie', json.dumps(movie), content_type="application/json")
        self.assertEqual(response.status_code, 202)
        self.assertEqual(response.json(), {
            "message": "SUCCESS"
            })

    def test_delete_fail_405(self):
        movie = {
            "title": "극한직업",
            "runtime": 111
            }

        response = self.client.patch('/movie', json.dumps(movie), content_type="application/json")
        self.assertEqual(response.status_code, 405)

    def test_delete_fail_400(self):
        movie = {
            "title": "국한직업",
            "runtime": 111
            }

        response = self.client.delete('/movie', json.dumps(movie), contetn_type="application/json")
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {
            "message": "INVALID_REQUEST"
            })

class MovieDetailViewTest(TestCase):
    def setUp(self):
        year = Year.objects.create(
            year       = 2019,
            is_deleted = 0
        )
        genres = Genres.objects.create(
            genres     = "코메디",
            is_deleted = 0
        )
        country = Country.objects.create(
            country    = "한국",
            is_deleted = 0
        )
        Movie.objects.create(
            id      = 4,
            title   = "극한직업",
            year    = year,
            rating  = 4,
            genres  = genres,
            country = country,
            runtime = 111,
            summary = "고반장은 국제 범죄조직의 국내 마약 밀반입 정황을 포착하고 장형사, 마형사, 영호, 재훈까지 4명의 팀원들과 함께 잠복 수사에 나선다. 마약반은 24시간 감시를 위해 범죄조직의 아지트 앞 치킨집을 인수해 위장 창업을 하게 되고, 수사는 뒷전, 치킨장사로 눈코 뜰 새 없이 바빠진 마약반에게 어느 날 절호의 기회가 찾아오는데",
            poster  = "극한직업_포스터",
        )

    def tearDown(self):
        Movie.objects.all().delete()
        Country.objects.all().delete()
        Genres.objects.all().delete()
        Year.objects.all().delete()

    def test_get_success(self):
        response = self.client.get('/movie/4')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {
            "data": [
                {
                    "id": 4,
                    "title": "극한직업",
                    "year": 2019,
                    "rating": 4,
                    "genres": "코메디",
                    "country": "한국",
                    "runtime": 111,
                    "summary": "고반장은 국제 범죄조직의 국내 마약 밀반입 정황을 포착하고 장형사, 마형사, 영호, 재훈까지 4명의 팀원들과 함께 잠복 수사에 나선다. 마약반은 24시간 감시를 위해 범죄조직의 아지트 앞 치킨집을 인수해 위장 창업을 하게 되고, 수사는 뒷전, 치킨장사로 눈코 뜰 새 없이 바빠진 마약반에게 어느 날 절호의 기회가 찾아오는데",
                    "poster": "극한직업_포스터"
                }]})

    def test_get_fail(self):
        response = self.client.get('/movie/10')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {
            "message": "INVALID_REQUEST"
            })

    def test_get_teapot(self):
        response = self.client.get('/movie/0')
        self.assertEqual(response.status_code, 418)
        self.assertEqual(response.json(), {
            "head": "I'm a teapot",
            "body": "The requested entity body is short and stout."
            })
