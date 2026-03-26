# Home# Dmitry M.
**System Designer | Integration & Data Design | Solution Architecture Track | Building B2B SaaS**

Systems analyst and technical designer with an engineering background in infrastructure, software development, and internal systems. I work at the intersection of business requirements, data models, integrations, and practical implementation. My current career direction is Solution Architecture Associate.

## Core Focus
- Solution elaboration at the system design level
- Data modeling and integration design
- API and ETL specifications
- Architecture artifacts: C4, DFD, ADR
- Internal tools built with Java / Spring Boot
- Practical engineering with infrastructure constraints in mind

## Core Competencies
- System Analysis
- Solution Design
- Data Modeling
- Integration Design
- API Design
- ETL Specifications
- SQL-based Analysis
- Java / Spring Boot
- Technical Documentation
- Infrastructure-aware Engineering

---

## MLG

**Type:** B2B SaaS / botanical domain  
**Role:** Co-founder, System Designer, Backend-oriented Engineer  
**Status:** active

### Context
A platform for botanical organizations and plant collections. It is being designed as a practical B2B system with attention to domain complexity, role-based access control, and long-term product evolution.

### Scope of Contribution
- Elaborating the domain model and key system scenarios
- Designing backend architecture and data structures
- Preparing technical documentation and system-level decisions
- Working together with a domain expert
- Hands-on backend implementation and coordination of the overall technical structure of the project

### Key Decisions
- Soft multi-tenancy
- Context-aware RBAC
- Hybrid domain model: current-state entities plus append-only event history for traceability and digital plant passports
- Separation of responsibilities between the application model, the dictionary layer, and operational workflows

### Technology Stack
Java, Spring Boot, PostgreSQL, Docker, GitHub, AI-assisted development workflow

### Links
[Project details](projects/mlg.md) | [C4 diagrams](/portfolio/assets/MLG_Context+Container_Diagram_en_safe.drawio.png) | [UI]()

---

## Serverless AI-Powered Transcriber
**Type:** Cloud-Native SaaS / Serverless Platform
**Role:** Solution Architect & Lead Designer
**Status:** Active

### Context
A high-performance online service for automated audio transcription. The project addresses the need for a scalable, cost-effective, and secure way to process long-form audio recordings using external AI engines.

### Areas of Responsibility
End-to-End Solution Design: Architecting the flow from secure user authentication to asynchronous file processing.

### Implementation Strategy
Orchestrating an AI-assisted development workflow (Claude Code) to accelerate delivery.

### Infrastructure & Deployment
Managing the full lifecycle via IaC and automated invalidation/sync processes.

### Key Architectural Decisions
Serverless-First Approach: Zero maintenance and near-zero idle costs (Pay-per-use model).

Event-Driven Asynchronous Pipeline: Leveraged S3 Triggers and API Webhooks to handle long-running AI tasks without blocking the UI.

Offloaded Data Transfers: Used S3 Presigned URLs (POST/GET) to handle multi-gigabyte uploads directly, bypassing API Gateway limits.

Secure Authentication: Implemented Amazon Cognito with PKCE flow for secure, token-based frontend access.

Infrastructure as Code (IaC): 100% reproducible environment managed through Terraform.

### Technology Stack
Cloud: AWS (Lambda, S3, API Gateway, DynamoDB, Cognito, CloudFront)
Language: Python 3.12 (Backend), Vanilla JavaScript (Frontend)
IaC: Terraform
AI Engine: AssemblyAI (Universal-3-Pro model)
Workflow: Claude Code, Git

[Project details](projects/serverless_transcriber.md)

---

## Supply Chain Optimization for FMCG

**Type:** Enterprise / decision-support systems  
**Role:** Systems Analyst / System Designer
**Status:** commercial project

### Context
Participation in two initiatives for an FMCG manufacturer:
- ML-based demand forecasting
- Mathematical production planning

