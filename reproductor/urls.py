from django.contrib import admin
from django.urls import path
from .views import Song

urlpatterns = [
    path('songs/', Song.as_view()), #<str:id>/
]
