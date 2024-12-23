from django.db import models
from datetime import timedelta


class Location(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class MovieChain(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    release_date = models.DateField()
    image = models.ImageField(upload_to='movie_images/', blank=True, null=True)  # 이미지 필드 추가
    cookie_status = models.BooleanField(default=False)
    naver_link = models.URLField(blank=True, null=True)
    movie_chain = models.ForeignKey(MovieChain, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']  # 영화 제목을 기준으로 가나다 순으로 정렬


class MovieLocation(models.Model):
    chain = models.ForeignKey(MovieChain, on_delete=models.CASCADE, related_name='locations')
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=300, blank=True, null=True)

    def __str__(self):
        return f"{self.chain.name} - {self.name}"


class Showtime(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    show_date = models.DateField()  # 날짜 필드 추가
    show_time = models.TimeField()  # 시간 필드 추가
    location = models.ForeignKey(MovieLocation, on_delete=models.CASCADE, null=True, blank=True)  # 장소 필드 추가
    duration = models.IntegerField(default=120, blank=True, null=True)  # 예시로 120분을 기본값으로 설정

    @property
    def end_time(self):
        from datetime import datetime, timedelta
        # 영화의 시작 시간과 러닝타임을 더해 종료 시간 계산
        start_time = datetime.combine(datetime.today(), self.show_time)
        end_time = start_time + timedelta(minutes=self.duration)
        return end_time.time()

    def __str__(self):
        return f"{self.movie.title} - {self.show_date} {self.show_time} - {self.location.name}"
