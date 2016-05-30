from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def post_detail(request):

    return HttpResponse("<h1>Hello world!</h1>")


def post_create(request):

    return HttpResponse("")


def post_list(request):

    return HttpResponse("")


def post_update(request):

    return HttpResponse("")


def post_delete(request):

    return HttpResponse("")
