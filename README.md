# Containerized ML Inference on AWS Lambda

Individual academic project developed in **2023** during the MLOps course of my Computer Engineering degree at **Insper**.

The goal was to package a machine-learning inference workload as a **Docker container image** for **AWS Lambda**, rather than relying on the traditional ZIP deployment workflow. This made it possible to package the inference code, serialized model artifacts and Python dependencies together.

## Architecture

```text
Client
  ↓
Amazon API Gateway
  ↓
AWS Lambda
  ↓
Docker container
  ↓
Encoder + serialized ML model
  ↓
Prediction
```

Deployment flow:

```text
Application + artifacts → Docker image → Amazon ECR → AWS Lambda → API Gateway
```

## Technologies

**Python · Docker · AWS Lambda · Amazon ECR · Amazon API Gateway · Boto3 · Pandas · scikit-learn · LightGBM**

## Project Goal

The focus of the assignment was **model operationalization**. The container packages the Lambda handler, model artifacts and runtime dependencies. The image is stored in Amazon ECR and used to create an AWS Lambda function, which can then be exposed through Amazon API Gateway.

Boto3 scripts demonstrate the infrastructure workflow used in the assignment: creating the ECR repository, creating the Lambda function, exposing it through API Gateway and testing both Lambda and HTTP invocation.

## Repository Structure

```text
.
├── Dockerfile
├── requirements.txt
├── .env.example
├── model.pkl
├── ohe.pkl
└── src/
    ├── ecr.py
    ├── create_lambda.py
    ├── create_api.py
    ├── predict_handler.py
    ├── test_lambda.py
    └── test_api.py
```

## Inference Flow

The Lambda handler receives an HTTP request body, converts the input into a Pandas DataFrame, applies the serialized encoder and sends the transformed features to the serialized model.

Example payload:

```json
{
  "age": 42,
  "job": "entrepreneur",
  "marital": "married",
  "education": "primary",
  "balance": 558,
  "housing": "yes",
  "duration": 186,
  "campaign": 2
}
```

The function returns the prediction as JSON.

## Container Build

```bash
docker build --platform linux/amd64 -t aws-lambda-ml-deployment .
```

## Deployment Overview

The portfolio version uses environment-based configuration and the standard Boto3 credential chain instead of embedding credentials in source code.

A local environment can be configured from `.env.example`. The deployment workflow is represented by:

```bash
python src/ecr.py
python src/create_lambda.py
python src/create_api.py
```

The deployed function and HTTP endpoint can be exercised with:

```bash
python src/test_lambda.py
python src/test_api.py
```

The original 2023 AWS environment is no longer active, so this public portfolio version is not presented as a currently deployed service.

## Portfolio Version

This repository is a cleaned public portfolio version of my original **2023 Insper MLOps assignment**.

The original `model.pkl` and `ohe.pkl` artifacts are included so the inference workflow used in the assignment is preserved. Historical AWS account identifiers, ARNs and endpoint URLs were removed from the public version.

The core architecture and implementation approach were preserved while configuration, naming and documentation were cleaned up for public presentation.

## What I Would Improve Today

If rebuilding the project today, I would:

- provision the AWS infrastructure with Infrastructure as Code;
- add automated unit and integration tests;
- add CI/CD for container build, validation and deployment;
- pin dependencies for reproducible builds;
- add structured logging, metrics and monitoring;
- validate request payloads and return more robust API errors;
- load model artifacts efficiently across warm Lambda invocations;
- use least-privilege IAM configuration;
- add model versioning and deployment rollback strategies.

These are **future improvements**, not features claimed to have existed in the original 2023 assignment.

## Historical Context

This repository represents an early hands-on MLOps project and my introduction to deploying containerized machine-learning inference workloads on AWS.
