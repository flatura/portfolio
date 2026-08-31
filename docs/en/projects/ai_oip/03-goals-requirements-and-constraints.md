# Goals, Requirements, and Constraints

## Goals and Non-Goals

### Primary project goals

- Check whether an LLM can work with prepared enterprise traces through controlled backend tools, not through direct data access.
- Build a reproducible lab stand with synthetic enterprise data.
- Implement an experimental vertical slice: user request → controlled execution flow → tool selection → backend tool call → structured result → evidence-backed answer → execution trace.
- Show an approach to managerial diagnostics where conclusions rest on facts, documents, calculations, and explicit analysis limits.
- Document an architectural direction for a future product: backend control plane, Tool Gateway, Tool Registry, playbook-based scenarios, semantic layer, audit trail.

### What this PoC is not

- Not a real MVP.
- Not a production-ready enterprise platform.
- Not a complete multi-turn conversational agent.
- Not an autonomous "AI executive".
- Not a BI replacement.
- Not a complete process-mining product.
- Not a production authentication and authorization model.
- Not a set of real enterprise data connectors.
- Not a complete playbook engine.
- Not an evaluation pipeline for answer quality.
- Not a production deployment model.
- Not a full observability and audit model.

## What was implemented

- chat-like UI based on Open WebUI;
- experimental LangGraph-based execution flow;
- backend tools for accessing prepared synthetic data;
- initial tool registry / tool description concept;
- synthetic financial and cross-functional management scenarios;
- single-turn analytical requests;
- evidence-backed response pattern;
- basic execution trace / run details;
- architectural documentation and future direction.

The prototype also explored a playbook-routing concept: a question could be directed into a bounded diagnostic path with a limited tool set. This was a prototype playbook concept, not a complete playbook engine.

## What was not implemented

- full multi-turn session state;
- continuation of an analytical scenario after a clarification question;
- correct handling of the user’s answer to system clarification;
- durable conversation memory;
- persisted analytical run context;
- production authentication and authorization;
- real enterprise data connectors;
- complete playbook engine;
- evaluation pipeline for answer quality;
- production deployment model;
- full observability and audit model.

## Current limitations

The most important limitation: each new message in Open WebUI was effectively processed as a new independent request rather than continuation of the same analytical session.

Even when the prototype asked a clarification question such as “which scenario did you mean?”, the next user answer was processed as a new independent request, not as continuation of the previous run.

The limitation was intentionally documented. The prototype validated a single-turn controlled execution idea; it did not deliver a conversational analytics product.

## Requirements

The items below describe the PoC intent. They should not be read as a claim that every requirement was fully implemented.

- **BR-001. Evidence-backed managerial analytics**
  The prototype should investigate a managerial question and return a conclusion grounded in calculations, documents, tool results, and explicit analysis limits.

- **BR-002. Faster first-pass analysis**
  The prototype should reduce the time of a first-pass hypothesis check by routing the request, calling tools, collecting evidence, and forming a structured answer.

- **BR-003. Transparency instead of opaque AI**
  The user should see not only the final text, but also the basis of the conclusion: selected diagnostic path, tool calls, parameters, results, sources, and limits.

- **BR-004. Safe data access model**
  The LLM should not receive direct access to databases, documents, or arbitrary SQL.

- **BR-005. Domain diagnostic paths**
  Analysis should be framed as bounded diagnostic paths, not as free chat over the full tool catalog.

- **BR-006. Demonstration without client data**
  The PoC should demonstrate the approach on a synthetic enterprise dataset.

- **BR-007. Extensibility direction**
  New analysis domains should be addable through tools, tool descriptions, and diagnostic paths rather than one giant prompt.

- **BR-008. Future enterprise constraints**
  Architectural choices should leave room for later audit, RBAC/ACL, controlled integrations, private deployment, and workflow portability. These were not implemented in the PoC.

## Functional requirements

- **FR-001. Chat-like interface for an analytical question**
  The user should be able to ask a free-form managerial question through a chat-like UI.

- **FR-002. Diagnostic path selection**
  The prototype should determine the domain of the question and select a bounded diagnostic path, or ask a clarification. Clarification was explored, but the user’s answer was not handled as continuation of the same run.

- **FR-003. Tool restriction by diagnostic path**
  A selected path should limit the available tools so the LLM does not work with the full catalog at once.

- **FR-004. Data access only through the tool-server**
  The LLM should receive data through controlled backend tools.

- **FR-005. Structured tool results**
  The tool-server should return structured JSON with result, metadata, status, and enough technical detail for a run log.

- **FR-006. Financial metric calculation**
  Financial metrics should be calculated from structured database data, not generated by the LLM.

- **FR-007. RAG as document evidence direction**
  Documents should be usable as additional evidence through a MinIO/Qdrant/RAG contour.

- **FR-008. Structured analytical answer**
  The final answer should include facts, interpretation, hypotheses, analysis limits, and recommended actions where possible.

- **FR-009. Run transparency**
  The prototype should expose the selected diagnostic path, tool calls, inputs, outputs, and basic run details.

- **FR-010. Same-language response**
  The prototype should answer in the same language as the user question.

- **FR-012. Clarifying question**
  If the question is incomplete, too broad, or missing critical parameters, the prototype may ask for the missing information. This was not a working multi-turn loop: the next message was treated as a new request.

- **FR-013. Reproducible synthetic data import**
  The lab stand should restore demo state from the repository: PostgreSQL seed, MinIO objects, Qdrant artifacts, manifests, and scripts.

- **FR-014. Several connected synthetic domains**
  The demo dataset should contain linked domains: finance, sales, products, documents, delivery, ITSM, PMO, meetings, and tasks.

## Constraints

- **CON-001. Verifiable conclusions**
  A material conclusion should be linked to a tool result, document, calculation, or an explicit limit.

- **CON-002. Controlled data access**
  The LLM should not get direct access to PostgreSQL, Qdrant, MinIO, the filesystem, or arbitrary SQL.

- **CON-003. Execution traceability**
  A run should preserve the selected diagnostic path, tool calls, parameters, results, and the final answer at a basic level.

- **CON-004. Synthetic data only**
  The PoC uses synthetic data. Real client data is not connected.

- **CON-005. Limited PoC scale**
  The PoC is sized for demo scenarios and architectural validation, not production load, mass users, or SLA.

- **CON-006. LLM usage**
  A local LLM is a target for a future product. The PoC may use an external LLM and should remain adaptable to model replacement.

## Assumptions

- The prototype works on a synthetic dataset, not on live client data.
- Some cross-domain scenarios are demonstrative and need further stabilization.
- The RAG contour shows a document-evidence direction; it is not a mature ingestion/lifecycle solution.
- Tool Registry and related factory ideas are early: part implemented, part described architecturally.
- The UI is a temporary chat-like harness, not a target executive cockpit.
- The prototype does not prove production readiness. It proves that a controlled LLM analytics loop can be assembled and demonstrated on synthetic data.
