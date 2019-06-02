from django.http import HttpResponse
from django.views import View
from .models import Users
import json
import hashlib


class Login(View):
    def post(self, request):
        response_data = {}
        try:
            hash_pass = hashlib.sha1( bytes(request.POST['password'], 'utf-8'))
            hash_pass = hash_pass.hexdigest()
            user_exist = Users.objects.filter(email=request.POST['email'], password=hash_pass)
            if user_exist != [] or cookie:
                response_data['ok'] = 'user logged'
            else:
                response_data['error'] = 'email or password wrong'
        except:
            raise ValueError('error, email or password wrong')

        return HttpResponse(json.dumps(response_data), content_type="application/json")

class Register(View): 
    def post(self, request):
        response_data = {}
        try:
            user_exist = Users.objects.filter(email=request.POST['email'])
            if user_exist == []:
                hash_pass = hashlib.sha1( bytes(request.POST['password'], 'utf-8'))
                hash_pass = hash_pass.hexdigest()
                user = Users(
                    firstname=request.POST['nombre'], lastname=request.POST['apellido'], 
                    email=request.POST['email'], password=hash_pass, 
                    sex=request.POST['genero'], born_date=request.POST['date'],
                )

                user.save()
                response_data['ok'] = 'user saved'
            else:
                response_data['error'] = 'user already exist'
        except:
            raise ValueError('500 error server')
        
        return HttpResponse(json.dumps(response_data), content_type="application/json")