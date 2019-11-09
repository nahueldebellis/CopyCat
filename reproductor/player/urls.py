from django.contrib import admin
from django.urls import path
from .views import Song, Search

urlpatterns = [
    path('search/<slug:song_name>/', Search.as_view()), #<str:id>/
    path('player/<int:song_id>/', Song.as_view()), #<str:id>/
]
