# MyLovelyGarden (MLG): SaaS Platform for Botanical Organizations

**Status:** MVP / pilot preparation  
**Role:** Co-founder, System Designer, Backend-oriented Engineer  
**Platform:** Web

## About the Project

**MyLovelyGarden** is a practical SaaS platform designed for botanical gardens, nurseries, plant breeders, and private plant collections.

The project addresses a common domain problem: plant records, observations, provenance, locations, and related operations are often managed through fragmented spreadsheets, local databases, or outdated specialized software. This makes search, cross-organization data exchange, consistent reference data management, and work with geo-linked objects unnecessarily difficult.

The goal of the project is to build a unified system for managing botanical collections and related workflows with emphasis on:
- a centralized taxonomy reference layer;
- role-based access with organizational context awareness;
- support for spatial data and mapping workflows;
- traceability of plant instance lifecycle.

---

## My Scope of Contribution

- Elaborating the domain model and key system scenarios
- Designing the backend layer, APIs, and data structures
- Preparing technical documentation and architecture artifacts
- Making system-level decisions around access model, data storage, and component boundaries
- Hands-on backend implementation
- Coordinating the overall technical structure of the project together with a domain expert

---

## Development Approach

The project is developed using an AI-assisted workflow. I define requirements, system decisions, data models, and API contracts, while part of the routine implementation is delegated to LLM-based tools in a controlled manner.

This approach is used to accelerate prototyping and technical iteration, but it does not replace manual work on architecture decisions, domain modeling, and key project constraints.

---

## Key System Decisions

### 1. Separated frontend and backend
The project is evolving as a decoupled web architecture with a dedicated frontend client and a backend API. This reduces coupling, simplifies UI evolution, and creates a foundation for future expansion of client channels.

### 2. Soft multi-tenancy
A soft multi-tenancy model was chosen for data isolation within a shared storage model. This helps reduce total cost of ownership at the early stage, simplifies maintenance, and preserves the ability to support shared analytics and a centralized reference layer.

### 3. Context-aware access model
The access model takes into account not only the user’s global system role, but also the organization and work context currently in use. This better fits B2B scenarios where the same user may have different permissions across different organizational units.

### 4. Spatial data support
The system is designed with geo-linked entities in mind: plant locations, plots, polygons, greenhouses, and other spatial objects. The spatial layer is treated as a core part of the domain model rather than a secondary visualization add-on.

### 5. Hybrid current-state and history model
A hybrid approach is used for plant lifecycle tracking: current operational state is stored separately from event and change history. This supports both efficient access to current data and traceability of actions, movements, and state changes.

### 6. "Circles of trust" data access model
System has a well granulated plant lists access control model. Admin has an ability to grant access to whole world (Public), to Verified tenant users or to single user. 

---

## Infrastructure Approach

At the MVP stage, the project is focused on practical deployment with controlled operational complexity. The deployment architecture is designed to avoid unnecessary early-stage overhead while preserving a path toward a more mature cloud environment later.

The current approach includes:
- containerized services;
- separate build pipelines for client and server parts;
- external object storage for media data;
- basic CI/CD automation;
- architectural and technological readiness for future scaling.

---

## Why This Project Matters for My Professional Track

For me, MyLovelyGarden is not just a pet project, but a practical environment for growing toward system design and solution architecture. It combines:
- domain design;
- data modeling;
- API and integration design;
- multi-tenant access model design;
- "circles of trust" data access model design;
- architecture documentation;
- hands-on backend implementation.

## C4 Diagrams
<figure markdown>
![C4 Diagrams](/portfolio/assets/MLG_Context+Container_Diagram_en_safe.drawio.png)
<figcaption>C4 Context + Container diagrams</figcaption>
</figure>