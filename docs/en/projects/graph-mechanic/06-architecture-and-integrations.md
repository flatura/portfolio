# Architecture and Integrations

## Architecture

GraphMechanic is designed as a modular web application.

Core components:

- **Web UI** - graph visualization, map view, logical graph view, editing tools;
- **Graph Model Layer** - normalized internal representation of nodes, edges, geometry, attributes, and layers;
- **Connector Layer** - adapters to external databases and data sources;
- **Style Engine** - configurable mapping between object attributes and visual appearance;
- **Validation Engine** - topology checks and domain-specific consistency rules;
- **State Update Layer** - dynamic updates for live or near-real-time graph state;
- **Persistence Layer** - storage of configuration, layouts, user settings, and audit data.

## Integration Flows

## Database connector read/write flows

The connector layer reads nodes, edges, and edge geometry from external sources, maps database fields to graph attributes, applies filters, and writes back approved changes.

Initial target sources include PostgreSQL / PostGIS, relational databases with graph-like tables, and exported CSV / JSON datasets.

## Route-based geometry generation

Visual editing extends PolylineMechanic functionality with route-based geometry generation for polyline creation and repair.

## Controlled save and export flow

Edits follow a controlled save / export workflow intended to reduce direct database manipulation and give domain users a safer visual editing path.
