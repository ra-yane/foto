from flask_jwt_extended import jwt_required
from flask_restful import Resource, request

from ..managers import ingredient


class Ingredients(Resource):

    def get(self):
        ingredient_list = ingredient.select_all_ingredints()
        return {'msg': 'success', 'ingredients': ingredient_list}