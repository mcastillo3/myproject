from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=100)
    year = models.CharField(max_length=4)
    imdb_rating = models.DecimalField(max_digits=3, decimal_places=1)
    poster = models.URLField()
    plot = models.TextField()
    run_time = models.TextField()
    genre = models.TextField()
    released = models.TextField()
    actors = models.TextField()
    director = models.TextField()

    def __str__(self):
        return self.title
