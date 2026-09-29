# Containerized ML Inference on AWS Lambda

Individual academic project developed in **2023** during the MLOps course of my Computer Engineering degree at **Insper**.

The project packages a machine-learning inference workflow in a Docker container for deployment with Amazon ECR, AWS Lambda and Amazon API Gateway.

## Architecture

`Client → API Gateway → Lambda → Docker container → Encoder + model → Prediction`

## Technologies

**Python · Docker · AWS Lambda · Amazon ECR · API Gateway · Boto3 · Pandas · scikit-learn · LightGBM**

## Project files

- `Dockerfile` — Lambda container image
- `model.pkl` — serialized model from the original assignment
- `ohe.pkl` — serialized encoder from the original assignment
- `src/predict_handler.py` — inference handler
- `src/ecr.py` — ECR repository creation script

## Historical context

This is a cleaned public portfolio version of my original 2023 Insper assignment. The original model artifacts are included so the inference workflow is preserved. The project represents my early hands-on experience deploying containerized machine-learning workloads on AWS.

## What I would improve today

I would add Infrastructure as Code, automated tests, CI/CD, dependency pinning, structured logging, request validation, monitoring and model versioning. These are future improvements rather than features claimed to have existed in the original assignment.
