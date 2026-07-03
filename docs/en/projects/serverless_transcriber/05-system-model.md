# System Model

## Domain Model

## Data Model

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

| Method | Path | Lambda handler | Purpose |
|-------|------|----------------|---------|
| `GET` | `/upload-url` | `get_upload_url` | Create record; return Presigned POST URL and `fileId` |
| `GET` | `/jobs` | `get_jobs` | List user's jobs (UI polling) |
| `GET` | `/download-url?fileId=...` | `get_download_url` | Verify access; Presigned GET URL for transcript |
| `POST` | `/webhook` | `webhook_assemblyai` | Transcription provider callback (`transcript_id`) |

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
