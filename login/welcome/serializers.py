from .models import User

class User():
    class Meta:
        model = User
        fields = ('firstname', 'lastname', 'email', 'sex', 'password')