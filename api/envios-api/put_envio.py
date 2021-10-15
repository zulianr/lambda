import json
import boto3
import uuid
from datetime import datetime


def lambda_handler(event, context):

    dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")
    table = dynamodb.Table('Envios')

    parameters = event["pathParameters"]
    id = str(parameters["idEnvio"])

    item = table.get_item(Key={'id': id})['Item']

    table.delete_item(Key={"id":id})
    item.pop("pendiente")

    table.put_item(Item=item)


    return {
        "statusCode": 200,
        "body": item,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        }
    }

#test
if __name__ == "__main__":
    lambda_handler({"pathParameters": {"idEnvio": 1}},{})