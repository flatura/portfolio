# Overview

## Product Overview

A serverless solution for transcribing audio recordings using an external transcription API.

## Technology Stack

* **Backend:** Python on AWS Lambda
* **Data Layer:** Amazon S3 (audio and transcription files), AWS DynamoDB (job status tracking)
* **Frontend:** Static HTML + Vanilla JS hosted on Amazon S3 and distributed via AWS CloudFront
* **Security:** Amazon Cognito (PKCE flow)
* **Infrastructure & IaC:** AWS API Gateway, fully provisioned via Terraform
