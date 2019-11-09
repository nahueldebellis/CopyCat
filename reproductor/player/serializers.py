from .models import Song
from rest_framework import serializers

class SongSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Song
        fields = ['id', 'name', 'author', 'album']
