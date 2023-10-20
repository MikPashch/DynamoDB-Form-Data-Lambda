import os
import json
import boto3
from time import strftime, gmtime
import random

dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('your_table_name')

def lambda_handler(event, context):
    # Parse form data from the event
    name = event['name']
    email = event['email']
    message = event['message']

    # Generate a unique ID as an integer from time
    random_id = int(strftime("%Y%m%d%H%M%S", gmtime()))


    # Put item into DynamoDB table
    response = table.put_item(
        Item={
            'ID': random_id,
            'Email': email,
            'Message': message,
            'Name': name
        })

    return {
    'statusCode': 200,
    'body': json.dumps('Thank you! I will contact you soon!' )
    }
