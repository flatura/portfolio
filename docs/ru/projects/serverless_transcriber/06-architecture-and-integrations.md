# Архитектура и интеграции

## Архитектура

## Архитектурная концепция

```mermaid
architecture-beta
    service dynamo(aws:dynamodb)[AWS DynamoDB]
    service lambda(aws:lambda)[AWS Lambda] 
    service api(aws:api-gateway)[AWS API Gateway]
    service static(aws:simple-storage-service)[Static website at Amazon S3]
    service storage(aws:simple-storage-service)[File storage at Amazon S3]
    service browser(logos:chrome)[Browser]
    service cognito(aws:cognito)[AWS Cognito]
    service ai(logos:webhooks)[AssemblyAI API]
    service front(aws:cloudfront)[AWS CloudFront]

    front:T -- B:static
    browser:T -- B:api
    browser:L -- R:front
    browser:B -- T:cognito

    api:R -- L:lambda
    api:T <-- B:ai
    lambda:T -- R:ai
    lambda:R -- L:dynamo
    lambda:B -- T:storage
    storage:L -- R:browser
```

## Потоки интеграции

## Диаграммы последовательности

### Отправка файла аудио

```mermaid
sequenceDiagram
    autonumber
    
    actor U as Браузер (SPA)
    participant API as API Gateway
    participant L as AWS Lambda
    participant S3 as Amazon S3
    participant DB as DynamoDB

    U->>API: GET /upload-url (+JWT в Header)
    activate API
    API->>L: Вызов get_upload_url
    deactivate API
    activate L
    L->>DB: Создание записи (Status: UPLOADING)
    L->>S3: Генерация Presigned POST URL
    activate S3
    S3-->>L: Ссылка для загрузки
    deactivate S3
    L-->>U: JSON: { uploadUrl, fileId }
    deactivate L

```

### Прямая загрузка и Асинхронный Триггер (Event-Driven)

```mermaid
sequenceDiagram
    autonumber
    
    actor U as Браузер (SPA)
    participant L as AWS Lambda
    participant S3 as Amazon S3
    participant DB as DynamoDB
    participant AI as AssemblyAI

    U->>S3: POST Загрузка аудио-файла (Обход API Gateway)
    activate S3
    S3-->>U: 204 No Content (Успех)
    deactivate S3
    
    S3-)L: Event: ObjectCreated (Асинхронный вызов s3_trigger)
    activate L
    L->>DB: Обновление статуса (TRANSMITTING)
    L->>S3: Генерация временной GET Presigned URL для AI
    L->>AI: POST /v2/transcript (Аудио URL + Webhook URL)
    activate AI
    alt AssemblyAI принимает запрос
        AI-->>L: 201 Created (transcript_id)
        L->>DB: Status = PROCESSING (сохранение ID)
    else Ошибка API (например, HTTP 400/500)
        AI-->>L: 4xx / 5xx Error
        deactivate AI
        L->>DB: Status = ERROR (Запись причины в лог)
    end
    deactivate L
    
```

### Обработка ИИ и Webhook (до нескольких минут)

```mermaid
sequenceDiagram
    autonumber
    
    actor U as Браузер (SPA)
    participant API as API Gateway
    participant L as AWS Lambda
    participant S3 as Amazon S3
    participant DB as DynamoDB
    participant AI as AssemblyAI
    
    loop Каждые 15 секунд (Polling)
        U->>API: GET /jobs
        activate API 
        API->>L: Вызов get_jobs
        deactivate API
        activate L
        L->>DB: Запрос списка файлов пользователя
        activate DB
        DB-->>L: Данные (Status: PROCESSING)
        deactivate DB
        L-->>U: Обновление UI
        deactivate L
    end

    Note over AI, DB: AssemblyAI завершает работу
    AI->>API: POST /webhook (передача transcript_id)
    activate API
    API->>L: Вызов webhook_assemblyai
    deactivate API
    activate L
    L->>AI: GET /v2/transcript/{id}
    activate AI
    AI-->>L: Готовый текст транскрипции
    deactivate AI
    L->>S3: PUT Сохранение текста (Transcript.txt)
    L->>DB: Обновление статуса (READY)
    deactivate L
    
```

### Получение результата (Скачивание)

```mermaid
sequenceDiagram
    autonumber
    
    actor U as Браузер (SPA)
    participant API as API Gateway
    participant L as AWS Lambda
    participant S3 as Amazon S3
    participant DB as DynamoDB

    U->>API: GET /jobs (Очередной опрос)
    activate API
    API-->>U: Status: READY (Кнопка скачивания активна)
    deactivate API

    U->>API: GET /download-url?fileId=...
    activate API
    API->>L: Вызов get_download_url
    deactivate API
    activate L
    L->>DB: Проверка прав доступа пользователя к файлу
    L->>S3: Генерация Presigned GET URL (с Content-Disposition)
    L-->>U: JSON: { downloadUrl }
    deactivate L
    U->>S3: Прямое скачивание текста.txt
    activate S3
    S3-->>U: Файл транскрипции
    deactivate S3
```
