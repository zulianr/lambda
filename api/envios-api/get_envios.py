import json
import boto3
import logging


def lambda_handler(event, context):

    dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")

    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    logger.info("httpMethod: %s", event.get('httpMethod'))
    logger.info("pathParameters: %s", event.get('pathParameters'))
    logger.info("path: %s", event.get('path'))

    table = dynamodb.Table('Envios')

    response = table.scan(IndexName="EnviosPendientesIndex")

    return {
        "statusCode": 200,
        "body": json.dumps(response["Items"]),
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        }
    }
