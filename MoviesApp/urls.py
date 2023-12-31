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
    path('Interstellar/', views.Interstellar,name="Interstellar"),
    path('ninele/', views.ninele,name="ninele"),
    path('thorloveandthunder/', views.thorloveandthunder,name="thorloveandthunder"),
    path('incrediblehulk/', views.incrediblehulk,name="incrediblehulk"),
    path('thorthedarkworld/', views.thorthedarkworld,name="thorthedarkworld"),
    path('captainamericathewintersoldie/', views.captainamericathewintersoldie,name="captainamericathewintersoldie"),
    path('jollyllb/', views.jollyllb,name="jollyllb"),
    path('jollyllb2/', views.jollyllb2,name="jollyllb2"),
    path('omg2/', views.omg2,name="omg2"),
    path('pushpa/', views.pushpa,name="pushpa"),
    path('gadar2/', views.gadar2,name="gadar2"),
    path('kashmirfiles/', views.kashmirfiles,name="kashmirfiles"),
    path('idiots3/', views.idiots3,name="idiots3"),
    path('avatar/', views.avatar,name="avatar"),
    path('avatar2/', views.avatar2,name="avatar2"),
    path('thorragnarok/', views.thorragnarok,name="thorragnarok"),
    path('thor/', views.thor,name="thor"),
    path('ironman3/', views.ironman3,name="ironman3"),
    path('avengers2012/', views.avengers2012,name="avengers2012"),
    path('ironman/', views.ironman,name="ironman"),
    path('bhoolbhulaiyaa/', views.bhoolbhulaiyaa,name="bhoolbhulaiyaa"),
    path('bhoolbhulaiyaa2/', views.bhoolbhulaiyaa2,name="bhoolbhulaiyaa2"),
    path('captainamericathefirstavenger/', views.captainamericathefirstavenger,name="captainamericathefirstavenger"),
    path('keralastory/', views.keralastory,name="keralastory"),
    path('raazi/', views.raazi,name="raazi"),
    path('pushpa2/', views.pushpa2,name="pushpa2"),
    path('it2/', views.it2,name="it2")
    
]
# path('moviename/', views.moviename,name="moviename")