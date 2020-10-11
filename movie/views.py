import json

from django.http  import JsonResponse
from django.views import View

from .models      import (
    Year,
    Genres,
    Country,
    Movie
)

def MovieTitleValidator(title):
    if Movie.objects.filter(title = title).exists():
        return True
    return False

def MovieRuntimeValidator(runtime):
    if Movie.objects.filter(runtime = runtime).exists():
        return True
    return False

class MovieView(View):
    def get(self, request):
        datas  = Movie.objects.select_related('year').order_by('year', 'title')
        result = [
            {
                "id": data.id,
                "title": data.title,
                "year": data.year.year,
            } for data in datas]
        return JsonResponse({"data": result}, status=200)

    def post(self, request):
        try:
            data    = json.loads(request.body)
        
            title   = data.get("title")
            year    = data.get("year")
            rating  = data.get("rating")
            genres  = data.get("genres")
            country = data.get("country")
            runtime = data.get("runtime")
            summary = data.get("summary")
            poster  = data.get("poster")
            
            None_Checker = [title, year, rating, genres, country, runtime, summary, poster]

            if None in None_Checker:
                return JsonResponse({"message": "INVALID_REQUEST"}, status=400)

            MovieValidators = [MovieTitleValidator(title), MovieRuntimeValidator(runtime)]
            
            if False not in MovieValidators:
                return JsonResponse({"message": "EXISTS_MOVIE"}, status=409)

            Movie(
                title   = title,
                year    = Year.objects.get(year = year),
                rating  = rating,
                genres  = Genres.objects.get(genres = genres),
                country = Country.objects.get(country = country),
                runtime = runtime,
                summary = summary,
                poster  = poster
            ).save()
            return JsonResponse({"message": "SUCCESS"}, status=201)
        except KeyError:
            return JsonResponse({"message": "INVALID_REQUEST"}, status=400)

    def put(self, request):
        try:
            data    = json.loads(request.body)

            title   = data.get("title")
            runtime = data.get("runtime")
            rating  = data.get("rating")

            if title == None or runtime == None:
                return JsonResponse({"message": "INVALID_REQUEST"}, status=400)
            if Movie.objects.filter(title = title, runtime = runtime).exists():
                movie = Movie.objects.get(title = title, runtime = runtime)
                movie.rating = rating
                movie.save()
                return JsonResponse({"message": "SUCCESS"}, status=202)
            return JsonResponse({"message": "INVALID_REQUEST"}, status=406)
        except KeyError:
            return JsonResponse({"message": "INVALID_REQUEST"}, status=400)


class MovieDetailView(View):
    def get(self, request, movie_id):
        if movie_id == 0:
            return JsonResponse(
                    {
                        "head": "I'm a teapot",
                        "body": "The requested entity body is short and stout."
                    }, status=418)
        if Movie.objects.filter(id=movie_id).exists():
            datas  = Movie.objects.select_related('year', 'genres', 'country').all().order_by('year', 'title')
            result = [
                {
                    "id": data.id,
                    "title": data.title,
                    "year": data.year.year,
                    "rating": data.rating,
                    "genres": data.genres.genres,
                    "country": data.country.country,
                    "runtime": data.runtime,
                    "summary": data.summary,
                    "poster": data.poster
                } for data in datas]
            return JsonResponse({"data": result}, status=200)
        return JsonResponse({"message": "INVALID_REQUEST"}, status=400)
