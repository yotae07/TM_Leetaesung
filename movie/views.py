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
