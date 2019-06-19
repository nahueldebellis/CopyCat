from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from ftplib import FTP
from .models import Song as song
from os import path as Path
import json

class Song(View):
    destination = '/songs/'
    ftp = FTP()
    ftp.set_debuglevel(2)
    ftp.connect('ftp-song', 21)
    ftp.login('copycat','quetepasaman1234')

    def post(self, request):
        response = {}

        song_name = request.POST['name']
        #hash_pass = hashlib.sha1( bytes(request.POST['password'], 'utf-8'))
        #hash_pass = hash_pass.hexdigest()
        save_model = song(
            name = song_name,
            author = request.POST['artist'],
            album = request.POST['album'],
            duration = request.POST['duration'],
            gender = request.POST['gender'],
            year = request.POST['year'],
            #image = request.FILES['image'],
            path = self.destination,
        )
        save_model.save()

        song_file = request.FILES['file']
        self.ftp.cwd(self.destination)
        self.ftp.storbinary('STOR %s.wav' % song_name, song_file)

        response['ok'] = 'song uploaded'
        #response[] save state if any error occur


        return HttpResponse(json.dumps(response), content_type="application/json")

    def get(self, request, *args, **kwargs):
        #return render(request, 'player/index.html')
        res = {}
        song_name = self.kwargs['s']
        r = BytesIO()
        model_song = Song.objects.get(name=song_name)
        location_song = '%s%s.wav' % (self.destination, song_name) # get song location in ftp server reading the model path
        self.ftp.retrbinary('RETR %s' % location_song, r.write)
        song.name = self.song_name
        response = HttpResponse()
        response.write(r.read())
        response['Content-Type'] ='audio/wav'
        response['Content-Length'] = Path.getsize(location_song)
        return response
