# Serverless Transcriber SaaS

**Status:** Active

## Product Overview
A serverless solution for transcribing audio recordings using an external transcription API.

## Background
There is an episodic need for fast and cost-effective transcription of large audio files (1.5h+) with minimal infrastructure costs. Low workload and a limited user base (up to 40 hours of recordings per month for 1-3 users).

## Requirements
* Accessible from any internet-connected device.
* Availability Region: European part of Eurasia (EU).
* Optimally minimal infrastructure usage.
* Audio file size: up to 300MB.
* Audio duration: up to 6 hours.
* Concurrent processing of up to 5 files.
* Strict access control to the service.
* Complete isolation of user data.

## UI Screenshots
### Main menu
<figure markdown>
![UI_1](../../assets/transcriber/main_menu.webp)
<figcaption>Main menu</figcaption>
</figure>

### Upoading a record
<figure markdown>
![UI_1](../../assets/transcriber/loading.webp)
<figcaption>Uploading a record</figcaption>
</figure>


### Processing the record
<figure markdown>
![UI_1](../../assets/transcriber/processed.webp)
<figcaption>Processing the record</figcaption>
</figure>


## Architectural Challenges & Engineering Decisions
* **Optimal Resource Utilization:** Need to account for the episodic nature of resource usage, a small number of use cases, and broad regional availability.
  * *Solution:* Utilize a Serverless approach and AWS Lambda infrastructure. A traditional VPS is unsuitable due to recurring computing costs (even when the service is idle). A Telegram bot is not viable due to audio file size limits (and the bot's logic still requires hosting).
* **Handling 300MB Files:** Need to account for large file volumes and limitations of standard gateways (like API Gateway payload limits).
  * *Solution:* Utilize direct upload to Amazon S3 via Presigned URLs, bypassing API Gateway completely.
* **Optimal Transcription Infrastructure:** Need to account for a zero budget for GPU equipment and hosting open-source LLMs/Models.
  * *Solution:* Integrate a third-party transcription API. AssemblyAI was chosen for providing the best quality-to-price ratio on the market.
* **Robust Event-Driven Model:** Lambda is excellent for decoupling the solution, but the third-party API transcription time may exceed the Lambda execution timeout.
  * *Solution:* Decouple the audio file submission from the text result retrieval. The selected transcription provider supports webhook notifications.
* **User Data Isolation:** Ensure compliance with access restrictions and data separation requirements.
  * *Solution:* Use AWS Cognito. It provides built-in account management, user registration, 2FA, brute-force protection, etc. The service seamlessly integrates into the AWS ecosystem.

## Role and Responsibilities
In this project, I acted as the Solution Designer, DevOps Engineer, and QA Tester.
* Formalized business and non-functional requirements (NFRs).
* Formulated tasks for Claude Code (AI-assisted development).
* Designed the Target Architecture.
* Prepared Architecture Decision Records (ADRs) for tech stack selection during the pre-sale phase.

## Technology Stack
* **Backend:** Python on AWS Lambda
* **Data Layer:** Amazon S3 (audio and transcription files), AWS DynamoDB (job status tracking)
* **Frontend:** Static HTML + Vanilla JS hosted on Amazon S3 and distributed via AWS CloudFront
* **Security:** Amazon Cognito (PKCE flow)
* **Infrastructure & IaC:** AWS API Gateway, fully provisioned via Terraform

---
## Architecture artifacts
### Cloud Architecture Diagram 
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

### Sequence Diagrams
#### Authentication
```mermaid
sequenceDiagram
    autonumber
    
    actor U as Browser (SPA)
    participant API as API Gateway
    participant C as Amazon Cognito

    U->>API: Request to API without JWT in Header
    activate API
    API->>U: Redirect to login form
    deactivate API
    activate U
    U->>C: Navigate to login form
    deactivate U
    activate C
    C->>U: Login form 
    deactivate C
    activate U
    U->>C: Enter credentials and attempt authentication
    deactivate U
    activate C
    alt Valid credentials
        C-->>U: Credentials valid, return Auth Code
    else Invalid credentials
        C-->>U: Credentials invalid, return error
    end
    deactivate C
    activate U
    U->>C: Exchange Code for JWT (/oauth2/token)
    deactivate U
    activate C
    C-->>U: Access & ID Tokens
    deactivate C
```

#### Audio File Upload Initiation
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

#### Direct Upload & Asynchronous Trigger (Event-Driven)
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

#### AI Processing & Webhook (up to several minutes)
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

#### Result Retrieval (Download)
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