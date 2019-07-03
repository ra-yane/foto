from redis import Redis
from rq import Queue

from .config import config

REDIS_URL = config['cache'].get('url', 'redis://localhost:6379/1')

cache = Redis(
    host=config['cache'].get('host', 'localhost'),
    password=config['cache'].get('password', None),
    db=1
)

queue = Queue(connection=cache, default_timeout=7200)
