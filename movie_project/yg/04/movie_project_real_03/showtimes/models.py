from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    release_date = models.DateField()
    image = models.ImageField(upload_to='movie_images/', blank=True, null=True)  # 이미지 필드 추가

    def __str__(self):
        return self.title

class Showtime(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    show_time = models.DateTimeField()

    def __str__(self):
        return f"Showtime for {self.movie.title} at {self.show_time}"
