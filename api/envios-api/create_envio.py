import json
import boto3
import uuid
from datetime import datetime


def lambda_handler(event, context):

    dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")

    table = dynamodb.Table('Envios')

    body = json.loads(event['body'])

    envio = {"id": str(uuid.uuid4), "fechaAlta":  str(datetime.now()), "pendiente": str(
        datetime.now()), "email": body['email'], "destino": body['destino']}

    table.put_item(Item=envio)

    return {
        "statusCode": 200,
        "body": envio,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        }
    }
