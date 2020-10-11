import json

from django.test  import (
    TestCase,
    Client
)

from .models import (
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
        genres = Genres.objects.create(
            genres     = "코메디",
            is_deleted = 0
        )
        country = Country.objects.create(
            country    = "한국",
            is_deleted = 0
        )
        Movie.objects.create(
            title   = "극한직업",
            year    = year,
            rating  = 4,
            genres  = genres,
            country = country,
            runtime = 111,
            summary = "불철주야 달리고 구르지만 실적은 바닥, 급기야 해체 위기를 맞는 마약반! 더 이상 물러설 곳이 없는 팀의 맏형 고반장은 국제 범죄조직의 국내 마약 밀반입 정황을 포착하고 장형사, 마형사, 영호, 재훈까지 4명의 팀원들과 함께 잠복 수사에 나선다. 마약반은 24시간 감시를 위해 범죄조직의 아지트 앞 치킨집을 인수해 위장 창업을 하게 되고, 뜻밖의 절대미각을 지닌 마형사의 숨은 재능으로 치킨집은 일약 맛집으로 입소문이 나기 시작한다. 수사는 뒷전, 치킨장사로 눈코 뜰 새 없이 바빠진 마약반에게 어느 날 절호의 기회가 찾아오는데…",
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
