# System Model

## Data Model

### TranscriptionJob
The core entity of the transcription process.

Attributes:

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

### System invariants

- a job belongs to one user;
- a download URL is issued only to the job owner;
- a transcript can be downloaded only in `READY` status;
- the webhook must be idempotent;
- a repeated callback from the provider must not create a new transcript;
- a failed job must not block the list of other jobs;
- presigned URLs have a limited lifetime.

## DynamoDB — job statuses

Each transcription job is stored as a DB record with a lifecycle:

| State Machine | Meaning |
|--------|----------|
| `UPLOADING` | Presigned URL issued; client upload in progress |
| `TRANSMITTING` | Audio uploaded to S3; submission to service initiated |
| `PROCESSING` | Service is transcribing (`transcript_id` stored) |
| `READY` | Transcript saved to S3; available for download |
| `ERROR` | AssemblyAI or pipeline failure (reason logged) |

## Amazon S3

* **File bucket:** audio uploads and generated transcripts (`Transcript.txt`).
* **Static website bucket:** SPA served via CloudFront.

## API Contracts

## API Gateway (authentication)

| Method | Path | Purpose |
|-------|------|---------|
| `GET` | `/upload-url` | Create record; return Presigned POST URL and `fileId` |
| `GET` | `/jobs` | List user's jobs (UI polling) |
| `GET` | `/download-url?fileId=...` | Verify access; Presigned GET URL for transcript |
| `POST` | `/webhook` | Transcription provider callback (`transcript_id`) |

All API Gateway routes require JWT (Amazon Cognito) except `/webhook` (transcription provider callback).

## Amazon Cognito (Hosted UI / PKCE)

| Method | Path | Purpose |
|-------|------|---------|
| `POST` | `/oauth2/token` | Exchange authorization code for Access & ID tokens |

## External transcription provider API

| Method | Path | Purpose |
|-------|------|---------|
| `POST` | `/v2/transcript` | Submit audio URL + webhook URL; returns `transcript_id` |
| `GET` | `/v2/transcript/{id}` | Fetch completed transcription text |

## Amazon S3 (direct client access)

| Method | Target | Purpose |
|-------|------|---------|
| `POST` | Presigned POST URL | Direct audio upload (bypasses API Gateway limits) |
| `GET` | Presigned GET URL | Direct transcript download |
