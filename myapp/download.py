import os
import boto3

s3 = boto3.client('s3', aws_access_key_id='', aws_secret_access_key='')
response = s3.list_objects_v2(Bucket='ml-flowbucket', Prefix='1')
all = response['Contents']
latest = max(all, key=lambda x: x['LastModified'])
res = str(latest['Key'])
x = res.split('/')
file_path = x[0]+'/'+x[1]+'/'+x[2]+'/'+x[3]+'/model.pkl'
s3.download_file('ml-flowbucket',file_path,'model.pkl')
