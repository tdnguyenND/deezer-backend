from django.db.models import CharField

from deezer.models import IdPrimaryKeyModel


class Artist(IdPrimaryKeyModel):
    name = CharField(max_length=1000)

    class Meta:
        db_table = 'artist'
