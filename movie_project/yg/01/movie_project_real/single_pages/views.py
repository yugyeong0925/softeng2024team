from django.shortcuts import render



def index(request):
    return render(request, 'single_pages/index.html', {'title': 'index'})


def portfolio_details(request):
    return render(request, 'single_pages/portfolio_details', {'title' : 'portfolio_details'})


def service_details(request):
    return render(request, 'single_pages/service_details', {'title' : 'service_details'})


def starter_page(request):
    return render(request, 'single_pages/starter_page.html', {'title' : 'starter_page'})


def manager(request):
    return render(request, 'single_pages/manager', {'title' : 'manager'})


def user(request):
    return render(request, 'single_pages/user.html', {'title' : 'user'})


def timetable(request):
    return render(request, 'single_pages/timetable.html', {'title' : 'timetable'})


def wizard(request):
    return render(request, 'single_pages/wizard.html', {'title' : 'wizard'})


def event(request):
    return render(request, 'single_pages/event.html', {'title' : 'event'})


def cookie(request):
    return render(request, 'single_pages/cookie.html', {'title' : 'cookie'})


def review(request):
    return render(request, 'single_pages/review.html', {'title' : 'review'})