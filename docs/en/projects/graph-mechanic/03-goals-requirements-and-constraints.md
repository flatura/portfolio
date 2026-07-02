# Goals, Requirements, and Constraints

## Goals and Non-Goals

## Requirements

## Key Capabilities

### 1. Domain-Generalized Graph Model

GraphMechanic is not limited to railway data.

The platform supports generalized graph concepts:

- nodes;
- edges;
- edge geometry;
- node attributes;
- edge attributes;
- layers;
- statuses;
- domain-specific metadata;
- external identifiers;
- topology validation rules.

This makes it possible to adapt the tool to different domains without rewriting the core application.

### 2. Configurable Database Connectors

The platform supports a connector-oriented approach to data access.

Instead of hardcoding a single database structure, GraphMechanic separates the visual graph model from the source database schema.

The connector layer is responsible for:

- reading nodes;
- reading edges;
- reading edge geometry;
- mapping database fields to graph attributes;
- applying filters;
- writing back approved changes;
- supporting different source schemas.

Initial target sources:

- PostgreSQL / PostGIS;
- relational databases with graph-like tables;
- exported CSV / JSON datasets;
- future graph database connectors.

### 3. Multi-Layer Graph Display

GraphMechanic can display multiple graph layers on the same map.

Examples:

- physical infrastructure layer;
- logical routing layer;
- service availability layer;
- planned changes layer;
- error / anomaly layer;
- historical snapshot layer.

Each layer can have its own visibility, styling rules, and data source.

This allows users to compare different interpretations of the same network and detect inconsistencies between physical, logical, and operational views.

### 4. Node and Edge Style Parameterization

The appearance of nodes and edges can be configured dynamically.

Visual parameters may depend on object attributes:

- node color by status;
- node size by importance or load;
- edge thickness by capacity or traffic;
- edge color by availability;
- dashed lines for planned or inactive segments;
- icons for different object types;
- labels based on selected fields.

This makes the graph useful not only as geometry, but as an operational visual model.

### 5. Dynamic Parameters and Live State Observation

GraphMechanic supports the idea of observing graph state changes over time.

The same topology can be enriched with dynamic data:

- availability;
- load;
- error state;
- latency;
- processing status;
- last update time;
- operational metrics.

This turns a static graph into a lightweight operational console.

The goal is not to replace full observability platforms, but to show system state in relation to domain topology.

### 6. Logical Graph View

In addition to map-based visualization, GraphMechanic supports a non-geographic graph layout.

This mode places all nodes on a single screen using a force-directed or layout-based graph view, similar in spirit to Obsidian-style graph visualization.

This is useful when geography hides the logical structure or when the graph is not geographic at all.

Use cases:

- dependency maps;
- logical topology;
- infrastructure relationships;
- domain entity graphs;
- process graphs;
- knowledge graphs;
- data lineage-like views.

### 7. Visual Editing

The platform extends the original PolylineMechanic functionality:

- node editing;
- edge editing;
- polyline creation;
- polyline repair;
- route-based geometry generation;
- attribute editing;
- visual validation;
- controlled save / export flow.

The editing model is intended to reduce direct database manipulation and give domain users a safer visual workflow.

## Example Use Cases

- Validate railway graph data before loading it into an enterprise GIS platform.
- Compare physical and logical network layers.
- Detect disconnected nodes or broken routes.
- Display operational state over infrastructure topology.
- Edit graph attributes without direct database access.
- Build a visual console for domain-specific network data.
- Switch between map-based and logical graph representation.
- Investigate inconsistencies between planned and actual topology.

## Constraints
