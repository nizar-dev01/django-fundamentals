from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def starting_page(request):
    return render(request, "blog/index.html", {
        "title": "First Blog",
        "content": "Blog content of the first blog post."
    })

def posts(request):
    pass

def single_post(request):
    pass