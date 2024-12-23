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
    path('timetable', views.timetable, name="timetable"),
    path('wizard', views.wizard, name="wizard"),
    path('event', views.event, name="event"),
    path('cookie', views.cookie, name="cookie"),
    path('review', views.review, name="review"),
    path('single_pages/index/', views.index, name='index'),
    ]