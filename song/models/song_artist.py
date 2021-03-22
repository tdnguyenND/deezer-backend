from django.db.models import ForeignKey, CASCADE

from deezer.models import IdPrimaryKeyModel
from song.models import Song, Artist


class SongArtist(IdPrimaryKeyModel):
    song = ForeignKey(to=Song, on_delete=CASCADE)
    artist = ForeignKey(to=Artist, on_delete=CASCADE)

    class Meta:
        db_table = 'song_artist'
