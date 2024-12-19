from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=100)
    cinema = models.CharField(max_length=50)
    rating = models.FloatField()
    poster_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title


    def __str__(self):
        return self.title

class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="reviews")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()  # 1~5
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.movie.title} - {self.user.username}"
