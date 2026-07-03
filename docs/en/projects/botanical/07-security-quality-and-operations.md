# Security, Quality, and Operations

## Security and Access Model

### Multi-tenancy and Access Control

The platform uses a soft multi-tenancy model based on a root organization unit pattern.

A user can belong to multiple organizations and have different roles depending on the current organization context. Access checks are applied at service, repository, API, and UI levels.

### Public Showcase

Organizations can publish selected data through public pages, public plant cards, public lists, QR-label targets, and a global map.

The public layer uses separate DTOs and visibility rules to avoid exposing internal fields and tenant data.

### Dual RBAC Contour

The system has a single User entity and two role-based access models: organizational roles and platform roles. One user may lead several organizations and also be a platform moderator; another user acts as a support engineer and therefore needs limited access to any tenant and object; a third user is a stakeholder with access only to dashboard modules. All three users authenticate through a unified authorization and authentication flow. Mechanism details are not disclosed.

## Non-Functional Requirements

### Key Quality Attributes

| Attribute | Scenario | Approach |
|---|---|---|
| Security | A user from organization A must not access organization B data | tenant-scoped queries, RBAC, public DTO, integration tests |
| Reliability | A stuck import must not block the system | background jobs, stale detection, retry/manual restart |
| Maintainability | The domain model changes actively at the MVP stage | modular monolith, package boundaries, DTO/service layers |
| Performance | Taxonomy reference search must remain acceptable as the catalog grows | indexes, normalized names, pagination, fuzzy matching strategy |
| Operability | A VPS failure must not lead to complete data loss | backups, restore plan, migration path |

## Failure Modes

| Risk | Impact | Mitigation |
| ----------------------- | --------------------------- | ------------------------------------------- |
| tenant filtering error | data leakage | tests, AccessControlService, scoped queries |
| VPS failure | service unavailability | backup, restore plan, migration path |
| MinIO volume loss | loss of photos/imports | object storage backup |
| stuck import job | import blocked | job lifecycle, stale detection |
| public DTO leakage | exposure of internal data | separate DTOs, visibility rules |

## Sizing and Cost Notes

### Primary load drivers

- number of organizations;
- number of plant instances;
- number of photos per plant;
- Excel import size;
- Smart Import frequency;
- public traffic volume for maps, QR pages, and images;
- taxonomy reference volume.

### Primary cost drivers

- VPS / compute;
- PostgreSQL/PostGIS storage;
- object storage for photos and imports;
- backups;
- LLM calls for Smart Import;
- public page and image traffic;
- monitoring and log storage.

### Scaling tiers

See [Roadmap and Demonstration](09-roadmap-and-demonstration.md).
