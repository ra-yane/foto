from peewee import MySQLDatabase, PostgresqlDatabase

from .config import config

db = MySQLDatabase(
    'skus',
    user=config['database'].get('user', 'root'),
    password=config['database'].get('password', 'foto'),
    host=config['database'].get('host', 'localhost')
)