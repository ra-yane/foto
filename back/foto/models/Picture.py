from peewee import *
from ..models import Ingredient
from ..core import db


class Picture(Model):
    id = PrimaryKeyField()
    url = CharField()
    code = ForeignKeyField(Ingredient)

    class Meta:
        table_name = 'pictures'
        database = db
        schema = 'skus'


with db:
    Picture.create_table(fail_silently=True)