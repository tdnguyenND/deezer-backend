from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from deezer.view_sets import AuthenticatedGenericViewSet
from song.serializers import PlaylistSerializer
from song.models import Playlist, SongPlaylist, Song


class PlaylistViewSet(AuthenticatedGenericViewSet, RetrieveModelMixin, ListModelMixin):
	queryset = Playlist.objects.all()
	serializer_class = PlaylistSerializer

	def create(self, request, *args, **kwargs):
		name = request.data.get('name')
		user = request.user
		playlist = Playlist.objects.create(user=user, name=name)
		return Response(self.get_serializer(playlist).data)

	@action(methods=['post'], detail=True, url_path='add_to_playlist', permission_classes=[AllowAny])
	def add_song_to_playlist(self, request):
		request_data = request.data
		playlist = self.get_object()
		song = request_data.get('song_id')
		SongPlaylist.objects.create(playlist=playlist, song=song)
		return Response(PlaylistSerializer(playlist).data)
