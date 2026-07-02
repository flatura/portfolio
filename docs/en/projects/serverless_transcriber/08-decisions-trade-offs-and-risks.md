# Decisions, Trade-offs, and Risks

## Key Decisions

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

## Trade-offs

## Serverless vs always-on hosting

* **VPS unsuitable:** Recurring computing costs even when the service is idle; poor fit for episodic workload.
* **Telegram bot not viable:** Platform file-size limits; bot logic still requires separate hosting.

## Managed transcription API vs self-hosted models

* **Zero GPU/hosting budget** ruled out running open-source speech models on owned infrastructure.
* **Third-party API (AssemblyAI)** chosen for best quality-to-price ratio; concurrency cap of 5 parallel jobs enforced at the provider integration layer.

See also [Architecture Decision Records](adr/index.md).
