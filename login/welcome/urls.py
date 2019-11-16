from django.urls import include, path
from .views import Register, Login, User

urlpatterns = [
    path('register/', Register.as_view()),
    path('login/', Login.as_view()),
    path('user/', User.as_view()),
]
