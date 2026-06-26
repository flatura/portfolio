# Integration Flows

## Database connector read/write flows

The connector layer reads nodes, edges, and edge geometry from external sources, maps database fields to graph attributes, applies filters, and writes back approved changes.

Initial target sources include PostgreSQL / PostGIS, relational databases with graph-like tables, and exported CSV / JSON datasets.

## Route-based geometry generation

Visual editing extends PolylineMechanic functionality with route-based geometry generation for polyline creation and repair.

## Controlled save and export flow

Edits follow a controlled save / export workflow intended to reduce direct database manipulation and give domain users a safer visual editing path.
