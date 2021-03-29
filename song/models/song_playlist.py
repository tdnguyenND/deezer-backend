from django.db.models import ForeignKey, CASCADE

from deezer.models import IdPrimaryKeyModel
from song.models.song import Song
from song.models.playlist import Playlist


class SongPlaylist(IdPrimaryKeyModel):
	song = ForeignKey(to=Song, on_delete=CASCADE)
	playlist = ForeignKey(to=Playlist, on_delete=CASCADE)

	class Meta:
		db_table = 'song_playlist'
