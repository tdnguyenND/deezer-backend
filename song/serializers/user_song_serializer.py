from rest_framework.serializers import ModelSerializer

from song.models import Song


class UserSongSerializer(ModelSerializer):
    class Meta:
        model = Song
        fields = ['id', 'title', 'artist', 'album', 'picture_url', 'song_url']
