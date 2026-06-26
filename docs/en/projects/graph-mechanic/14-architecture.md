# Architecture

GraphMechanic is designed as a modular web application.

Core components:

- **Web UI** - graph visualization, map view, logical graph view, editing tools;
- **Graph Model Layer** - normalized internal representation of nodes, edges, geometry, attributes, and layers;
- **Connector Layer** - adapters to external databases and data sources;
- **Style Engine** - configurable mapping between object attributes and visual appearance;
- **Validation Engine** - topology checks and domain-specific consistency rules;
- **State Update Layer** - dynamic updates for live or near-real-time graph state;
- **Persistence Layer** - storage of configuration, layouts, user settings, and audit data.
