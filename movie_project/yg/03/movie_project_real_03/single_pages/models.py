# single_pages/models.py

from django.db import models

class MovieLocation(models.Model):
    location_name = models.CharField(max_length=100)

    def __str__(self):
        return self.location_name


class Movie(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Location(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    




    
# MovieLocation을 문자열로 참조하여 순환 임포트 방지
class Showtime(models.Model):
    movie = models.ForeignKey('single_pages.Movie', on_delete=models.CASCADE, related_name='single_pages_showtimes')
    showtime = models.DateTimeField()


    def __str__(self):
        return f"{self.movie.title} at {self.showtime} in {self.location}"



