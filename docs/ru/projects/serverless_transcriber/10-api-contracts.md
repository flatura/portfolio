# API-контракты

## API Gateway (аутентификация)

| Метод | Путь | Lambda handler | Назначение |
|-------|------|----------------|------------|
| `GET` | `/upload-url` | `get_upload_url` | Создать запись; вернуть Presigned POST URL и `fileId` |
| `GET` | `/jobs` | `get_jobs` | Список джобов пользователя (polling UI) |
| `GET` | `/download-url?fileId=...` | `get_download_url` | Проверка доступа; Presigned GET URL транскрипта |
| `POST` | `/webhook` | `webhook_assemblyai` | Callback AssemblyAI (`transcript_id`) |

Все маршруты API Gateway требуют JWT (Amazon Cognito), кроме `/webhook` (callback провайдера).

## Amazon Cognito (Hosted UI / PKCE)

| Метод | Путь | Назначение |
|-------|------|------------|
| `POST` | `/oauth2/token` | Обмен authorization code на Access & ID tokens |

## AssemblyAI (внешний)

| Метод | Путь | Назначение |
|-------|------|------------|
| `POST` | `/v2/transcript` | Отправка URL аудио + webhook URL; возвращает `transcript_id` |
| `GET` | `/v2/transcript/{id}` | Получение готового текста транскрипции |

## Amazon S3 (прямой доступ клиента)

| Метод | Цель | Назначение |
|-------|------|------------|
| `POST` | Presigned POST URL | Прямая загрузка аудио (обход лимитов API Gateway) |
| `GET` | Presigned GET URL | Прямое скачивание транскрипта |
