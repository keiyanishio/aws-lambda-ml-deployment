import json
import os
import boto3
from dotenv import load_dotenv

load_dotenv()

region = os.getenv("AWS_REGION", "us-east-2")
client = boto3.client("lambda", region_name=region)

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

response = client.invoke(
    FunctionName="aws_lambda_ml_deployment",
    Payload=json.dumps(payload),
)
print(response["Payload"].read().decode())
