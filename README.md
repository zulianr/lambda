## Ejercicio lambda
### Ricardo Zulian

Comandos para probar 

`docker run -p 8000:8000 --network awslocal --name dynamodb amazon/dynamodb-local:1.11.119 -jar DynamoDBLocal.jar -sharedDb`

`sam local start-api --docker-network awslocal`
