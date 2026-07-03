# Обзор
## Обзор продукта
Бессерверное решение для транскрибации аудиозаписей посредством внешнего API-транскрибации.

## Технологический стек

* **Backend:** Python в AWS Lambda
* **Data:** Amazon S3 (фалйы записей, транскрибации), AWS DynamoDB (для статусов джобов)
* **Frontend:** static HTML + JS на Amazon S3 с разверткой в AWS CloudFront
* **AI:** AssemblyAI API
* **Security:** AWS Cognito
* **Infrastructure:** AWS API Gateway, упаковка в Terraform проект