from django.shortcuts import render
from django.http import HttpResponse


posts = [
    {
        'author': 'Esteban Buniak',
        'title': '1st post',
        'content': 'content for the 1st post',
        'date_posted': 'August 7, 2024'
    },
    {
        'author': 'Esteban Buniak',
        'title': '2nd post',
        'content': 'content for the 2nd post',
        'date_posted': 'August 7, 2024'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
