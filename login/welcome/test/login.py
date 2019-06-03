from django.test import TestCase
from .http import Http

class Login(TestCase):
    def log(self):
        uri = '/welcome/login/'
        body = {
            'email': 'debellisnahuel@gmail.com',
            'password': '123456789'
        }
        
        http = Http()
        content = http.post(uri, body)
        print(content)
        self.assertEqual(content, '{"ok": "user logged"}')