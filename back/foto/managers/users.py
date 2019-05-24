from peewee import DoesNotExist, IntegrityError
from playhouse.shortcuts import model_to_dict

from ..core import db
from ..exceptions import *
from ..models import User


@db.connection_context()
def get_all(search=None, max=None):
    users = []
    if search is None or search == '':
        query = User.select()
    else:
        query = User.select().where(
            (User.first_name.contains(search)) |
            (User.last_name.contains(search)))
    for user in query:
        users.append(model_to_dict(user))
    logger.debug('Get all users from db. Number of users : {}'.format(len(users)))
    if max is not None:
        users = users[:min([len(users), int(max)])]
    return users


@db.connection_context()
def get(user_id):
    try:
        user = User.get(User.id == user_id)
        logger.debug('Get {} user. Response : {}'.format(user_id, user))
        return user
    except DoesNotExist:
        raise UserNotExisting


@db.connection_context()
def get_by_mail(mail):
    with db.transaction():
        try:
            user = User.get(User.email == mail)
            logger.debug('Get {} user. Response : {}'.format(mail, user))
            return user
        except DoesNotExist:
            raise UserNotExisting


@db.connection_context()
def add_user(email, first_name, last_name):
    with db.atomic():
        try:
            user = User.create(
                first_name=first_name,
                last_name=last_name,
                email=email)
            return user
        except IntegrityError:
            raise UserAlreadyRegistered
