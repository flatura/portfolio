# Security and Access Model

## Multi-tenancy and Access Control

The platform uses a soft multi-tenancy model based on a root organization unit pattern.

Users can belong to multiple organizations and have different roles depending on the current organization context. Access checks are enforced across service, repository, API, and UI layers.

## Public Showcase

Organizations can expose selected data through public pages, public plant pages, public lists, QR-label targets, and a global map.

The public layer uses separate DTOs and visibility rules to avoid leaking internal fields.
