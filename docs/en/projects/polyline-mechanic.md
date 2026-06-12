# Railway Graph Polyline Editing Utility

**Type:** Internal tooling / GIS data preparation / railway graph editing
**Role:** initiator, concept author, developer
**Status:** historical internal project / evolved into GraphMechanic concept

## Overview

A local web utility for creating, editing, and repairing railway track polylines used in railway graph data preparation.

The project emerged from a practical data quality problem: railway infrastructure objects had to be connected with correct geometry, but manual preparation of polyline data was slow, error-prone, and difficult to validate without a visual tool.

The utility provided a lightweight internal interface for working with railway graph geometry: editing nodes, creating polylines, generating route-based geometry, and repairing incorrect or incomplete track segments.

## Context

The project was created in the context of an enterprise GIS initiative, where railway infrastructure data had to be prepared for map visualization, routing, and further analytical use.

Raw graph data and infrastructure objects required manual cleanup and alignment. Without a dedicated tool, this work would have required direct data manipulation, repeated checks, and significant coordination between analysts and developers.

The goal was to create a small practical tool that allowed visual editing and faster preparation of railway graph data.

## Problem

The team needed to work with railway track geometry in a more controlled and visual way.

Typical issues included:

* missing or incorrect polyline geometry;
* disconnected graph nodes;
* railway segments requiring manual correction;
* difficulty validating geometry through raw data alone;
* slow preparation of infrastructure objects for further use;
* repeated developer involvement for data fixes that could be handled visually.

## Solution

I designed and implemented a local web utility for railway graph polyline editing.

The tool supported:

* viewing railway graph objects on a map;
* editing graph nodes;
* creating new polylines;
* generating polylines through a routing service;
* repairing existing polylines through route recalculation;
* applying changes without full page reloads;
* preparing graph data for further use in GIS-related systems.

## Role and Contribution

I acted as the initiator, concept author, and developer.

My contribution included:

* identifying the need for a dedicated visual editing tool;
* defining the main user scenarios for railway graph cleanup;
* designing the application structure;
* implementing the backend and server-side page generation;
* implementing interactive UI behavior with JavaScript and jQuery;
* adding asynchronous polyline loading and update flows;
* supporting practical data preparation work for railway infrastructure objects.

## Architectural Approach

The utility was implemented as a layered monolithic web application.

The architecture included:

* server-side page rendering;
* MVC structure;
* business logic layer;
* repository layer;
* polyline caching;
* asynchronous polyline retrieval;
* jQuery-based interactions for partial updates without full page reloads.

This approach was intentionally pragmatic: the tool was designed for local/internal use, fast iteration, and practical data preparation rather than long-term productization.

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

## UI Screenshots

<figure markdown>
![GraphMechanic: UI](../../assets/graphmechanic/ui/v1/ui_9f3c1a4.webp)
<figcaption>User interface</figcaption>
</figure>

<figure markdown>
![GraphMechanic: node editing](../../assets/graphmechanic/ui/v1/edit_node_9f3c1a4.webp)
<figcaption>Node editing</figcaption>
</figure>

<figure markdown>
![GraphMechanic: polyline creation](../../assets/graphmechanic/ui/v1/create_polyline_9f3c1a4.webp)
<figcaption>Polyline creation</figcaption>
</figure>

<figure markdown>
![GraphMechanic: polyline generation via routing service](../../assets/graphmechanic/ui/v1/edit_polyline_9f3c1a4.webp)
<figcaption>Polyline generation through a routing service</figcaption>
</figure>

<figure markdown>
![GraphMechanic: polyline repair via routing service](../../assets/graphmechanic/ui/v1/fix_polyline_9f3c1a4.webp)
<figcaption>Polyline repair through a routing service</figcaption>
</figure>

## What This Project Demonstrates

This project demonstrates my early transition from requirements and data preparation work toward hands-on internal tooling development.

It shows the ability to:

* identify a repetitive data preparation bottleneck;
* convert a manual GIS/data-cleanup task into a visual tool;
* design a pragmatic internal application for a narrow operational problem;
* combine backend logic, map UI, routing, caching, and asynchronous interactions;
* create tools that reduce manual work and improve data quality.

The project later evolved conceptually into GraphMechanic, a broader idea for visual graph editing and GIS-related data tooling.

## Full Documentation

* Documentation is in progress.
* The project direction continues in GraphMechanic: https://github.com/flatura/graphmechanic_docs
