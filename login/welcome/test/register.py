from django.test import TestCase
from .http import Http

class Register(TestCase):
    def new_user(self):
        uri = '/welcome/register/'
        body = {
            'nombre': 'nahuel',
            'apellido': 'de bellis',
            'sex': 'masc',
            'date': '27-12-2000',
            'email': 'debellisnahuel@gmail.com',
            'password': '123456789'
        }
        http = Http() 
        content = http.post(uri, body)
        self.assertEqual(content, '{"error": "user already exist"}')

