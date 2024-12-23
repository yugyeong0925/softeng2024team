from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    release_date = models.DateField()
    image = models.ImageField(upload_to='movie_images/', blank=True, null=True)  # 이미지 필드 추가
    cookie_status = models.BooleanField(default=False)
    naver_link = models.URLField(blank=True, null=True)
    

    def __str__(self):
        return self.title
    
    

    class Meta:
        ordering = ['title']  # 영화 제목을 기준으로 가나다 순으로 정렬



class Location(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    




class MovieChain(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class MovieLocation(models.Model):
    chain = models.ForeignKey(MovieChain, on_delete=models.CASCADE, related_name='locations')
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=300, blank=True, null=True)

    def __str__(self):
        return f"{self.chain.name} - {self.name}"


class Showtime(models.Model):
    movie = models.ForeignKey('single_pages.Movie', on_delete=models.CASCADE, related_name='showtimes')
    showtime = models.DateTimeField()
    


    def __str__(self):
        return f"{self.movie.title} at {self.showtime} in {self.location}"
