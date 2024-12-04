from django.urls import path
from . import views


app_name = "single_pages"


urlpatterns = [
    path('about_me/', views.about_me, name='about_me'),
    path('', views.landing, name='landing_pages'),
    path('about_yg/', views.about_yg, name='about_yg'),
    path('about_jh/', views.about_jh, name='about_jh'),
]