import os
import boto3
from dotenv import load_dotenv

load_dotenv()

region = os.getenv("AWS_REGION", "us-east-2")
account_id = os.environ["AWS_ACCOUNT_ID"]
role_arn = os.environ["AWS_LAMBDA_ROLE_ARN"]
repository_name = "aws-lambda-ml-deployment"
function_name = "aws_lambda_ml_deployment"
image_uri = f"{account_id}.dkr.ecr.{region}.amazonaws.com/{repository_name}:latest"

client = boto3.client("lambda", region_name=region)
response = client.create_function(
    FunctionName=function_name,
    PackageType="Image",
    Code={"ImageUri": image_uri},
    Role=role_arn,
    Timeout=30,
    MemorySize=128,
)

print(f"Function Name: {response['FunctionName']}")
print(f"Function ARN: {response['FunctionArn']}")
