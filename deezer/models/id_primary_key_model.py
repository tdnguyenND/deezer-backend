from django.db.models import BigAutoField, Model


class IdPrimaryKeyModel(Model):
    id = BigAutoField(primary_key=True, db_index=True, unique=True)

    class Meta:
        abstract = True
