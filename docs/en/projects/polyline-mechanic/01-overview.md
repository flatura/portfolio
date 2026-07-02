# Overview

A local web utility for creating, editing, and repairing railway track polylines used in railway graph data preparation.

The project emerged from a practical data quality problem: railway infrastructure objects had to be connected with correct geometry, but manual preparation of polyline data was slow, error-prone, and difficult to validate without a visual tool.

The utility provided a lightweight internal interface for working with railway graph geometry: editing nodes, creating polylines, generating route-based geometry, and repairing incorrect or incomplete track segments.

## Technology Stack

* Java / Spring Boot
* Server-side rendering
* MVC architecture
* Repository layer
* JavaScript / jQuery
* Map-based UI
* Routing service integration
* Polyline caching
* Asynchronous data loading