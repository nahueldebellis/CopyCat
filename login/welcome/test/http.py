from django.test import Client

class Http():
    def __init__(self):
        self.response = None
        self.client = Client()

    def post(self, uri, body):
        response = self.client.post(uri, body)
        self.response = response
        return response.content.decode("utf-8") 

    def get(self, uri):
        response = self.client.get(uri)
        self.response = response
        return response.content.decode("utf-8") 