from django.test import TestCase, Client
import wave
import os
from io import BytesIO
# Create your tests here.

TESTDATA_FILENAME = os.path.join(os.path.dirname(__file__), 'europa.wav')

class Player(TestCase):      
    def upload(self):
        client = Client() # setup
        chunk = 1024 # setup
        binary_song = b'' # setup
        with open(TESTDATA_FILENAME, 'rb') as data: # if doesn't work then use wave.open to read binary data
            binary_song = data.read()

        song = binary_song
        
        response = client.post('/player/songs/', { 
            'name': 'europa', 
            'duration': 123,
            'year': 2021,
            'author': 'las ligas menores', 
            'album': 'las ligas menores', 
            'gender': 'rock', 
            'file': song
        })

        print(response)
        self.assertEqual(response.status_code, 201)



