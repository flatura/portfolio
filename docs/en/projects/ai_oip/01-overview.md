# Overview

## Summary

**AI Operational Intelligence Prototype** — a technical PoC / working prototype of controlled LLM execution for evidence-backed analytics.

The original working name was AI Operational Intelligence Platform / Executive Decision Intelligence. That name described the intended product direction, not the maturity of what was built.

The prototype explores how an executive analytics assistant could be built. A user asks an analytical question in a chat-like UI; the backend runs a controlled execution flow over prepared synthetic data. The LLM is intended to act inside a backend-mediated tool environment, not as a free-form chatbot with arbitrary data access.

This is not a production platform and not a complete multi-turn decision-support product. It is an experimental enterprise AI architecture prototype that validated a bounded execution idea.

## What was prototyped

- chat-like UI based on Open WebUI;
- experimental LangGraph-based execution flow;
- backend tools for accessing prepared synthetic data;
- initial tool registry / tool description concept;
- synthetic financial and cross-functional management scenarios;
- single-turn analytical requests;
- evidence-backed response pattern;
- basic execution trace / run details;
- architectural documentation and future direction.

## Technology Stack

| Layer | PoC choice | Role |
|---|---|---|
| Chat-like UI | Open WebUI | Temporary demo interface |
| Execution flow | FastAPI + LangGraph | Experimental single-request diagnostic flow |
| Tool execution | FastAPI tool-server | Controlled backend tools, validation, structured output |
| Structured data | PostgreSQL | Synthetic finance, delivery, ITSM, PMO, meetings data |
| Document store | MinIO + Qdrant | Document evidence direction for RAG |
| Runtime/cache | Redis | Lab runtime support |
| LLM | OpenAI-compatible API | Planning and synthesis; not a source of truth |
| Infra | Docker Compose | Reproducible lab stand |

**Architecture patterns explored:** Tool Gateway, Tool Registry concept, prototype playbook routing, RAG direction, run trace, evidence trail.

**Development approach:** AI-assisted prototyping, synthetic data generation, scenario-driven PoC validation.
