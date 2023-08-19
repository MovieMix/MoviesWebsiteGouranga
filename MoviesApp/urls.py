from django.contrib import admin
from django.urls import path,include
from MoviesApp import views

urlpatterns = [   
    path('', views.movies,name="movies"),
    path('home/', views.home,name="home"),
    path('search/', views.search,name="search"),
    path('about/', views.about,name="about"),
    path('ohmygod/', views.ohmygod,name="ohmygod"),
    path('oppenheimer/', views.oppenheimer,name="oppenheimer"),
    path('rrr/', views.rrr,name="rrr"),
    path('it/', views.it,name="it"),
    path('omg2/', views.omg2,name="omg2"),
    path('gadar2/', views.gadar2,name="gadar2"),
    path('idiots3/', views.idiots3,name="idiots3"),
    path('it2/', views.it2,name="it2")
    
]
# path('moviename/', views.moviename,name="moviename")