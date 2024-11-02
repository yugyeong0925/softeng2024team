from django.urls import path
from . import views



app_name = "single_pages"



urlpatterns = [
    path("",views.landing_page, name='landing_page'),
    path("about_yugyeong/", views.about_yugyeong, name='about_yugyeong'),
    path("about_junhyeok/", views.about_junhyeok, name='aobut_junhyeok')
]
