from django.urls import include, path
from .views import Register, Login

urlpatterns = [
    path('register/', Register.as_view()),
    path('login/', Login.as_view()),
]
