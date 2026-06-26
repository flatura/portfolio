# API Contracts

## API Gateway (authenticated)

| Method | Path | Lambda handler | Purpose |
|--------|------|----------------|---------|
| `GET` | `/upload-url` | `get_upload_url` | Create job record; return Presigned POST URL and `fileId` |
| `GET` | `/jobs` | `get_jobs` | List current user's jobs and statuses (UI polling) |
| `GET` | `/download-url?fileId=...` | `get_download_url` | Verify access; return Presigned GET URL for transcript |
| `POST` | `/webhook` | `webhook_assemblyai` | AssemblyAI completion callback (`transcript_id`) |

All API Gateway routes require a valid JWT (Amazon Cognito) except `/webhook` (provider callback).

## Amazon Cognito (Hosted UI / PKCE)

| Method | Path | Purpose |
|--------|------|---------|
| `POST` | `/oauth2/token` | Exchange authorization code for Access & ID tokens |

## AssemblyAI (external)

| Method | Path | Purpose |
|--------|------|---------|
| `POST` | `/v2/transcript` | Submit audio URL + webhook URL; returns `transcript_id` |
| `GET` | `/v2/transcript/{id}` | Fetch completed transcription text |

## Amazon S3 (direct client access)

| Method | Target | Purpose |
|--------|--------|---------|
| `POST` | Presigned POST URL | Direct audio upload (bypasses API Gateway payload limits) |
| `GET` | Presigned GET URL | Direct transcript download |
