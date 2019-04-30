from django.urls import path 
from . import views

urlpatterns = [
    path('expresion/', views.Calculator.as_view()),
]