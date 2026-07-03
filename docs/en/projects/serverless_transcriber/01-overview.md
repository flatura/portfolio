# Overview

## Product Overview

A serverless solution for transcribing audio recordings using an external transcription API.

## Technology Stack

* **Backend:** Python on AWS Lambda
* **Data:** Amazon S3 (recording files, transcriptions), AWS DynamoDB (job statuses)
* **Frontend:** static HTML + JS on Amazon S3 deployed via AWS CloudFront
* **AI:** AssemblyAI API
* **Security:** AWS Cognito
* **Infrastructure:** AWS API Gateway, packaged as a Terraform project
