# Decisions, Trade-offs, and Risks

## Key Decisions

### Key Architecture Decisions

#### Decoupled Frontend and Backend

The system uses a separated Angular frontend and Spring Boot backend API. This keeps UI evolution independent from backend domain logic and supports future client channels.

#### Root-unit Soft Multi-tenancy

Each tenant is represented by a root organization unit. Tenant-scoped entities carry a `root_unit_id`, and access is constrained through repositories, specifications, services, and API-level checks.

#### Context-aware Authorization

Permissions depend not only on global user roles, but also on the currently selected organization and unit context.

This fits B2B scenarios where the same user may have different permissions in different organizations or departments.

#### PostGIS as a Core Domain Layer

Plant locations, garden places, greenhouses, beds, and polygons are modeled as spatial data, not as decorative map overlays.

#### Hybrid Current State and History Model

The system separates current operational state from history/audit-related data. This keeps day-to-day queries efficient while preserving traceability of important changes.

#### Controlled Public Exposure

Public pages, plant cards, lists, photos, and map data are exposed through dedicated public endpoints and DTOs. Visibility rules prevent accidental exposure of internal tenant data.

## Trade-offs

### Root-unit soft multi-tenancy vs database-per-tenant

This keeps early-stage operational complexity lower than database-per-tenant while preserving isolation and shared reference data.

See also [Architecture Decision Records](adr/index.md).
