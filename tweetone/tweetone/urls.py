from django.conf.urls import patterns, include, url
from django.contrib import admin
from tweetexamp import views



urlpatterns = [
	url(r'^$', views.main, name='main'),
	url(r'^index$', views.index, name='index'),
	url(r'^search$', views.search, name='search'),
	url(r'^search/(?P<id>[a-zA-Z0-9]+)/' , views.comments, name='comments'),
]


