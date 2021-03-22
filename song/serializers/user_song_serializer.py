from rest_framework.serializers import ModelSerializer, SerializerMethodField

from song.models import Song, SongArtist


class UserSongSerializer(ModelSerializer):
    artist = SerializerMethodField()

    @staticmethod
    def get_artist(instance):
        return ', '.join(SongArtist.objects.filter(song=instance).values_list('artist__name', flat=True))

    class Meta:
        model = Song
        fields = ['id', 'title', 'artist', 'album', 'picture_url', 'song_url']
