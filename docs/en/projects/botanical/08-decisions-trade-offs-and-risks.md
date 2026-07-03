# Decisions, Trade-offs, and Risks

## Key Decisions

### Decoupled frontend and backend

The system uses a separate Angular frontend and Spring Boot backend API. This reduces coupling, allows independent evolution of UI and backend logic, and creates a foundation for future client channels.

### Root-unit soft multi-tenancy

Each tenant is represented by a root organizational unit. Tenant-scoped entities carry `root_unit_id`, and access is constrained through repositories, specifications, services, and API-level checks.

### Context-aware authorization

Permissions depend not only on the user's global role, but also on the current organization and selected organizational context.

This fits B2B scenarios where the same user may have different permissions in different organizations or departments.

### PostGIS as part of the domain model

Plant locations, garden areas, greenhouses, beds, and polygons are modeled as spatial data, not as a secondary map overlay.

### Hybrid current state and history model

The system separates current operational state from data related to change history and audit trail. This allows efficient work with current records while preserving traceability of important changes.

### Controlled public data exposure

Public pages, plant cards, lists, photos, and map data are published through separate public endpoints and DTOs.

Visibility rules prevent accidental exposure of internal tenant data.

## Architectural Trade-offs

### 1. Soft multi-tenancy instead of full isolation

#### Context

The system is designed for many organizations (multi-tenant). At an early stage the product needs low operational complexity, high development speed, and meeting functional requirements (taxonomic layer and ability to develop network scenarios between organizations).

#### Decision

Logical multi-tenancy through a `root_unit_id` attribute is used for data isolation. The root organizational unit is the organization boundary; all entities in the tree reference this root unit.

#### Rejected alternative

`database-per-tenant` or `schema-per-tenant`.

#### Rationale

* lower infrastructure complexity at an early stage
* allows absorbing organizations or spinning off departments with minimal entity migration

#### Trade-offs

* Data isolation is logical, not physical; any tenant filtering error in any API can break tenant isolation.
* Harder to back up, restore, export, and physically delete data for a single organization (right to be forgotten).
* Harder to dedicate a large client to separate infrastructure.
* Sharding and regional data separation will require additional design.

#### Compensating measures

* All entities belonging to an organization carry `root_unit_id`.
* Access is constrained at multiple levels: repository queries, JPA specifications, business-logic checks, controller method authorization.
* Central authorization is extracted into `AccessControlService`.
* Public APIs return only public DTOs and do not expose internal fields.
* Integration tests for cross-tenant access denial are written for critical scenarios.
* For 152-FZ compliance a separate availability zone for RF users is provisioned (two zones so far). Replication of public data between availability zones is planned, accounting for possible disconnection of the RF network segment from the global internet.

#### Review trigger

* enterprise clients requiring physical isolation
* data volume growth to noisy-neighbor levels
* need for regional data storage or legal requirement to physically separate organization data

---

### 2. Modular monolith instead of microservices

#### Context

The product has a broad domain model: plants, taxonomy, cultivars, lists, places, import, public pages, users, roles, media, and inter-organization exchange. The team is small and the domain model is still actively refined. It is also unclear how much load will differ across entities.

#### Decision

The backend is implemented as a modular monolith on Spring Boot: a single artifact with separation by domain areas through controllers, services, repositories, and DTOs.

#### Rejected alternative

A set of microservices: taxonomy service, collections service (+ import), media service, authorization and identity service, GIS service, public resources service.

#### Why this makes sense now

A monolith reduces distributed-system overhead: no network contracts between services, no distributed transactions, no service discovery infrastructure, no complex observability or inter-service failure orchestration. This speeds delivery and keeps the domain model cohesive while the product has not yet passed the first pilots.

#### Trade-offs

* Individual domain modules cannot be scaled independently.
* A failure in one module can affect the entire backend.
* Over time, implicit dependencies between domain areas may emerge.
* Import, media, and GIS may have different load profiles but still live in one application.

#### Compensating measures

* Strict package separation by domain areas. Service layer as the boundary for business logic, DTOs as the API boundary. This lowers the cost of extracting a bounded context into its own service.
* Asynchronous execution of heavy imports to avoid blocking a thread and hitting timeouts.

#### Review trigger

Service extraction makes sense when a specific module gets independent load scale, a dedicated owning team, a separate release cadence, or separate resilience requirements. First extraction candidates: import pipeline, media processing/storage gateway, public map/search read model.

---

### 3. Monorepo for backend and frontend instead of separate repositories

#### Context

The project is developed by a small team where one developer owns architecture, backend, frontend, deployment, and integration. For these conditions, speed of coordinated changes matters more than organizational independence of teams.

#### Decision

Backend and frontend are stored in one repository.

#### Rejected alternative

Separate repositories for backend, frontend, infrastructure, and documentation.

#### Why this makes sense now

A monorepo allows atomic API and UI changes, easier maintenance of full architectural context, faster full-stack refactoring and LLM code generation. The result is more stable because the model sees the connected product picture.

#### Trade-offs

* Responsibility boundaries may blur as the team grows.
* Harder to restrict access to parts of the codebase.
* Higher risk of broad changes without understanding blast radius.

#### Compensating measures

* Separate frontend/backend folders and independent build and run commands.
* Integration tests for frontend/backend interaction.

#### Review trigger

Separate repos become justified when independent teams with different release cycles appear, different code access policies, or need to publish parts of the system independently.

---

### 4. Docker Compose instead of cloud native

#### Context

At an early stage the system must deploy quickly on a VPS, demonstrate the product, run pilots, and keep infrastructure costs low.

#### Decision

Backend, frontend, PostgreSQL/PostGIS, and MinIO run in a single Docker Compose environment.

#### Rejected alternative

Full cloud-native infrastructure with dedicated DB and object storage capacity, container autoscaling, monitoring, and multi-zone deployment.

#### Why this makes sense now

Docker Compose gives fast cold start, reproducible environment, low cost, and a simple operational model. For MVP, demo stand, and early pilot this is better than premature cloud-native complexity.

#### Trade-offs

* A single VPS is a single point of failure.
* DB, object storage, and services compete for resources.
* Scaling is mostly vertical.
* No full high-availability model, no peak load handling. Cannot be considered production architecture.
* Backup, restore, and monitoring become critical operational tasks.

#### Compensating measures

* Services remain stateless.
* Configuration must be env-based.
* DB and object storage data live on persistent volumes with regular backups.
* Reverse proxy / TLS / rate limits are moved to the infrastructure layer.
* Target migration path must be described in advance: separate PostgreSQL/PostGIS instances, S3-compatible storage, horizontal scaling of service containers.

#### Review trigger

Transition is needed when paying clients appear, SLA expectations, growth in photo/import volume, high-availability requirements, regular VPS downtime, or need for regional data placement.

... Only part of the trade-offs is published in the portfolio.

See also [Architecture Decision Records](adr/index.md).
