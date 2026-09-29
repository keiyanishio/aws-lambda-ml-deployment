import os
import boto3
from dotenv import load_dotenv

load_dotenv()

region = os.getenv("AWS_REGION", "us-east-2")
function_name = "aws_lambda_ml_deployment"
api_name = "aws_lambda_ml_deployment_api"
route_key = "POST /lambda-function"

lambda_client = boto3.client("lambda", region_name=region)
apigw = boto3.client("apigatewayv2", region_name=region)
function = lambda_client.get_function(FunctionName=function_name)
function_arn = function["Configuration"]["FunctionArn"]

api = apigw.create_api(
    Name=api_name,
    ProtocolType="HTTP",
    Target=function_arn,
    RouteKey=route_key,
)

lambda_client.add_permission(
    FunctionName=function_name,
    StatementId="AllowApiGatewayInvoke",
    Action="lambda:InvokeFunction",
    Principal="apigateway.amazonaws.com",
    SourceArn=f"{api['ApiEndpoint'].replace('https://', 'arn:aws:execute-api:' + region + ':*:' + api['ApiId'])}/*",
)

print(f"API endpoint: {api['ApiEndpoint']}/lambda-function")
