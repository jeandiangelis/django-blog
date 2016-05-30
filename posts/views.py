from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.


def post_detail(request, id=None):
    post = get_object_or_404(Post, id=id)
    context = {
        "title": "detail",
        "post": post
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
