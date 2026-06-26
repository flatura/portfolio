# Requirements

## Implemented MVP Capabilities

* Chat-based executive query interface through Open WebUI.
* LangGraph/FastAPI `agent-lab` runtime for diagnostic workflows.
* Tool-server layer for controlled backend tool execution.
* Tool Registry concept for tool discovery and playbook constraints.
* Financial Operations playbook for margin, revenue, discounts, COGS, and product mix diagnostics.
* Executive Operations / Delivery-oriented playbook for roadmap, delivery, ITSM, PMO, meetings, tasks, and KPI anomaly analysis.
* Synthetic enterprise dataset with connected business domains.
* PostgreSQL-backed metric tools.
* Qdrant/MinIO-backed document evidence direction for RAG.
* Playbook routing based on user intent.
* Execution timeline and run details for transparency.
* Same-language response handling for user-facing answers.
* Initial guardrails against wrong fallback behavior, repeated tool calls, and unsupported analysis paths.
