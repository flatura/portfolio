# Decisions, Trade-offs, and Risks

## Key Decisions

## Dual geographic and logical views

The platform combines map-based geographic visualization with a non-geographic logical graph layout, allowing the same topology to be inspected from both infrastructure and relationship perspectives.

## Connector-oriented data access

Instead of hardcoding a single database structure, GraphMechanic separates the visual graph model from the source database schema via a connector layer.

## Multi-layer visualization

Multiple graph layers can be displayed on the same map, each with its own visibility, styling rules, and data source.

## Attribute-driven style engine

Visual appearance of nodes and edges is configured dynamically based on object attributes, turning the graph into an operational visual model.

## Domain-generalized graph model

The platform is not limited to railway data; generalized graph concepts allow adaptation to different domains without rewriting the core application.

## Trade-offs

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

The strongest value is not "visualize a graph", but "make operational graph data inspectable, editable, and understandable".

See also [Architecture Decision Records](adr/index.md).
