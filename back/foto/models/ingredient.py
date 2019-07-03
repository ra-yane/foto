from peewee import *

from ..core import db


class Ingredient(Model):
    code = CharField(primary_key=True)
    name = CharField()

    class Meta:
        table_name = 'ingredients'
        database = db
        schema = 'skus'


with db:
    Ingredient.create_table(fail_silently=True)