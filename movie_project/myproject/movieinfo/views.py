from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse
from .models import Movie, Review

def index(request):
    movies = [
        {"title": "영화1", "poster_url": "https://via.placeholder.com/150", "cinema": "CGV 전주", "rating": 4.5},
        {"title": "영화2", "poster_url": "https://via.placeholder.com/150", "cinema": "메가박스 전주", "rating": 4.0},
        {"title": "영화3", "poster_url": "https://via.placeholder.com/150", "cinema": "롯데시네마 전주", "rating": 3.8},
    ]
    reviews = [
        {"movie_title": "영화1", "text": "아주 재미있어요!", "author": "사용자1"},
        {"movie_title": "영화2", "text": "조금 지루했어요.", "author": "사용자2"},
        {"movie_title": "영화3", "text": "액션이 멋졌습니다.", "author": "사용자3"},
    ]
    return render(request, 'movieinfo/index.html', {'movies': movies, 'reviews': reviews})

@login_required
def create_review(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    if request.method == "POST":
        Review.objects.create(
            movie=movie,
            user=request.user,
            rating=int(request.POST['rating']),
            content=request.POST['content']
        )
        return redirect('movie_detail', movie_id=movie.id)
    return render(request, 'movieinfo/create_review.html', {'movie': movie})

@login_required
def update_review(request, review_id):
    review = get_object_or_404(Review, id=review_id, user=request.user)
    if request.method == "POST":
        review.rating = int(request.POST['rating'])
        review.content = request.POST['content']
        review.save()
        return redirect('movie_detail', movie_id=review.movie.id)
    return render(request, 'movieinfo/update_review.html', {'review': review})

@login_required
def delete_review(request, review_id):
    review = get_object_or_404(Review, id=review_id, user=request.user)
    if request.method == "POST":
        review.delete()
        return redirect('movie_detail', movie_id=review.movie.id)
    return render(request, 'movieinfo/delete_review.html', {'review': review})

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password_confirm = request.POST['password_confirm']
        if password != password_confirm:
            messages.error(request, '비밀번호가 일치하지 않습니다.')
        else:
            try:
                user = User.objects.create_user(username=username, password=password)
                login(request, user)
                messages.success(request, '회원가입이 완료되었습니다.')
                return redirect('index')
            except:
                messages.error(request, '회원가입에 실패했습니다. 사용자명을 확인하세요.')
    return render(request, 'register.html')  # 전역 템플릿

def user_login(request):
    if request.method == 'POST':
        user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user is not None:
            login(request, user)
            return redirect('index')
        messages.error(request, '로그인 실패: 사용자명이나 비밀번호가 틀립니다.')
    return render(request, 'login.html')  # 전역 템플릿

@login_required
def user_logout(request):
    logout(request)
    return redirect('index')

@login_required
def profile(request):
    return render(request, 'profile.html')  # 전역 템플릿

def movie_detail(request, movie_id):
    # 영화 ID에 따라 데이터를 가져옵니다 (임시 예시 데이터)
    movie = {
        "id": movie_id,
        "title": "Example Movie",
        "cinema": "CGV",
        "rating": 4.5,
    }
    return render(request, "movieinfo/movie_detail.html", {"movie": movie})
