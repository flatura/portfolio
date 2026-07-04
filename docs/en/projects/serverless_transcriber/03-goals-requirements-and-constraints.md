# Goals, Requirements, and Constraints
## Goals and Non-Goals
### Primary project goals

* Implement cost-optimal audio transcription for personal use

### Out of scope

* Not a publicly accessible open system
* Not a paid or monetizable platform

## Business requirements

- BR-001. The service is accessible over the internet.
- BR-002. Access is limited to authorized users.
- BR-003. The system supports transcription of long audio.
- BR-004. The system supports speaker diarization.
- BR-005. The user can download the completed transcript.

## Functional requirements

- FR-001. The user receives a presigned upload URL.
- FR-002. The system creates a transcription job whose current status the user can check without refreshing the page.
- FR-003. The system updates job status as processing progresses.
- FR-004. The UI displays a list of jobs and their current status.
- FR-005. The user receives a presigned URL for the completed transcript.
- FR-006. The webhook handler accepts a callback from the transcription provider.

## Constraints

- CON-001. Files up to 300 MB.
- CON-002. Recording duration up to 6 hours.
- CON-003. Up to 5 files transcribed concurrently.
- CON-004. 1–3 users.
- CON-005. An on-premises model is not considered.
- CON-006. Ongoing infrastructure costs must be minimal.

## Non-functional requirements

- NFR-001. Access control.
- NFR-002. Cost efficiency.
- NFR-003. Portability.
- NFR-004. Operability.
- NFR-005. Resilience of async workflow.

## Requirements (detailed)

- **BR-001. Internet accessibility**
  The system must be accessible from any device connected to the internet.
- **BR-002. Restricted access**
  The system must provide user authorization and authentication. New user registration is not planned, but user management must be supported.
- **BR-003. Speaker diarization**
  The system must support splitting the transcript by speakers.
- **BR-004. File formats**
  The system must support the most common voice recorder formats — MP3, AAC.

## Rules and constraints (detailed)

* **CON-001. Deployment region: for users in Europe, the Caucasus, and Turkey.**
  An AWS region with acceptable availability. Low latency is not a critical requirement because the primary scenario is asynchronous.

* **CON-002. Recording file size — up to 300 MB.**

* **CON-003. Single recording duration — up to 6 hours.**
  The system must operate reliably on long recordings.

* **CON-004. Final transcription cost**
  The cost per minute at 40 hours per month must not exceed $0.3/minute including infrastructure costs (reference: https://speech2text.ru/my/rate).

* **CON-005. Mandatory access restriction**
  1–2 accounts for personal use is sufficient.

* **CON-006. Running an open-source transcription model is not planned**
  Due to lack of hardware at the required level, and the economic impracticality of renting such equipment.

* **CON-007. Solution portability**
  The solution must be easy to deploy and, if needed, tear down when the need for it is temporarily gone.

* **CON-008. Minimal maintenance costs**
  The solution must require minimal resources for maintenance (security updates, etc.).
