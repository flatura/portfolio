# Data Model

## DynamoDB - job status tracking

Each transcription job is stored as a record with a lifecycle status:

| Status | Meaning |
|--------|---------|
| `UPLOADING` | Presigned upload URL issued; client upload in progress |
| `TRANSMITTING` | Audio uploaded to S3; submission to AssemblyAI initiated |
| `PROCESSING` | AssemblyAI is transcribing (`transcript_id` stored) |
| `READY` | Transcript saved to S3; available for download |
| `ERROR` | AssemblyAI or pipeline failure (reason logged) |

## Amazon S3

* **File storage bucket:** raw audio uploads and generated transcript files (`Transcript.txt`).
* **Static website bucket:** SPA assets served via CloudFront.
