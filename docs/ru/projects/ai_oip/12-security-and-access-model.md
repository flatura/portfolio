# Модель безопасности и доступа

## Controlled LLM execution

LLM рассуждает и планирует, но доступ к данным делегирован контролируемым backend tools - не free chat поверх корпоративных данных.

## Controlled tool access model

Спроектировал controlled tool access model, при которой LLM никогда не обращается напрямую к PostgreSQL, Qdrant или MinIO.
