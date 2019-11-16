from django.shortcuts import redirect
from rest_framework.views import APIView
from rest_framework.response import Response

from django.http import HttpResponse
from django.views import View
from .models import Users
import json
import hashlib
from .serializers import UserSerializer

class User(View):
    def get(self, request):
        user_id = request.COOKIES['id']
        user_data = Users.objects.filter(id=user_id)
        [ user_response := {'nombre': u.firstname, 'apellido':u.lastname, 'email':u.email } for u in user_data ]
        return HttpResponse(json.dumps(user_response), content_type="application/json")


class Login(View):
    def post(self, request):
        response_data = {}
        try:
            hash_pass = hashlib.sha1(request.POST['password'].encode())
            hash_pass = hash_pass.hexdigest()
            user_exist = Users.objects.filter(email=request.POST['email'], password=hash_pass).first()
            if user_exist:
                response = redirect('http://localhost/perfil')
                response.set_cookie(key='id', value=user_exist.id)
                return response
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
            if not len(user_exist):
                hash_pass = hashlib.sha1(request.POST['password'].encode())
                hash_pass = hash_pass.hexdigest()
                user = Users(
                    firstname=request.POST['nombre'], lastname=request.POST['apellido'], 
                    email=request.POST['email'], password=hash_pass, 
                    sex=request.POST['genero'], born_date=request.POST['date'],
                )

                user.save()
                response = redirect('http://localhost/login')
                return response
            else:
                response_data['error'] = 'user already exist'
        except:
            raise ValueError('500 error server')
        
        return HttpResponse(json.dumps(response_data), content_type="application/json")