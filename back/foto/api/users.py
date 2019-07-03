from flask_jwt_extended import jwt_required
from flask_restful import Resource, request

from ..core import logger
from ..managers import users


class Users(Resource):
    """
    Manage the users in the database
    """

    @jwt_required
    def get(self):
        """
        Get the list of users in foto
        :return: list of users
        """
        search = request.args.get('search', None)
        user_list = users.get_all(search=search, max=max)
        logger.debug('Get on /users called. Search : {}.'.format(search))
        return user_list


class User(Resource):
    """
    Manage an user in the database
    """

    @jwt_required
    def get(self, user_id):
        """
        Get an user by its id
        :return: the user demanded
        """
        logger.debug('Get on /users/:id called.')
        return users.get(user_id).get_data()
