# Architecture and Integrations

## Architecture

## Architectural concept

The system is built on an event-driven model.

The static frontend is served via S3/CloudFront. The user authenticates through Cognito Hosted UI and calls API Gateway using the obtained JWT. API Gateway routes requests to Lambda functions.

Large audio files do not pass through API Gateway and Lambda. The backend issues a presigned POST URL, after which the browser uploads the file directly to S3. An S3 ObjectCreated event triggers a handler that creates a temporary URL for the transcription provider and submits a new transcription request. The external provider performs long transcription asynchronously and returns the result via webhook. The final text transcript is saved to S3, and the job status is updated and stored in DynamoDB.

```mermaid
architecture-beta
    service dynamo(aws:dynamodb)[AWS DynamoDB]
    service lambda(aws:lambda)[AWS Lambda] 
    service api(aws:api-gateway)[AWS API Gateway]
    service static(aws:simple-storage-service)[Static website at Amazon S3]
    service storage(aws:simple-storage-service)[File storage at Amazon S3]
    service browser(logos:chrome)[Browser]
    service cognito(aws:cognito)[AWS Cognito]
    service ai(logos:webhooks)[Transcriber API]
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

## Integration flows

## Sequence diagrams

### Audio file submission

```mermaid
sequenceDiagram
    autonumber
    
    actor U as Browser (SPA)
    participant API as API Gateway
    participant L as AWS Lambda
    participant S3 as Amazon S3
    participant DB as DynamoDB

    U->>API: GET /upload-url (+JWT in Header)
    activate API
    API->>L: Invoke get_upload_url
    deactivate API
    activate L
    L->>DB: Create record (Status: UPLOADING)
    L->>S3: Generate Presigned POST URL
    activate S3
    S3-->>L: Upload link
    deactivate S3
    L-->>U: JSON: { uploadUrl, fileId }
    deactivate L

```

### Direct upload and asynchronous trigger (event-driven)

```mermaid
sequenceDiagram
    autonumber
    
    actor U as Browser (SPA)
    participant L as AWS Lambda
    participant S3 as Amazon S3
    participant DB as DynamoDB
    participant AI as TranscribeProvider

    U->>S3: POST Upload audio file (Bypass API Gateway)
    activate S3
    S3-->>U: 204 No Content (Success)
    deactivate S3
    
    S3-)L: Event: ObjectCreated (Async invoke s3_trigger)
    activate L
    L->>DB: Update status (TRANSMITTING)
    L->>S3: Generate temporary GET Presigned URL for AI
    L->>AI: POST /v2/transcript (Audio URL + Webhook URL)
    activate AI
    alt TranscribeProvider accepts request
        AI-->>L: 201 Created (transcript_id)
        L->>DB: Status = PROCESSING (save ID)
    else API error (e.g. HTTP 400/500)
        AI-->>L: 4xx / 5xx Error
        deactivate AI
        L->>DB: Status = ERROR (Log reason)
    end
    deactivate L
    
```

### AI processing and webhook (up to several minutes)

```mermaid
sequenceDiagram
    autonumber
    
    actor U as Browser (SPA)
    participant API as API Gateway
    participant L as AWS Lambda
    participant S3 as Amazon S3
    participant DB as DynamoDB
    participant AI as TranscribeProvider
    
    loop Every 15 seconds (Polling)
        U->>API: GET /jobs
        activate API 
        API->>L: Invoke get_jobs
        deactivate API
        activate L
        L->>DB: Request user's file list
        activate DB
        DB-->>L: Data (Status: PROCESSING)
        deactivate DB
        L-->>U: Update UI
        deactivate L
    end

    Note over AI, DB: TranscribeProvider completes processing
    AI->>API: POST /webhook (pass transcript_id)
    activate API
    API->>L: Invoke webhook_TranscribeProvider
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

### Result retrieval (download)

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
    L->>S3: Generate Presigned GET URL (with Content-Disposition)
    L-->>U: JSON: { downloadUrl }
    deactivate L
    U->>S3: Direct download of Transcript.txt
    activate S3
    S3-->>U: Transcription file
    deactivate S3
```
