from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', 'posts.views.post_list'),
    url(r'^create/$', 'posts.views.post_create'),
    url(r'^detail/$', 'posts.views.post_detail'),
    url(r'^delete/$', 'posts.views.post_delete'),
    url(r'^update/$', 'posts.views.post_update'),
]
