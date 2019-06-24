from django.contrib import admin
from django.urls import path
from .views import Song

urlpatterns = [
    path('<slug:song_name>/', Search.as_view()), #<str:id>/
    path('songs/<slug:song_name>', Song.as_view()), #<str:id>/
]
