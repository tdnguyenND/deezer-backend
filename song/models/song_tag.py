from django.db.models import ForeignKey, CASCADE

from deezer.models import IdPrimaryKeyModel
from song.models.song import Song
from song.models.tag import Tag


class SongTag(IdPrimaryKeyModel):
    song = ForeignKey(to=Song, on_delete=CASCADE)
    tag = ForeignKey(to=Tag, on_delete=CASCADE)

    class Meta:
        db_table = 'song_song_tag'
