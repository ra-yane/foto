from peewee import MySQLDatabase, PostgresqlDatabase

from .config import config

db = MySQLDatabase(
    'topack',
    user=config['database'].get('user', 'root'),
    password=config['database'].get('password', 'topack'),
    host=config['database'].get('host', 'localhost')
)

eDB = db = MySQLDatabase(
    'topack',
    user=config['database'].get('user', 'root'),
    password=config['database'].get('password', 'topack'),
    host=config['database'].get('host', 'localhost')
)