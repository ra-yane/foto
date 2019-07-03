from peewee import *

from ..models import Ingredient

def select_all_ingredints():
    ingredients = Ingredient.select()
    lst = []
    for ing in ingredients:
        lst.append({'code': ing.code, 'name': ing.name})
    return lst