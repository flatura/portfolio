# Architecture and Integrations

## Architecture

## Cloud Architecture Diagram

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

## Integration Flows

## Sequence Diagrams

### Audio File Upload Initiation

```mermaid
sequenceDiagram
    autonumber
    
    actor U as Browser (SPA)
    participant API as API Gateway
    participant L as AWS Lambda
    participant S3 as Amazon S3
    participant DB as DynamoDB

    U->>API: GET /upload-url (pass JWT)
    API->>L: Invoke get_upload_url
    L->>DB: Create record (Status: UPLOADING)
    L->>S3: Generate Presigned POST URL
    S3-->>L: Upload link
    L-->>U: JSON: { uploadUrl, fileId }
```

### Direct Upload & Asynchronous Trigger (Event-Driven)

```mermaid
sequenceDiagram
    autonumber
    
    actor U as Browser (SPA)
    participant L as AWS Lambda
    participant S3 as Amazon S3
    participant DB as DynamoDB
    participant AI as AssemblyAI

    U->>S3: POST Upload audio file (Bypass API Gateway)
    S3-->>U: 204 No Content (Success)
    
    S3-)L: Event: ObjectCreated (Async trigger s3_trigger)
    L->>DB: Update status (TRANSMITTING)
    L->>S3: Generate temporary GET Presigned URL for AI
    L->>AI: POST /v2/transcript (Audio URL + Webhook URL)
    AI-->>L: 201 Created (Return transcript_id)
    L->>DB: Update status (PROCESSING + save ID)
```

### AI Processing & Webhook (up to several minutes)

```mermaid
sequenceDiagram
    autonumber
    
    actor U as Browser (SPA)
    participant API as API Gateway
    participant L as AWS Lambda
    participant S3 as Amazon S3
    participant DB as DynamoDB
    participant AI as AssemblyAI
    
    loop Every 15 seconds (Polling)
        U->>API: GET /jobs
        activate API
        API->>L: Invoke get_jobs
        deactivate API
        activate L
        L->>DB: Request user's job list
        activate DB
        DB-->>L: Data (Status: PROCESSING)
        deactivate DB
        L-->>U: Update UI
        deactivate L
    end

    Note over AI, DB: AssemblyAI completes processing
    AI->>API: POST /webhook (pass transcript_id)
    activate API
    API->>L: Invoke webhook_assemblyai
    deactivate API
    activate L
    L->>AI: GET /v2/transcript/{id}
    activate AI
    AI-->>L: Completed transcription text
    deactivate AI
    L->>S3: PUT Save text (Transcript.txt)
    L->>DB: Update status (READY)
    deactivate L
```

### Result Retrieval (Download)

```mermaid
sequenceDiagram
    autonumber
    
    actor U as Browser (SPA)
    participant API as API Gateway
    participant L as AWS Lambda
    participant S3 as Amazon S3
    participant DB as DynamoDB

    U->>API: GET /jobs (Next polling interval)
    activate API
    API-->>U: Status: READY (Download button active)
    deactivate API

    U->>API: GET /download-url?fileId=...
    activate API
    API->>L: Invoke get_download_url
    deactivate API
    activate L
    L->>DB: Verify user access rights to file
    activate DB
    DB-->>L: Data access confirmed
    deactivate DB
    L->>S3: Generate Presigned GET URL (with Content-Disposition)
    L-->>U: JSON: { downloadUrl }
    deactivate L
    activate U
    U->>S3: Direct download of Transcript.txt
    deactivate U
    activate S3
    S3-->>U: Transcription file
    deactivate S3
```
