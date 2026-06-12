# GraphMechanic - Visual Graph Operations Platform

**Type:** Graph visualization / GIS-aware graph editing / internal tooling platform  
**Role:** concept author, system designer, prototype engineer  
**Status:** concept prototype / paused project  
**Origin:** evolved from PolylineMechanic railway graph tooling

## Overview

GraphMechanic is a visual platform for working with domain-specific graph data: infrastructure networks, transport graphs, GIS-linked objects, logical dependencies, and operational topology.

The project evolved from PolylineMechanic, an internal tool for editing railway graph polylines. The original problem was narrow: prepare and repair railway track geometry. GraphMechanic generalizes this idea into a broader tool for viewing, editing, comparing, and monitoring graph-based systems.

The core idea is to combine two complementary views of a graph:

- **geographic view** - nodes and edges placed on a map;
- **logical view** - all nodes arranged as a graph layout, independent from geography.

This allows the same graph to be inspected both as real-world infrastructure and as a logical network of relationships.

## Problem

Many organizations store graph-like data in databases, GIS systems, internal tools, or operational platforms, but lack a convenient interface for visual inspection and controlled editing.

Typical problems:

- graph data exists in a database, but is hard to inspect visually;
- geographically linked objects are difficult to validate only through tables;
- node and edge attributes affect behavior, but are not visible in the UI;
- multiple graph layers need to be compared side by side;
- domain teams need visual diagnostics without direct database access;
- real-time state changes are hard to observe in relation to graph topology;
- existing tools are either too generic, too GIS-heavy, too database-specific, or too complex for lightweight internal use.

## Product Concept

GraphMechanic provides a configurable visual layer over graph data.

It allows users to connect to graph-like datasets, visualize them on a map or as a logical graph, configure visual styles, inspect node and edge attributes, and observe changes over time.

The platform is intended for teams that work with infrastructure, transport, logistics, utility networks, telecom topology, GIS-linked assets, or custom operational graphs.

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

## Target Users

- GIS analysts;
- system analysts working with graph-like domains;
- infrastructure data engineers;
- transport and logistics analysts;
- telecom / utility network teams;
- internal tooling teams;
- teams maintaining custom operational graph data.

## Example Use Cases

- Validate railway graph data before loading it into an enterprise GIS platform.
- Compare physical and logical network layers.
- Detect disconnected nodes or broken routes.
- Display operational state over infrastructure topology.
- Edit graph attributes without direct database access.
- Build a visual console for domain-specific network data.
- Switch between map-based and logical graph representation.
- Investigate inconsistencies between planned and actual topology.

## Competitive Context

GraphMechanic is positioned between several existing categories:

- GIS platforms and utility network tools;
- graph database visualization tools;
- network topology and monitoring tools;
- open-source graph visualization libraries;
- custom internal admin panels.

Unlike heavy GIS platforms, GraphMechanic focuses on configurable graph operations and lightweight domain adaptation.

Unlike generic graph visualization tools, it treats geography, geometry, layers, database connectors, and editing workflows as first-class concerns.

Unlike monitoring systems, it does not start from infrastructure metrics. It starts from a domain graph and adds state observation on top.

## Differentiation

GraphMechanic is built around a specific combination:

- graph data;
- geographic and non-geographic views;
- editable topology;
- configurable database connectors;
- multi-layer visualization;
- style rules based on attributes;
- dynamic state observation;
- domain-specific validation.

The strongest value is not “visualize a graph”, but “make operational graph data inspectable, editable, and understandable”.

## Current Status

The project is currently paused.

Some concepts and earlier implementation experience come from PolylineMechanic, a railway graph polyline editing utility. GraphMechanic generalizes that work into a broader product direction.

The current version should be treated as a concept-stage project and architecture direction rather than a finished SaaS product.

## What This Project Demonstrates

GraphMechanic demonstrates a product and architecture direction built from real internal tooling experience.

It shows:

- ability to generalize a narrow internal tool into a broader product concept;
- understanding of graph-based domains and GIS-linked data;
- interest in visual tools for system understanding and data quality;
- ability to connect backend data structures with interactive visual workflows;
- movement from one-off internal tools toward reusable product architecture.

## Full Documentation

- Documentation is in progress.