from django.urls import path
from . import views

app_name = "single_pages"


urlpatterns = [
    path('', views.index, name="index"),
    path('index/', views.index, name="index"),    
    path('portpolio_details/', views.portfolio_details, name="portpolio_details"),
    path('service_details/', views.service_details, name="service_details"),
    path('starter_page', views.starter_page, name="starter_page"),
    path('manager', views.manager, name="manager"),
    path('user', views.user, name="user"),
    path('wizard', views.wizard, name="wizard"),
    path('event', views.event, name="event"),
    path('cookie', views.cookie, name="cookie"),
    path('review/', views.movie_review, name="review"),
    path('single_pages/index/', views.index, name='index'),
    path('movie_list/', views.movie_list, name='movie_list'),  # 영화 목록 페이지
    path('get_locations/<int:chain_id>/', views.get_locations, name='get_locations'),
    path('movie_showtimes/<int:movie_id>/', views.movie_showtimes, name='movie_showtimes'),
    path('confirm/', views.confirm_selection, name='confirm_selection'),  # 추가된 URL 패턴 
    path('movie_showtimes_selected/', views.movie_showtimes_selected, name='movie_showtimes_selected'),
]
