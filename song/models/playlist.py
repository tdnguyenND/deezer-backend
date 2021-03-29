from django.db.models import CharField, ForeignKey, CASCADE

from deezer.models import IdPrimaryKeyModel
from user.models import User


class Playlist(IdPrimaryKeyModel):
	name = CharField(max_length=50)
	owner = ForeignKey(to=User, on_delete=CASCADE)

	class Meta:
		db_table = 'playlist'
