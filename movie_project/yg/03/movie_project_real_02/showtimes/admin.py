# showtimes/admin.py
from django.contrib import admin
from .models import Movie, Showtime

# Movie 모델을 Admin에 등록
admin.site.register(Movie)
admin.site.register(Showtime)
