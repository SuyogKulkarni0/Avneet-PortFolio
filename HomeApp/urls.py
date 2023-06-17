from django.contrib import admin
from django.urls import path
from HomeApp import views

urlpatterns = [
    path('',views.index,name='Home'),
    path('about',views.about,name='about'),
    path('dailysoaps',views.dailysoaps,name='services'),
    path('advertisements',views.advertisements,name="Ads"),
    path('movies',views.movies,name='movies'),
    path('albums',views.albums,name='albums'),
    path('contri',views.contri,name='contri'),
    path('contact',views.contact,name='contact')
]
