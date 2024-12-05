from django.shortcuts import render

# Create your views here.
def landing(request):
    return render(request,'single_pages/landing.html', {'title':'Home'})

def about_me(request):
    return render(request,'single_pages/about_me.html', {'title':'About Me'})

def blog_list(request):
    post_list = [
        {
            'title' : 'First Post',
            'content': 'This is my first post'
        },
        {
            'title' : 'Second Post',
            'content': 'This is my second post'
        }
    ]
    return render(request, 'single_pages/blog.html', {'title': 'Blog List', 'posts': post_list})


def about_yg(request):
    return render(request, 'single_pages/about_yg.html')


def about_jh(request):
    return render(request, 'single_pages/about_jh.html')