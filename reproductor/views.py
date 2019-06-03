from django.shortcuts import render
from django.views import View
from ftplib import FTP
from .models import Song
from os import path as Path
import hashlib

class Song(View):
    destination = '/songs/'
    ftp = FTP()
    ftp.set_debuglevel(2)
    ftp.connect('ftp-song', 21)
    ftp.login('copycat','quetepasaman1234')

    def post(self, request):
        response = {}
        try:
            song_name = request.POST['name']
            #hash_pass = hashlib.sha1( bytes(request.POST['password'], 'utf-8'))
            #hash_pass = hash_pass.hexdigest()
            save_model = Song(
                name = song_name,
                artist = request.P|T['artist'],
                album = request.POST['album'],
                gender = request.POST['gender'],
                image = request.FILES['image'],
                path = destination,
            )

            song = request.FILES['file']
            self.cwd(destination)
            self.ftp.storbinary('STOR %s' % song_name, song, 1024)

            response['ok'] = 'song uploaded'
            #response[] save state if any error occur
            save_model.save()
        except:
            raise ValueError('error: params')

        return HttpResponse(json.dumps(response), content_type="application/json")

    def get(self, request, *args, **kwargs):
        res = {}
        song_name = self.kwargs['song']
        r = BytesIO()
        model_song = Song.objects.get(name=song_name)
        location_song = '%s%s' % destination % song_name # get song location in ftp server reading the model path
        self.ftp.retrbinary('RETR %s' % location_song % , r.write)
        song.name = self.song_name
        response = HttpResponse()
        response.write(r.read())
        response['Content-Type'] ='audio/wav'
        response['Content-Length'] = Path.getsize(location_song)
        return response
