# Goals, Requirements, and Constraints

## Goals and Non-Goals

### Primary project goals

* Implement cost-optimal audio transcription for personal use

### Out of scope

* Not a publicly accessible open system
* Not a paid or monetizable platform

## Functional Requirements (FR)

- **BR-001. Internet accessibility**
  The system must be accessible from any device connected to the internet.
- **BR-002. Restricted access**
  The system must provide user authorization and authentication. New user registration is not planned, but user management must be supported.
- **BR-003. Speaker diarization**
  The system must support splitting the transcript by speakers.
- **BR-004. File formats**
  The system must support the most common voice recorder formats — MP3, AAC.

## Rules and Constraints (NFR)

* **CON-001. Availability region — European part of Eurasia.**

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
