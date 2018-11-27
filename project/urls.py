from django.conf.urls import url
from . import views

urlpatterns = [
    url('', views.post_list, name='post_list'),
    url('post/new', views.post_new, name='post_new'),
]
