from django.db import models

class Year(models.Model):
    year       = models.IntegerField()
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'years'

class Genres(models.Model):
    genres     = models.CharField(max_length=50)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'genreses'

class Country(models.Model):
    country    = models.CharField(max_length=50)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'countries'

class Movie(models.Model):
    title      = models.CharField(max_length=100)
    year       = models.ForeignKey(Year, on_delete=models.SET_NULL, null=True)
    rating     = models.IntegerField()
    genres     = models.ForeignKey(Genres, on_delete=models.SET_NULL, null=True)
    country    = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    runtime    = models.IntegerField()
    summary    = models.CharField(max_length=1000)
    poster     = models.CharField(max_length=500)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'movies'

