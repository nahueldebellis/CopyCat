from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
from django.core.files import File
from .models import Song as song
from .serializers import SongSerializer

class Search(APIView):
    queryset = song.objects.all()
    def get(self, request, song_name=""):
        result = song.objects.filter(name=song_name)
        data = [(s.id, s.name, s.album, s.author) for s in result]
        return Response(data) 

class Song(APIView):
    queryset = song.objects.all()
    def post(self, request):
        song_name = request.POST['name']
        save_model = song(
            name = song_name,
            author = request.POST['artist'],
            album = request.POST['album'],
            duration = request.POST['duration'],
            gender = request.POST['gender'],
            year = request.POST['year'],
            file_data = File(request.FILES['file']),
        )

        save_model.save()

        result['ok'] = 'song uploaded'
        return Response(result)

    def get(self, request, song_id=0):
        response = HttpResponse()

        result = song.objects.filter(id=song_id).first()
        song_file = result.file_data.read()


        response.write(song_file)
        response['Content-Type'] = 'audio/wav'
        response['Content-Disposition'] = 'attachment; filename="song.wav"'

        return response

