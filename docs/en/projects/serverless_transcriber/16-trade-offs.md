# Trade-offs

## Serverless vs always-on hosting

* **VPS unsuitable:** Recurring computing costs even when the service is idle; poor fit for episodic workload.
* **Telegram bot not viable:** Platform file-size limits; bot logic still requires separate hosting.

## Managed transcription API vs self-hosted models

* **Zero GPU/hosting budget** ruled out running open-source speech models on owned infrastructure.
* **Third-party API (AssemblyAI)** chosen for best quality-to-price ratio; concurrency cap of 5 parallel jobs enforced at the provider integration layer.
