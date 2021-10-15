import boto3


def create_envio_table(dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")

    table = dynamodb.create_table(
        TableName='Envios',
        KeySchema=[
            {
                'AttributeName': 'id',
                'KeyType': 'HASH'  # Partition key
            }

        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'id',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'pendiente',
                'AttributeType': 'S'
            },

        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 10,
            'WriteCapacityUnits': 10
        },


        GlobalSecondaryIndexes=[
            {
                "IndexName": "EnviosPendientesIndex",
                "KeySchema": [
                    {
                        "AttributeName": "id",
                        "KeyType": "HASH"
                    },
                    {
                        "AttributeName": "pendiente",
                        "KeyType": "RANGE"
                    }
                ],
                "Projection": {
                    "ProjectionType": "ALL"
                },
                "ProvisionedThroughput": {
                    "ReadCapacityUnits": 1,
                    "WriteCapacityUnits": 1,
                }

            }
        ],

    )
    return table


if __name__ == '__main__':
    movie_table = create_envio_table()
    print("Table status:", movie_table.table_status)
