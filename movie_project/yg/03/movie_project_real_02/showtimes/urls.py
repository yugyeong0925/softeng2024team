# showtimes/urls.py
from django.urls import path
from . import views  # views를 가져오기

urlpatterns = [
    path('add_showtime/', views.add_showtime, name='add_showtime'),  # 이곳에서만 URL 패턴을 정의
]
