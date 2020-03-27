from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

posts = [
    {
        'author' : 'Rajvardhan',
        'title'  : 'The very first blog',
        'content': 'first post content',
        'date_posted' : '27-03-2020'
    },
    {
        'author': 'Sanskar',
        'title': 'The very first blog',
        'content': 'first post content',
        'date_posted': '27-03-2020'
    },
    {
        'author': 'Yash',
        'title': 'The very first blog',
        'content': 'first post content',
        'date_posted': '27-03-2020'
    }
]

def home(request):
    context = {
        'posts' : posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title' : 'About'})
