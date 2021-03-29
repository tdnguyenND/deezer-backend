from rest_framework.serializers import ModelSerializer

from song.models.playlist import Playlist
from song.serializers.user_song_serializer import UserSongSerializer
from user.serializers import UserPublicInfoSerializer


class PlaylistSerializer(ModelSerializer):
	owner = UserPublicInfoSerializer()
	song = UserSongSerializer(source='song_playlist__song', many=True)

	class Meta:
		model = Playlist
		fields = ['name', 'owner', 'song']
