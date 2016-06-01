from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm

# Create your views here.


def post_detail(request, id=None):
    post = get_object_or_404(Post, id=id)
    context = {
        "title": "detail",
        "post": post
    }

    return render(request, "posts/detail.html", context)


def post_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.save()
        messages.success(request, "Success!")

        return HttpResponseRedirect(post.get_absolute_url())

    context = {
        "form": form,
    }

    return render(request, 'posts/form.html', context)


def post_list(request):
    query_set = Post.objects.all()

    context = {
        "title": "list",
        "query_set": query_set
    }

    return render(request, "posts/list.html", context)


def post_update(request, id=None):
    post = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, instance=post)

    if form.is_valid():
        post = form.save(commit=False)
        post.save()
        messages.success(request, "Success!")
        return HttpResponseRedirect(post.get_absolute_url())

    context = {
        "post": post,
        "form": form
    }

    return render(request, "posts/update.html", context)


def post_delete(request, id=None):
    post = get_object_or_404(Post, id=id)
    post.delete()
    messages.success(request, "Deleted!")

    return redirect("posts:list")
