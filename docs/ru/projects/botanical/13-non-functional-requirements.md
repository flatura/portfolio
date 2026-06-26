# Нефункциональные требования

## Инфраструктура и deployment

Проект спроектирован как практичный cloud-ready MVP:

* разделенные frontend и backend;
* containerized services;
* PostgreSQL/PostGIS database;
* MinIO/S3-compatible storage для медиа и import-файлов;
* schema migrations через Flyway;
* production profile на базе environment configuration;
* базовый CI/CD и deployment automation path.
