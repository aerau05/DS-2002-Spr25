# upload_private.py
import boto3

s3 = boto3.client('s3', region_name='us-east-1')

bucket = 'ds2002-jxw9ev'
local_file = 'google_logo.png'

with open(local_file, 'rb') as data:
    s3.put_object(Bucket=bucket, Key=local_file, Body=data)
