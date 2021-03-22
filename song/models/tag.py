from django.db.models import CharField

from deezer.models import IdPrimaryKeyModel


class Tag(IdPrimaryKeyModel):
    name = CharField(max_length=50)

    class Meta:
        db_table = 'song_tag'
