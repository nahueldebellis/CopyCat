from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
from .models import Users
import json

@method_decorator(csrf_exempt, name="post")
class Login(View):
    def post(self, request):
        response_data = {}
        try:
            user = Users.objects.get(email=request.POST['email'], password=request.POST['password'])
            if user:
                response_data['ok'] = 'user logged'
            else:
                raise ValueError('error, email or password wrong')
        except:
            response_data['error'] = 'email or password wrong'

        return HttpResponse(json.dumps(response_data), content_type="application/json")

@method_decorator(csrf_exempt, name="post")
class Register(View): 
    def post(self, request):
        response_data = {}
        user_exist = False #Users.objects.get(email=request.POST['email'])
        
        user = Users(
            firstname=request.POST['nombre'], lastname=request.POST['apellido'], 
            email=request.POST['email'], password=request.POST['password'], 
            sex=request.POST['genero'], born_date=request.POST['date'],
        )

        user.save()
        response_data['ok'] = 'user saved'
        
        return HttpResponse(json.dumps(response_data), content_type="application/json")