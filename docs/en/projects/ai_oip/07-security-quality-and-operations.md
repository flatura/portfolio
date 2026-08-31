# Security, Quality, and Operations

## Security and Access Model

### Implemented in the PoC

- Only synthetic data is used.
- The LLM does not get direct access to PostgreSQL, Qdrant, or MinIO.
- Data access goes through controlled HTTP tools.
- Tools have explicit input contracts.
- Financial calculations are performed by named queries / backend logic, not by arbitrary SQL from the LLM.
- Run details can show the selected diagnostic path, tool calls, inputs, and outputs.

### Target production model — not implemented

- SSO / IdP integration.
- RBAC / ABAC.
- Tenant isolation.
- ACL-aware RAG retrieval.
- Tool permissions by diagnostic path, user role, and domain.
- Read-only mode by default.
- Approval gates for write actions.
- Full audit log: run_id, user_id, tool_id, params hash, result hash, source refs.
- Secrets management.
- On-prem/private deployment option.

## Controlled LLM execution

The LLM can plan the next step, but data access is delegated to controlled backend tools — not free chat over corporate data.

## Controlled tool access model

The LLM never queries PostgreSQL, Qdrant, or MinIO directly.

## Non-Functional Requirements

The PoC was not sized or proven against production NFR. The relevant lab constraints were:

- demonstrable single-request flow;
- traceability of tool calls;
- no direct model access to data stores;
- reproducible Docker Compose stand;
- synthetic data only.

## Failure Modes

| Failure mode | How it appeared | Notes |
|---|---|---|
| Wrong diagnostic-path routing | An operational question could go into a finance path | Clarification was explored, but the user’s answer was not continued as the same session |
| Unsupported question | Question outside dataset/tool coverage | Explicit limitation is preferable to a fabricated answer |
| Duplicate tool calls | Same tool called with the same parameters | Fingerprint `tool_id + canonical_json(args)`, run-local cache |
| Stub/empty tool response | Tool returned no data or a stub | Status handling, warning, insufficient-evidence verdict |
| Missing RAG evidence | Document layer finds no confirmation | Explicit limitation: document evidence not found |
| Hallucinated conclusion | LLM states a conclusion without evidence | Evidence-first prompt; no evaluation pipeline was implemented |
| Incomplete cross-domain linkage | Metrics exist, but finance ↔ delivery ↔ ITSM is not proven | Needs a stronger semantic layer; not fully stabilized |
| External LLM unavailable | API down or rate-limited | Retry/backoff and local-model option are future work |
| Context overflow | Tool manifest/evidence too large | Context budget, summarization, retrieval filters — early |
| Data leakage risk | Model sees extra data | Tool-level permissions and no direct data access; no production ACL |

## Sizing and Cost Notes

The current PoC is sized for demonstration:

- 1-3 concurrent users;
- a few diagnostic runs during a demo;
- synthetic dataset for 2024-2025;
- tens/hundreds of thousands of rows at most in lab data;
- one run usually expected to stay within 1-10 tool calls;
- cost is driven by LLM API calls and Docker/VPS/local infrastructure;
- production sizing was not performed.

Production would need separate estimates for source volume, document corpus, ingestion frequency, users, RPS, SLA, LLM routing cost, and private deployment. That work was not done.
