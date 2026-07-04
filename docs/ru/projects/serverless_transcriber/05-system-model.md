# Модель системы

## Модель данных

### TranscriptionJob
Основная сущность процесса транскрибации.

Атрибуты:

- `fileId`
- `ownerUserId`
- `inputS3Key`
- `transcriptS3Key`
- `status`
- `providerTranscriptId`
- `createdAt`
- `updatedAt`
- `errorReason`
- `speakerMode`
- `fileSize`
- `durationEstimate`

### Системные инварианты

- job принадлежит одному пользователю;
- download URL выдаётся только владельцу job;
- transcript можно скачать только в статусе `READY`;
- webhook должен быть idempotent;
- повторный callback от provider не должен создавать новый transcript;
- failed job не должен блокировать список остальных job;
- presigned URLs имеют ограниченное время жизни.

## DynamoDB - статусы джобов

Каждая задача транскрибации хранится как запись БД с жизненным циклом:

| State Machine | Значение |
|--------|----------|
| `UPLOADING` | Выдана предподписанная ссылка; идёт загрузка клиентом |
| `TRANSMITTING` | Аудио загружено в S3; отправка в сервис |
| `PROCESSING` | сервис транскрибирует (`transcript_id` сохранён) |
| `READY` | Транскрипт сохранён в S3; доступен для скачивания |
| `ERROR` | Ошибка AssemblyAI или пайплайна (причина в логе) |

## Amazon S3

* **Bucket файлов:** загрузки аудио и сгенерированные транскрипты (`Transcript.txt`).
* **Bucket статического сайта:** SPA, раздаётся через CloudFront.

## API-контракты

## API Gateway (аутентификация)

| Метод | Путь | Назначение |
|-------|------|------------|
| `GET` | `/upload-url` | Создать запись; вернуть Presigned POST URL и `fileId` |
| `GET` | `/jobs` | Список джобов пользователя (polling UI) |
| `GET` | `/download-url?fileId=...` | Проверка доступа; Presigned GET URL транскрипта |
| `POST` | `/webhook` |  Callback AssemblyAI (`transcript_id`) |

Все маршруты API Gateway требуют JWT (Amazon Cognito), кроме `/webhook` (callback провайдера транскрибации).

## Amazon Cognito (Hosted UI / PKCE)

| Метод | Путь | Назначение |
|-------|------|------------|
| `POST` | `/oauth2/token` | Обмен authorization code на Access & ID tokens |

## внешний API провайдера транскрибации

| Метод | Путь | Назначение |
|-------|------|------------|
| `POST` | `/v2/transcript` | Отправка URL аудио + webhook URL; возвращает `transcript_id` |
| `GET` | `/v2/transcript/{id}` | Получение готового текста транскрипции |

## Amazon S3 (прямой доступ клиента)

| Метод | Цель | Назначение |
|-------|------|------------|
| `POST` | Presigned POST URL | Прямая загрузка аудио (обход лимитов API Gateway) |
| `GET` | Presigned GET URL | Прямое скачивание транскрипта |
