Terraform project structure that provisions AWS resources (IAM, VPC, S3, Lambda, CloudWatch) and connects them so that any file uploaded to S3 triggers a Python Lambda function

The structure as follows.
aws-s3-lambda-project/
├── main.tf
├── provider.tf
├── vpc.tf
├── iam.tf
├── s3.tf
├── lambda.tf
├── outputs.tf
├── variables.tf
└── lambda_function/
    └── handler.py
