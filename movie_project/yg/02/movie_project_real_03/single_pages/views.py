from django.shortcuts import render
from showtimes.models import Movie  # showtimes 앱에서 Movie 모델을 가져옵니다.


# single_pages/views.py
from showtimes.models import Movie  # Movie 모델 임포트

def movie_list(request):
    # 검색어 가져오기 (GET 요청에서 'search' 파라미터를 가져옴)
    query = request.GET.get('search', '')  # 검색어가 없다면 빈 문자열로 초기화

    # 영화 목록 가져오기
    if query:
        # 검색어가 있을 경우, 영화 제목에서 검색
        movies = Movie.objects.filter(title__icontains=query)  # 제목에 검색어가 포함된 영화 찾기
    else:
        # 검색어가 없으면 전체 영화 목록
        movies = Movie.objects.all()
    return render(request, 'single_pages/movie_list.html', {'movies': movies, 'query': query})






def index(request):
    return render(request, 'single_pages/index.html', {'title': 'index'})


def portfolio_details(request):
    return render(request, 'single_pages/portfolio_details.html', {'title' : 'portfolio_details'})


def service_details(request):
    return render(request, 'single_pages/service_details.html', {'title' : 'service_details'})


def starter_page(request):
    return render(request, 'single_pages/starter_page.html', {'title' : 'starter_page'})


def manager(request):
    return render(request, 'single_pages/manager.html', {'title' : 'manager'})


def user(request):
    return render(request, 'single_pages/user.html', {'title' : 'user'})



def wizard(request):
    return render(request, 'single_pages/wizard.html', {'title' : 'wizard'})


def event(request):
    return render(request, 'single_pages/event.html', {'title' : 'event'})


def cookie(request):
    return render(request, 'single_pages/cookie.html', {'title' : 'cookie'})


def review(request):
    return render(request, 'single_pages/review.html', {'title' : 'review'})

