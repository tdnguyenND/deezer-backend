from django.db.models import CharField, ForeignKey, CASCADE

from deezer.models import IdPrimaryKeyModel
from user.models import User


class Song(IdPrimaryKeyModel):
    title = CharField(max_length=50)
    artist = CharField(max_length=50)
    picture_url = CharField(max_length=1000)
    song_url = CharField(max_length=1000)
    album = CharField(max_length=50)

    owner = ForeignKey(to=User, on_delete=CASCADE)

    class Meta:
        db_table = 'song_song'
