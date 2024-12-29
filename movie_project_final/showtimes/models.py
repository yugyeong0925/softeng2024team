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
    image = models.ImageField(upload_to='movies/', blank=True, null=True)
    cookie_status = models.BooleanField(default=False)
    naver_link = models.URLField(blank=True, null=True)
    duration = models.IntegerField(default=120, blank=True, null=True)

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

    @property
    def end_time(self):
        """
        영화의 시작 시간(show_time)과 Movie 모델의 duration(러닝타임)을 더해 종료 시간을 계산합니다.
        """
        from datetime import datetime, timedelta

        # 영화의 시작 시간과 날짜를 결합하여 시작 시간을 생성합니다.
        start_time = datetime.combine(self.show_date, self.show_time)
        
        # 영화에 설정된 duration(러닝타임)을 더하여 종료 시간을 계산합니다.
        end_time = start_time + timedelta(minutes=self.movie.duration + 10)
        
        # 종료 시간을 시간:분 형식으로 반환합니다.
        return end_time.time()

    def __str__(self):
        return f"{self.movie.title} - {self.show_date} {self.show_time} - {self.location.name if self.location else 'No Location'}"
    
    class Meta:
        # 기본적으로 날짜(show_date)와 시간(show_time)을 기준으로 정렬
        ordering = ['show_date', 'show_time']