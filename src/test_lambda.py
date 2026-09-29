import json
import boto3

client = boto3.client("lambda")
payload = {
    "body": json.dumps({
        "age": 42,
        "job": "entrepreneur",
        "marital": "married",
        "education": "primary",
        "balance": 558,
        "housing": "yes",
        "duration": 186,
        "campaign": 2,
    })
}
response = client.invoke(FunctionName="aws_lambda_ml_deployment", Payload=json.dumps(payload))
print(response["Payload"].read().decode())
