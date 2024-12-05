from django.urls import path
from . import views

app_name="blog"


urlpatterns = [
    path('<int:pk>/', views.PostDetail.as_view()),
    path('',views.PostList.as_view(), name='post_list'),
    # path('<int:pk>/', views.single_post_page),
    # path('', views.index),
]