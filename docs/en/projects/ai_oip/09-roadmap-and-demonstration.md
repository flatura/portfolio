# Roadmap and Demonstration

## Roadmap

| Phase | Goal | Exit criteria |
|---|---|---|
| v0.1 Lab PoC | Show controlled LLM execution | Request → diagnostic path → tool calls → answer + run details. PROTOTYPED |
| v0.2 Stabilized run | Stabilize one financial and one operational scenario | Demo can run without hand-substituting the result. PROTOTYPED |
| v0.3 Document evidence layer | Strengthen evidence through RAG | Answer can refer to documents/chunks. PROTOTYPED as a direction |
| v0.4 Tool Registry v0.1 | Move hardcoded tools toward a registry | Tools described through a manifest; separate tool-server. PROTOTYPED as an initial concept |
| v0.5 Executive report | Move from chat answer to report artifact | Executive brief + signal cards + evidence appendix. NOT IMPLEMENTED |
| v0.6 Cross-domain scenario | Show finance → delivery → ITSM → PMO chain | Prototype can explore a planted cross-domain cause. EXPLORED, NOT FULLY STABILIZED |
| v1 Real MVP | See below | Not reached |

## Next step toward MVP

To become a real MVP, the prototype would need:

1. multi-turn session state;
2. correct handling of clarifying questions;
3. continuation of the same analytical run;
4. persisted run/session context;
5. more formal tool registry schema;
6. evaluation harness;
7. read-only connectors to realistic enterprise data sources;
8. authentication and authorization model;
9. audit and observability layer;
10. demo scenarios with measurable expected outcomes.

The current work is a technical PoC / working prototype. It is not yet a real MVP.

## Demo Scenarios

Demo scenarios below are single-turn analytical requests on synthetic data. They show the intended flow, not a complete conversational product.

### Financial Performance Diagnosis

Example question:

> Why did gross margin drop in March?

Expected prototype flow: route into a financial diagnostic path, call metric tools for gross margin, revenue, discounts, COGS, and product mix, then produce a structured summary with evidence and limitations.

### Operational / KPI Anomaly Diagnosis

Example question:

> Why is time-to-market unstable while local team KPIs look normal?

Expected prototype flow: route into an operational diagnostic path and inspect delivery, PMO, ITSM, meeting decisions, and related evidence for cross-functional bottlenecks that are not visible in isolated KPI dashboards.

### Cross-Domain Management Hypothesis

Target scenario:

> Identify the top problematic projects, explain the selection criteria, describe the issue for each project, and prepare a meeting agenda for product owners.

This scenario shows the intended product direction: not only retrieving delayed tasks, but turning structured and document evidence into a management-ready diagnostic brief. It was explored as a target demo-flow and still needs stabilization of cross-domain linkage and evidence quality.

## UI Screenshots

### "What can you do?"

<figure markdown>
![UI_1](/portfolio/assets/ai_oip/what.png)
<figcaption>Prototype catalog of diagnostic paths and tools</figcaption>
</figure>

### Financial diagnostic path: gross margin drop hypothesis

<figure markdown>
![UI_2](/portfolio/assets/ai_oip/gross_margin.png)
<figcaption>Financial performance diagnosis with tool-based evidence</figcaption>
</figure>

<figure markdown>
![UI_3](/portfolio/assets/ai_oip/gross_margin_report.png)
<figcaption>Financial performance diagnosis usage report</figcaption>
</figure>

<figure markdown>
![UI_4](/portfolio/assets/ai_oip/tools_called.png)
<figcaption>Financial performance diagnosis: called tools and run details</figcaption>
</figure>

### Operational diagnostic path: KPI anomaly

<figure markdown>
![UI_5](/portfolio/assets/ai_oip/KPI.png)
<figcaption>Operational anomaly diagnosis across delivery, ITSM, PMO, and documents</figcaption>
</figure>

## What This Demonstrates

This project demonstrates the ability to take an ambiguous enterprise AI idea and turn it into a constrained, demonstrable prototype.

It shows:

- understanding of enterprise AI risks;
- controlled LLM execution instead of free chat;
- separation of chat UI and execution layer;
- tool-mediated analytics;
- evidence-backed response design;
- execution trace as a trust/debugging mechanism;
- ability to build a working prototype quickly;
- ability to honestly document limitations.

The core value is not "using an LLM". The core value is designing a system where AI reasoning is bounded by architecture, evidence, tool contracts, and auditability — and stating clearly what the prototype did and did not implement.
