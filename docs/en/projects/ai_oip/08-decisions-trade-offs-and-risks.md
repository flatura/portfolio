# Decisions, Trade-offs, and Risks

## Key Decisions

## Backend as control plane

The backend should define available tools, permissions, validation rules, execution boundaries, auditability, and response structure. The LLM is not the data-access system.

This was prototyped as a lab control plane. Production authentication, authorization, and audit were not implemented.

## Lab runtime separated from target architecture

LangGraph and Open WebUI were used as fast lab tools for an experimental execution flow. The target product architecture would assume a backend-native control plane, a dedicated UI, Tool Gateway, semantic layer, report service, and audit trail.

LangGraph was useful for a single-request tool loop. It was not used as durable conversation memory.

## Open WebUI as temporary interface

Open WebUI was configured as a temporary chat-like interface for PoC demonstration rather than building a dedicated executive UI upfront.

The most important limitation: each new message in Open WebUI was effectively processed as a new independent request rather than continuation of the same analytical session. Even a clarification question such as “which scenario did you mean?” did not produce a working continuation when the user answered.

See also [Architecture Decision Records](adr/index.md).

## Prototype playbook concept instead of a free tool set

The prototype did not expose all tools to the LLM at once. A diagnostic path was intended to define the domain frame and allowed tools. This remained a prototype concept, not a complete playbook engine.

## Synthetic data instead of real enterprise connectors

The PoC uses a synthetic enterprise dataset to demonstrate cross-domain diagnostics without live client data.

## RAG as document evidence, not as a SQL replacement

Structured metrics are calculated in PostgreSQL/tools. RAG is used for documents, decisions, reports, minutes, and context.

## Trade-offs

### 1. Interface

**Context.** The PoC needed a fast way to show the main user scenario: ask an analytical question, run a controlled tool flow, and return an evidence-backed answer.

**Decision.** Open WebUI as a temporary interface.

**Rejected alternative.** Building a dedicated UI first would have added frontend, auth, and conversation-history work before the architectural idea was validated.

**Trade-off.** Open WebUI did not provide durable session state for this prototype. Run details had to be generated on the backend and opened by a link. There is a risk that the PoC is perceived as “just another LLM chat”.

### 2. Execution harness

**Context.** A single request needed planning, tool calls, evidence evaluation, possible extra tool calls, and a final answer.

**Decision.** LangGraph + FastAPI as an experimental lab runtime.

**Rejected alternatives.** A Java Spring Boot backend was premature. n8n and Dify were either too rigid or too heavy for this PoC.

**Trade-off.** LangGraph should not become the production core. Workflow logic would later need a backend-native control plane. Per-request graph state is not the same as multi-turn conversation state.

### 3. Synthetic dataset

**Context.** A realistic demo needed linked finance, sales, delivery, ITSM, PMO, meetings, and documents. Real corporate data is sensitive, incomplete, and expensive to connect.

**Decision.** Use a synthetic enterprise dataset with planted cross-domain scenarios.

**Trade-off.** The PoC does not prove behavior on dirty, incomplete, or contradictory real data. Real integration problems were not tested.

### 4. Data-access layer

**Context.** The LLM must not get direct access to data.

**Decision.** A lightweight FastAPI tool-server.

**Trade-off.** The layer is sufficient to check the hypothesis “LLM selects an action, backend executes, result returns as evidence”. It is not a mature Tool Gateway with RBAC, quotas, or approval gates.

### 5. LLM API

**Context.** The PoC needed usable reasoning and fast iteration. A local model would have required hardware and serving work first.

**Decision.** External OpenAI-compatible LLM API.

**Trade-off.** External API cost, latency, and data-policy limits. Acceptable here because the PoC uses synthetic data only.

## Main risks

1. Scope explosion — the idea easily spreads into finance, process mining, goal-setting, personal assistant, meeting transcription, and daily reports. A hard vertical slice is required.
2. Missing digital traces — real companies may not have the needed data, or access may be politically blocked.
3. Weak verifiability — without a bind to tool results, an answer can look convincing and still be poorly checkable.
4. Conversation state — without multi-turn session handling, clarification questions cannot become a real analytical dialogue.
5. Corporate security — a production version would need separate work on RBAC, ACL, audit, secrets, deployment, and operations.
