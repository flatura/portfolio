# Требования

## Реализованные возможности MVP

* Chat-based executive query interface через Open WebUI.
* LangGraph/FastAPI `agent-lab` runtime для diagnostic workflows.
* Tool-server layer для controlled backend tool execution.
* Концепция Tool Registry для tool discovery и playbook constraints.
* Financial Operations playbook для диагностики margin, revenue, discounts, COGS и product mix.
* Executive Operations / Delivery-oriented playbook для анализа roadmap, delivery, ITSM, PMO, meetings, tasks и KPI anomalies.
* Синтетический enterprise dataset со связанными бизнес-доменами.
* PostgreSQL-backed metric tools.
* Направление Qdrant/MinIO-backed document evidence для RAG.
* Playbook routing на основе user intent.
* Execution timeline и run details для прозрачности.
* Same-language response handling для user-facing answers.
* Начальные guardrails против wrong fallback behavior, repeated tool calls и unsupported analysis paths.
