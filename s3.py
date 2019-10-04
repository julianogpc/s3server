import time

import boto3

client = boto3.client(
    's3',
    aws_access_key_id='SCALITY_USER',
    aws_secret_access_key='ABCDEFGHIJKLMNOPQRSTUVWXYZ',
    endpoint_url='http://localhost:8000'
)

bucket_name = str(time.time())

client.create_bucket(Bucket=bucket_name)

lists = client.list_buckets()

filename = 'file.txt'

client.upload_file(filename, bucket_name, filename)

with open(filename, 'wb') as f:
    client.download_fileobj(bucket_name, filename, f)
