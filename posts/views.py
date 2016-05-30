from django.http import HttpResponse
from django.shortcuts import render
from .models import Post

# Create your views here.


def post_detail(request):
    context = {
        "title": "detail"
    }

    return render(request, "posts/detail.html", context)


def post_create(request):

    return HttpResponse("")


def post_list(request):
    query_set = Post.objects.all()

    context = {
        "title": "list",
        "query_set": query_set
    }

    return render(request, "posts/index.html", context)


def post_update(request):

    return HttpResponse("")


def post_delete(request):

    return HttpResponse("")
