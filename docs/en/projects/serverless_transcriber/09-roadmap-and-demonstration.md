# Roadmap and Demonstration

## Roadmap

| Phase | Goal | Changes | Exit criteria |
|---|---|---|---|
| v1 | Basic transcription | upload, async transcription, status, download | stable processing of long files |
| v1.1 | Operational resilience | stuck job detection, quota and budget alerts, old log cleanup, old file cleanup | predictable operation without manual monitoring |
| v2 | Transcript post-processing | speaker-aware summarization | user receives not only a transcript but also a brief summary |
| v3 | Format expansion | additional formats, metadata extraction | less manual preparation of source audio and transcript post-processing |

## Screenshots and demo

### Main menu

<figure markdown>
![UI_1](/portfolio/assets/transcriber/main_menu.webp)
<figcaption>Main menu</figcaption>
</figure>

### Uploading an audio recording

<figure markdown>
![UI_1](/portfolio/assets/transcriber/loading.webp)
<figcaption>Uploading an audio recording</figcaption>
</figure>

### File processing

<figure markdown>
![UI_1](/portfolio/assets/transcriber/processed.webp)
<figcaption>Processing the recording</figcaption>
</figure>

## What this project demonstrates

This project demonstrates my ability to:

- translate a personal/operational need into requirements, constraints, and an architectural solution;
- design a serverless process accounting for long asynchronous operations;
- use AWS services to minimize ongoing costs;
- bypass API Gateway/Lambda limits via direct upload to S3 object storage;
- design a state machine for the job lifecycle;
- apply Cognito, JWT, and presigned URLs for restricted file access;
- document architectural trade-offs through ADRs;
- use Terraform for reproducible infrastructure deployment.
