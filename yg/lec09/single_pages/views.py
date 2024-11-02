from django.shortcuts import render

# Create your views here.
def landing_page(request):
    return render(request, 'single_pages/landing.html', {'title':'Home'})


def about_yugyeong(request):
    return render(request, 'single_pages/teamkyg.html', {'title':'About Yugyeong'})


def about_junhyeok(request):
    return render(request, 'single_pages/teamsjh.html', {'title':'About Junhyeok'})


def blog_lsit(request):
    post_list = [
        {
            'title': 'First Post',
            'content': 'This is my first post'
        },
        {
            'title': 'Second Post',
            'content': 'This is my post'
        },
    ]
    return render(request, 'single_pages/blog.html', {'title': 'blog list', 'posts': post_list})