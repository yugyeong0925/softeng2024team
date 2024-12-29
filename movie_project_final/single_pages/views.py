from django.shortcuts import render, get_object_or_404, redirect
from showtimes.models import Movie  # showtimes 앱에서 Movie 모델을 가져옵니다.
from django.http import JsonResponse
from .models import MovieLocation, Review
from django.http import Http404




def confirm_selection(request):
    if request.method == 'POST':
        selected_movies = request.POST.getlist('selected_movies')  # 선택된 영화들의 ID 리스트
        # 선택된 영화들을 처리 (예: DB 저장, 다른 처리 등)
        movies = Movie.objects.filter(id__in=selected_movies)
        # 선택된 영화들을 보여줄 템플릿을 렌더링
        return render(request, 'single_pages/selected_movies.html', {'movies': movies})
    else:
        return redirect('single_pages:movie_list')  # GET 요청 시 영화 목록 페이지로 리디렉션
    

def wizard_view(request):
    # 영화 목록을 전달
    movies = Movie.objects.all()
    return render(request, 'single_pages/wizard.html', {'movies': movies})


def showtimes_selected(request):
    # 선택된 영화들이 form에서 넘어왔다고 가정 (예: POST 요청으로 넘어옴)
    selected_movie_ids = request.POST.getlist('movies')  # 여러 개의 영화 ID를 받음
    movies = Movie.objects.filter(id__in=selected_movie_ids)  # 선택된 영화들만 가져옴
    
    return render(request, 'your_template_path/showtimes_selected.html', {'movies': movies})


def movie_showtimes_selected(request):
    if request.method == "POST":
        # 선택된 영화들 받아오기
        selected_movie_ids = request.POST.getlist('selected_movies')
        
        # 선택된 영화들이 있으면
        if selected_movie_ids:
            # 선택된 영화들 불러오기
            movies = Movie.objects.filter(id__in=selected_movie_ids)
            return render(request, 'single_pages/showtimes_selected.html', {'movies': movies})
        else:
            return Http404("선택된 영화가 없습니다.")
    else:
        return redirect('single_pages:wizard')  # GET 요청 시 wizard 페이지로 리디렉션
    

def movie_review(request):
    movies = Movie.objects.all()  # showtimes 앱에서 Movie 객체를 가져옵니다.

    if request.method == "POST":
        movie_id = request.POST.get('movie')  # 영화 ID를 가져옵니다.
        review_text = request.POST.get('review_text')  # 리뷰 텍스트를 가져옵니다.

        try:
            # movie_id로 Movie 객체를 가져옵니다.
            movie = Movie.objects.get(id=movie_id)
        except Movie.DoesNotExist:
            # 만약 Movie 객체가 없다면 에러 메시지를 반환합니다.
            return render(request, 'single_pages/review.html', {'movies': movies, 'error': '영화를 찾을 수 없습니다.'})

        # Review 객체를 생성하고 저장합니다.
        review = Review(movie=movie, review_text=review_text)
        review.save()

        return redirect('single_pages:review')  # 리뷰 작성 후 리다이렉트

    return render(request, 'single_pages/review.html', {'movies': movies})



def movie_list(request):
    # 영화 목록을 가져옴
    movies = Movie.objects.all()  # 모든 영화 가져오기

    # 템플릿 선택 (조건에 따라 변경 가능)
    template_name = 'single_pages/movie_list.html'  # 기본 템플릿

    if 'wizard' in request.GET:  # URL에 'wizard' 파라미터가 있다면
        template_name = 'single_pages/wizard.html'  # wizard 템플릿 사용

    return render(request, template_name, {'movies': movies})



def movie_showtimes(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    showtimes = movie.showtime_set.all()  # showtime_set은 Movie와 Showtime의 관계 이름
    return render(request, 'single_pages/movie_showtimes.html', {'movie': movie, 'showtimes': showtimes})




def get_locations(request, chain_id):
    locations = MovieLocation.objects.filter(chain_id=chain_id)
    location_data = [{"id": location.id, "name": location.name} for location in locations]
    return JsonResponse({"locations": location_data})




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
    movies = Movie.objects.all()
    return render(request, 'single_pages/wizard.html', {'movies': movies})


def event(request):
    return render(request, 'single_pages/event.html', {'title' : 'event'})


def cookie(request):
    return render(request, 'single_pages/cookie.html', {'title' : 'cookie'})


def review(request):
    return render(request, 'single_pages/review.html', {'title' : 'review'})

