from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, EmailField, JSONField

from deezer.models import IdPrimaryKeyModel
from django.utils.translation import gettext as _

from user.constant import AccountTypeChoices, AccountType


class User(AbstractUser, IdPrimaryKeyModel):
    email = EmailField(null=True, blank=True)
    name = CharField(max_length=256, blank=True)
    account_type = CharField(choices=AccountTypeChoices, max_length=1, default=AccountType.FACEBOOK)
    related_id = CharField(max_length=256, blank=True)
    picture = CharField(max_length=1000, blank=True)

    username = None
    first_name = None
    last_name = None

    USERNAME_FIELD = 'id'
    REQUIRED_FIELDS = ['related_id', 'account_type']

    class Meta:
        db_table = 'user'
        ordering = ['id']
        verbose_name = _("User")
        verbose_name_plural = _("Users")
