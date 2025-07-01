# File-Upload-S3-Terraform
Flask-based File Upload App with AWS S3 and Terraform

This project demonstrates a simple Python Flask web application that allows users to upload files to an AWS S3 bucket. The S3 bucket is provisioned using Terraform, following Infrastructure as Code (IaC) principles.

Key Features:
1. File Upload Web App using Flask
2. S3 Bucket Provisioned with Terraform
3. Environment variables used to securely pass AWS credentials and bucket name
4. /healthz endpoint for readiness/health checks

Tech Stack:
Python (Flask, Boto3)
AWS S3
Terraform

How to Run?
1. Configure AWS Credentials
   Before running Terraform and Flask app , setup AWS credentials
   aws configure
2. Provision S3 Bucket through Terraform
   cd terraform
   terraform init
   terraform plan
   terraform apply
   This generates the s3 bucket name as output
3. Run Flask app locally
   cd app
   pip install -r requirements.txt
   python app.py

   Visit -> http://localhost:5000

   To Test visit http://localhost:5000/upload
   Upload a file via the form
   User gets message "file uploaded successfully on s3 bucket"
   Check the S3 bucket via AWS Console


