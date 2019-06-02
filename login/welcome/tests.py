from django.test import TestCase, Client

class Login(TestCase):
    def log(self):
        client = Client()
        response = client.post(
            '/welcome/login', 
            {
                'email': 'debellisnahuel@gmail.com',
                'password': '123456789'
            }
        )
        print(response.content)
        self.assertEqual(response.content, "{'ok': 'user logged'}")


class Register():
    pass

