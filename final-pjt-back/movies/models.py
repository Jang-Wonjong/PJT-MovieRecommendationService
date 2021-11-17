from django.db import models


# Create your models here.
class Movie(models.Model):
    id = models.IntegerField(primary_key=True)
    adult = models.BooleanField()
    backdrop_path = models.TextField()
    genre_ids = models.TextField()
    tmdb_id = models.IntegerField()
    original_language = models.CharField(max_length=50)
    original_title = models.CharField(max_length=100)
    overview = models.TextField()
    popularity = models.FloatField()
    poster_path = models.TextField()
    release_date = models.DateField()
    title = models.CharField(max_length=100)
    video = models.BooleanField()
    vote_average = models.FloatField()
    vote_count = models.IntegerField()

    def __str__(self):
        return self.title