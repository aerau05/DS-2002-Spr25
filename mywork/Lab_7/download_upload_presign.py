# download_upload_presign.py
import requests
import boto3

url = 'https://upload.wikimedia.org/wikipedia/commons/4/47/PNG_transparency_demonstration_1.png'
local_filename = 'auto_image.png'

# Download image
with open(local_filename, 'wb') as f:
    f.write(requests.get(url).content)

# Upload to S3
s3 = boto3.client('s3', region_name='us-east-1')
bucket = 'ds2002-jxw9ev'

with open(local_filename, 'rb') as f:
    s3.put_object(Bucket=bucket, Key=local_filename, Body=f)

# Presign the file
presigned_url = s3.generate_presigned_url(
    'get_object',
    Params={'Bucket': bucket, 'Key': local_filename},
    ExpiresIn=604800
)

print("Presigned URL:", presigned_url)
