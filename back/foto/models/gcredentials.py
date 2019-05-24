from peewee import *

from ..core import db
from .user import User


class GCredentials(Model):
    id = PrimaryKeyField()
    user = ForeignKeyField(User, unique=True)
    token = CharField()
    refresh_token = CharField(null=True)
    token_uri = CharField()
    client_id = CharField()
    client_secret = CharField()
    scopes = CharField()

    class Meta:
        database = db


with db:
    GCredentials.create_table(fail_silently=True)
