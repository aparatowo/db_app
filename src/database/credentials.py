# Use this code snippet in your app.
# If you need more information about configurations or implementing the sample code, visit the AWS docs:
# https://aws.amazon.com/developers/getting-started/python/
import os
import boto3
import base64
import json
from botocore.exceptions import ClientError

# initial_region_name = "eu-north-1"

AWS_REGION = os.environ['AWS_REGION']
DB_SECRET = os.environ["DB_SECRET"]


def get_secret():

    # secret_name = DB_SECRET
    region_name = AWS_REGION

    # Create a Secrets Manager client
    session = boto3.session.Session()
    client = session.client(
        service_name='ssm',
        region_name=region_name
    )

    get_secret_value_response = client.get_parameters_by_path(
        Path='/test/db',
        WithDecryption=True
    )

    return {param['Name']: param['Value'] for param in get_secret_value_response['Parameters']}

