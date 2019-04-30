from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
import json

class Calculator(View):
    def post(self, request):
        body_unicode = request.body.decode('utf-8')
        body_data = json.loads(body_unicode)
        
        result = eval('{}'.format(body_data['expresion']))
        print(result)
        context = {'result': result}
        return HttpResponse(result)
    def get(self, request):
         return render(request, 'login/calculator.html')


# Create your views here.
def index(request):
    return HttpResponse("<h1>CopyCat</h1>")


        
