# Архитектура и интеграции
## Архитектурная концепция

```text
OpenWebUI
  → agent-lab / LangGraph
  → Playbook Router
  → selected playbook
  → Tool Registry
  → Tool Gateway / tool-server
  → PostgreSQL / Qdrant / MinIO
  → evidence
  → structured executive answer
```

## Context diagram

```mermaid
flowchart TB
    Executive[Executive / C-level]
    DomainOwner[Domain Owner]
    Admin[Platform Admin]
    Platform[Executive Decision Intelligence Platform]
    ERP[Finance / Sales / ERP data]
    Delivery[Delivery Tracker]
    ITSM[ITSM / Service Desk]
    PMO[PMO / Roadmap]
    Docs[Documents / Knowledge Base]
    LLM[OpenAI-compatible LLM]

    Executive --> Platform
    DomainOwner --> Platform
    Admin --> Platform
    Platform --> ERP
    Platform --> Delivery
    Platform --> ITSM
    Platform --> PMO
    Platform --> Docs
    Platform --> LLM
```

## Поток одного diagnostic run

```mermaid
sequenceDiagram
    autonumber
    participant U as User
    participant UI as OpenWebUI
    participant AG as agent-lab
    participant PB as Playbook Router
    participant LLM as LLM
    participant TG as tool-server / Tool Gateway
    participant PG as PostgreSQL
    participant QD as Qdrant
    participant MN as MinIO

    U->>UI: Управленческий вопрос
    UI->>AG: POST /agent/check-hypothesis
    AG->>PB: classify intent
    PB-->>AG: selected playbook + allowed tools
    AG->>LLM: plan next diagnostic step
    LLM-->>AG: call metric_gross_margin
    AG->>TG: controlled tool call
    TG->>PG: execute named query
    PG-->>TG: metric result
    TG-->>AG: structured evidence
    AG->>LLM: evaluate evidence
    LLM-->>AG: need document evidence
    AG->>TG: rag_search
    TG->>QD: vector search with filters
    QD-->>TG: chunks + scores
    TG->>MN: resolve object refs
    MN-->>TG: source metadata
    TG-->>AG: document evidence
    AG->>LLM: synthesize answer with limitations
    AG-->>UI: final answer + run details
    UI-->>U: executive brief + evidence trail
```

## Интеграционные принципы

1. LLM не исполняет SQL.
2. LLM не читает документы напрямую.
3. LLM не получает полный список всех tools без ограничений.
4. Backend / tool-server валидирует входные параметры.
5. Tools возвращают structured JSON, metadata, warnings и status.
6. Evidence связывается с tool call, документом, period/entity и claim.
7. Debug visibility доступна через run details, но не должна раскрывать приватные chain-of-thought рассуждения.