### Scope of Contribution
- Elaborating business and functional requirements
- Process modeling in BPMN / Camunda
- Identifying data sources and ETL preparation requirements
- Validating R&D hypotheses using Jupyter Notebook, SQL, and AI-assisted Python-based data analysis
- Preparing architecture artifacts together with the Enterprise Architect
- Designing the data model, DDL, API specifications, and ETL contracts for the solver-based optimization workflow
- Evolving modular documentation in Confluence

### Key Outcome
The resulting technical materials, data model, and architecture artifacts helped stakeholders assess implementation complexity and supported the decision to adopt a packaged solution instead of continuing in-house development.

### Technology Stack
BPMN, Camunda, SQL, Python, Jupyter Notebook, Confluence, C4, DFD, Gurobi

[Project details](projects/fmcg_forecaster_planner.md)

---

## Enterprise GIS / ad-hoc Railway Graph Tooling

**Type:** Enterprise GIS / internal tooling  
**Role:** Systems Analyst / Technical System Designer  
**Status:** commercial project

### Context
Work in an enterprise GIS domain at the intersection of system analysis, data processing, infrastructure, and application development.

### Scope of Contribution
- Preparing and refining business and system requirements
- Working with architects on solution elaboration
- Coordinating delivery with Information Security requirements and project constraints in mind
- Designing and implementing railway graph data processing algorithms
- Deploying internal GIS infrastructure
- Developing an internal tool for visual editing and cleanup of graph data

### Key Outcomes
- Reduced cold data load time from 24 to 4 seconds through algorithms mapping railway polylines to transport graph nodes.
- Deployed an internal tile server and routing engine, allowing the team to operate independently of external Projects GIS modules.
- Designed and built an internal Spring Boot + OpenLayers tool that enabled preparation of more than 10,000 infrastructure objects in 4 weeks.
- The tool and documentation package were retained in the corporate GitLab as a reusable internal solution

### Technology Stack
Java, Spring Boot, JDBC, OpenLayers, OSRM, Docker, Confluence, Jira, UML

[Project details](projects/gis_bi_1.md)

---

## KPI / MBO Internal System

**Type:** Internal automation / performance management  
**Role:** Head of IT / Internal Systems Developer  
**Status:** implemented prototype

### Context
An internal project focused on automating performance evaluation and management workflows in a distributed organization.

### Scope of Contribution
- Requirements gathering and process modeling
- Designing a KPI / MBO system prototype
- Developing internal solutions with Java / Spring Boot
- Supporting the transition of the IT function from operational support to internal process automation

### Additional Outcomes
- Designed and implemented a QR-code-based inventory system
- Established technical documentation standards and a unified internal knowledge base
- Supported and developed the IT infrastructure of a distributed organization

### Technology Stack
Java, Spring Boot, Docker, Process Automation, Technical Documentation

🔗 [Project details](projects/fastmbo.md) | 🔗 [ADR](projects/fastmbo-adr.md)

---

# Professional Direction

## System Design
I work on solutions at the intersection of requirements, data, integrations, and practical implementation. My primary interest is in systems where structure, traceability, maintainability, and a reasonable balance between delivery speed and technical sustainability matter.

## Engineering Foundation
I have a 10+ years of engineering background in infrastructure, virtualization, networking, internal platforms, and application development. This helps me account not only for the logical solution model, but also for operational constraints.

## Current Development Track
I am moving toward Solution Architecture Associate through:
- hands-on system design
- architecture artifacts
- AI-assisted prototyping
- development of my own SaaS projects
- deeper work in data / integration / backend design

---

# Technologies and Tools

## Analysis and Design
System Analysis, Solution Design, Data Modeling, Integration Design, API Design, ETL Specifications, BPMN, C4, DFD, ADR

## Backend and Data
Java, Spring Boot, JDBC, PostgreSQL, SQL, Python, Jupyter Notebook

## Infrastructure and Tooling
Docker, OSRM, OpenLayers, Confluence, Jira, GitHub, GitLab

# Links

- [LinkedIn](https://linkedin.com/in/morozovda-sa)
- [GitHub](https://github.com/flatura)


Content available in Russian. [Русская версия](/ru/).