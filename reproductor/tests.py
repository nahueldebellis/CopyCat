from django.test import TestCase, Client
from wave
from io import BytesIO
# Create your tests here.

class Player(TestCase):
    def setUp(self):
        self.song_name = 'europa.wav' # setup
        self.destination = '%s' % self.song_name # setup
        self.client = Client() # setup
        self.chunk = 1024 # setup
        self.binary_song = b'' # setup

    def upload(self):
        with open(self.destination, 'rb') as data: # if doesn't work then use wave.open to read binary data
            byte = data.read(self.chunk)
            while byte:
                self.binary_song = binary+byte
                byte = f.read(self.chunk)

            song = BytesIO(self.binary_song)
            song.name = self.song_name

            response = self.client.post('/player/upload/', {'song': song}, follow=True)
            self.assertEqual(response.status_code, 201)



