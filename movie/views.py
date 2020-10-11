import json

from django.http  import JsonResponse
from django.views import View

from .models      import (
    Year,
    Genres,
    Country,
    Movie
)

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

class MovieDetailView(View):
    def get(self, request, movie_id):
        if movie_id == 0:
            return JsonResponse(
                    {
                        "head": "I'm a teapot",
                        "body": "The requested entity body is short and stout."
                    }, status=418)
        if Movie.objects.filter(id=movie_id).exists():
            datas = Movie.objects.select_related('year', 'genres', 'country').all().order_by('year', 'title')
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
