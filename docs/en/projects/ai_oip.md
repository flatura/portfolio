## AI Operational Intelligence Platform

**Type:** Enterprise AI / Decision-support system / Agentic analytics prototype  
**Role:** System Designer, AI-assisted Prototype Engineer
**Status:** working prototype, May 2026

### Context
A prototype system for managerial analytics, where the LLM does not "answer from memory" but operates within a controlled execution loop: it selects permitted tools, calls backend functions, retrieves verifiable data, preserves the execution trace, and generates an executive-level response based on evidence.

### Responsibilities
- Designed the overall architectural framework of the project.
- Built a LangGraph-based agent harness for controlled scenario execution.
- Defined a tool registry to describe available tools and constraints.
- Prepared synthetic financial and cross-functional managerial scenarios.
- Configured Open WebUI as a familiar chat interface for PoC demonstration.
- Developed the approach to system transparency: tool calls, parameters, results, evidence.
- Shaped the development direction: playbooks, evidence graph, report generation, tool generator.

### Key Decisions
- Controlled LLM invocation instead of a free chat approach.
- Tool registry as a catalog of instruments for the LLM.
- Evidence-based answers: the response must reference data, not just the model's reasoning.
- Run trace as the foundation for trust, debugging, and audit.
- Separation of roles: the backend sets the boundaries, the LLM acts within a constrained scenario.

## UI Screenshots
### "What can you do?"
<figure markdown>
![UI_1](assets/ai_oip/what.png)
<figcaption>"Что ты умеешь?"</figcaption>
</figure>

### Financial playbook: gross margin drop hypothese
<figure markdown>
![UI_1](assets/ai_oip/gross_margin.png)
<figcaption>Gross margin drop hypothese</figcaption>
</figure>

### Execution playbook: KPI anomaly
<figure markdown>
![UI_1](assets/ai_oip/KPI.png)
<figcaption>KPI anomaly</figcaption>
</figure>

### Technology Stack
LangGraph, Python, Open WebUI, synthetic datasets, tool registry, agent harness, LLM-assisted development, evidence-based analytics.

### What the project demonstrates
This project demonstrates my transition from classical system analysis to designing enterprise AI systems: assembling a controlled loop with tools, constraints, tracing, verifiable data, and clear managerial value.

