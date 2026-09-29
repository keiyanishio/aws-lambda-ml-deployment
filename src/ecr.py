import boto3

repository_name = "aws-lambda-ml-deployment"
ecr_client = boto3.client("ecr")

response = ecr_client.create_repository(
    repositoryName=repository_name,
    imageScanningConfiguration={"scanOnPush": True},
    imageTagMutability="MUTABLE",
)

repository = response["repository"]
print(f"Repository ARN: {repository['repositoryArn']}")
print(f"Repository URI: {repository['repositoryUri']}")
