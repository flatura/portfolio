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

The project is designed as a practical MVP:

* separated frontend and backend;
* stateless services in Docker containers;
* PostgreSQL/PostGIS database;
* MinIO/S3-compatible storage for media and import files;
* schema migrations via Flyway;
* launch profiles based on environment configuration;
* basic CI/CD (Docker image build via GitHub Actions).

## Failure Modes

| Risk | Impact | Mitigation |
| ----------------------- | --------------------------- | ------------------------------------------- |
| tenant filtering error | data leakage | tests, AccessControlService, scoped queries |
| VPS failure | service unavailability | backup, restore plan, migration path |
| MinIO volume loss | loss of photos/imports | object storage backup |
| stuck import job | import blocked | job lifecycle, stale detection |
| public DTO leakage | exposure of internal data | separate DTOs, visibility rules |

## Sizing and Cost Notes
