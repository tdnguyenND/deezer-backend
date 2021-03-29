import re

from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from deezer.settings import UPLOAD_SONG_FORM_ARTIST_DELIMITERS
from deezer.view_sets import AuthenticatedGenericViewSet
from song.functions import artist_from_name
from song.models import Song, SongArtist
from song.serializers import UserSongSerializer
from song.services import upload_song_to_storage, upload_picture_to_storage


class SongViewSet(AuthenticatedGenericViewSet, RetrieveModelMixin, ListModelMixin):
    queryset = Song.objects.all()
    serializer_class = UserSongSerializer

    @action(methods=['post'], detail=False, url_path='upload')
    def upload_song(self, request):
        request_data = request.data
        audio_file = request.FILES.getlist('audio_file')[0]
        song_url = upload_song_to_storage(audio_file)

        picture_file = request.FILES.getlist('picture_file')[0]
        picture_url = upload_picture_to_storage(picture_file)
        artists = map(lambda s: artist_from_name(' '.join(s.split())),
                      re.split(UPLOAD_SONG_FORM_ARTIST_DELIMITERS, request_data.get('artist')))

        title = request_data.get('title')
        album = request_data.get('album')

        song = Song.objects.create(title=title, album=album, picture_url=picture_url, song_url=song_url,
                                   owner=request.user)
        for artist in artists:
            SongArtist.objects.create(song=song, artist=artist)

        return Response(UserSongSerializer(song).data)

    @action(methods=['get'], detail=False, url_path='discovery', permission_classes=[AllowAny])
    def get_discovery_list(self, request, *args, **kwargs):
        qs = self.get_queryset()[:min(50, self.get_queryset().count())]
        return Response(self.get_serializer(qs, many=True).data)

    @action(methods=['get'], detail=False, url_path='history', permission_classes=[AllowAny])
    def get_history_list(self, request, *args, **kwargs):
        qs = self.get_queryset()[:min(50, self.get_queryset().count())]
        return Response(self.get_serializer(qs, many=True).data)

    @action(methods=['get'], detail=False, url_path='test', permission_classes=[AllowAny])
    def test(self, request, *args, **kwargs):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            field = 'HTTP_X_FORWARDED_FOR'
            ip = x_forwarded_for.split(',')[0]
        else:
            field = 'REMOTE_ADDR'
            ip = request.META.get('REMOTE_ADDR')
        return Response({'ip': ip, 'field': field})
