**Status:** Pilot / pre-production operation for internal B2E use; pre-sale architecture for B2B productization  
**Role:** Systems Analyst / Solution Designer  
**Domain:** Enterprise GIS, logistics, railway infrastructure  
**NDA:** Detailed architecture, data models, and source code are confidential

## Summary

Enterprise GIS platform for the logistics sector.

The initiative started as an internal B2E system for visualizing reports from corporate tabular master systems in a GIS interface, with spatial binding to railway infrastructure and the track-segment graph.

The same engineering foundation was later reused as a basis for a more universal B2B-oriented BI/GIS product concept for logistics companies and freight carriers.

## Product Context

The internal product addressed a practical enterprise problem: business users worked with complex operational reports, but the data was difficult to interpret without spatial context.

The system allowed users to visualize enterprise data on a map, link business metrics to railway infrastructure, work with map layers, and analyze objects in relation to the railway graph.

The external B2B direction reused the same infrastructure and architectural base, but required a more configurable model: client-specific layers, dynamic business metrics, on-premise deployment, and stricter product-level documentation.

## Architecture and Engineering Challenges

### Isolated GIS Infrastructure

Corporate security requirements did not allow reliance on external map providers or public routing APIs.

**Solution:** Researched and prepared an isolated GIS infrastructure approach based on a local tile server and routing components. Configured and deployed Mapnik-based tile server components and an OSRM/GIS routing service for use inside a closed enterprise contour.

The proposed approach became reusable as a platform-level GIS capability for other internal teams.

### Configurable GIS Data Model

The transition from an internal ad-hoc system to a reusable B2B product required a more flexible model for layers, geometry, and business metrics.

**Solution:** Designed a relational/PostGIS-based data model that allowed configurable GIS layers and binding of GeoJSON geometry to business attributes and indicators.

This made it possible to describe map layers not as hardcoded screens, but as configurable business objects.

### Railway Infrastructure Binding

The source enterprise systems did not provide a single ready-to-use GIS graph for all required railway objects.

**Solution:** Designed logic for linking fragmented geospatial data to railway infrastructure objects and the track-segment graph. Participated in the design of visual editing tools for infrastructure data based on OpenLayers and backend services.

### Reverse Engineering and Architecture Formalization

Part of the system relied on existing legacy components and undocumented implementation details.

**Solution:** Reconstructed and formalized the architecture of existing components. Prepared conceptual architecture artifacts, including C4 diagrams, ERD, DFD, and integration descriptions, to align business stakeholders and the development team.

## Role and Contribution

My responsibilities included:

- eliciting and formalizing business and functional requirements;
- translating business needs into implementation tasks for developers;
- preparing project documentation and architecture artifacts;
- defining non-functional requirements for performance, security, deployment, and operation in a closed enterprise contour;
- designing API contracts and target architecture for the B2B product direction;
- preparing technical rationale and ADR-style notes for technology choices during the pre-sale phase;
- configuring and deploying ad-hoc infrastructure components, including tile server and GIS routing components;
- designing geospatial data processing logic and infrastructure editing scenarios;
- supporting pre-production readiness activities.

## Technology Stack

Used across related components:

- **Backend:** Python, FastAPI, Java, Spring Boot
- **Data & GIS:** PostgreSQL, PostGIS, OracleDB, GeoJSON, OSRM, Mapnik
- **Frontend:** Angular, OpenLayers
- **Infrastructure:** Docker, Traefik, on-premise deployment in a closed enterprise contour

## Professional Relevance

This project demonstrates experience in enterprise GIS systems, internal product development, B2B productization, geospatial data modeling, infrastructure isolation, on-premise deployment constraints, and communication between business stakeholders, architects, and development teams.

It is especially relevant to roles involving systems analysis, solution design, enterprise integration, GIS-enabled products, and MVP-to-product transition.