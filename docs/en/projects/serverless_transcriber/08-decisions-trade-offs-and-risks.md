# Decisions, Trade-offs, and Risks

## Key decisions

### Full event-driven model
Transcription is a long-running process that may exceed Lambda function execution time.
    * *Decision:* Implement an event-driven model. Temporally decouple audio file submission from text result retrieval. Find a transcription provider that offers webhook notification functionality.

### Working with 300 MB files
File size may exceed API Gateway limits and increase Lambda function runtime.
    * *Decision:* Use Presigned URL functionality provided by Amazon S3 out of the box. This allows the client to access S3 directly, bypassing API Gateway and Lambda.

## Architectural trade-offs (ADR)

### 1. Optimal architectural style
#### Context
The episodic nature of tool usage, a small number of use cases, broad availability zone, and strict infrastructure and maintenance cost requirements must be accounted for.

#### Decision
Use a Serverless approach and AWS Lambda infrastructure.

#### Rejected alternative
VPS, Telegram bot

#### Rationale

- Lambda functions are billed for execution time; with episodic usage they can fit within the Free tier (1M requests or 400 TB-s per month), i.e. business logic is free under given conditions. AWS Lambda also handles infrastructure security on Amazon's side, eliminating maintenance costs.

- VPS require periodic payment for capacity (even when the service is unused this can be $3–7 per month), and require resources to maintain the required security level (OS security updates, fresh packages, etc.).

- A Telegram bot as a channel is convenient enough, but unsuitable due to audio file size limits (50 MB) + it does not eliminate the need to host bot logic somewhere (VPS with all that entails).

#### Trade-offs

* Serverless requires more careful design, maximizing offloading of heavy operations outside functions (Presigned URLs in S3). Function stability requirements must be higher. Quotas on invocations and spend alerts must be configured.
* Serverless is harder to debug.

### 2. Optimal transcription infrastructure
#### Context
Budget for running an open-source model on owned hardware is not planned.

#### Decision
Use a third-party transcription API service.

#### Rejected alternative
Locally run open-source model, rented hardware for running an open-source model.

#### Rationale
- A third-party transcription API service works fast and requires no maintenance. AssemblyAI was chosen as optimal quality-to-price ratio — $0.15 per hour. Cost per minute is $0.0025 when using Amazon cloud and serverless approach, which is 120 times less than required. The limit of 5 concurrent transcription processes is also met.

- No hardware available for local model deployment (minimum requirements — 16 GB RAM and 8 GB video memory on an external GPU). Purchasing additional hardware is outside the digital nomad paradigm.

- Renting compatible hardware costs $5–10 per month with hourly billing, requires separate resources for deployment, launch, and security (security updates). Running such hardware continuously costs $40–60 per month. The solution is suboptimal.

#### Trade-offs

- Recordings are sent to a third-party service; the privacy requirement is not met. Agreed with the stakeholder.

- The third-party service may change pricing or shut down.

- API keys must be stored securely. Storing in code is insecure and bad practice. AWS Secrets Manager costs $0.40 per month + $0.05 per 10,000 requests — this must be factored into the final cost per transcription minute.

### 3. User data isolation

#### Context
Access restriction and data separation requirements must be met, and the service must support multiple users without open registration.

#### Decision
AWS Cognito

#### Rejected alternative
Password protection of a static HTML page

#### Rationale

- AWS Cognito has built-in account management, registration, 2FA, brute-force protection, etc. The service integrates seamlessly into the AWS ecosystem. Project needs fit within the Free tier (<10,000 MAU).

- HTML password protection is poorly adapted to brute-force attacks; changing the password via code changes is not best practice. No ability to separate access between multiple users.

- A custom access management system is over-engineering on top of a single business process.

#### Trade-offs
- Free tier terms may change and user management functionality may become paid. Solution cost must be re-evaluated.

... Key ADRs are presented only partially for demonstration purposes
