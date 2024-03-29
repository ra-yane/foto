import boto3

from .config import config

S3_ACCESS_KEY = config['aws'].get('access_key')
S3_SECRET_KEY = config['aws'].get('private_key')
endpoint = config['aws'].get('endpoint')

storage = boto3.client(
    "s3",
    aws_access_key_id=S3_ACCESS_KEY,
    aws_secret_access_key=S3_SECRET_KEY,
    endpoint_url=endpoint
)
