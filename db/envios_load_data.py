import json
import boto3


def load_envios(envios, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")

    table = dynamodb.Table('Envios')
    for envio in envios:
        id = envio['id']
        fechaAlta = envio['fechaAlta']
        destino = envio['destino']
        email = envio['email']
        pendiente = envio['pendiente']

        print("Adding envio:", id, fechaAlta, destino, email, pendiente)

        table.put_item(Item=envio)


if __name__ == '__main__':
    with open("enviosdata.json") as json_file:
        envios_list = json.load(json_file)
    load_envios(envios_list)