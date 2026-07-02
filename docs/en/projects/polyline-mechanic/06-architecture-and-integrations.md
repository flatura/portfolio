# Architecture and Integrations

## Architecture

## Architectural Approach

The utility was implemented as a layered monolithic web application.

The architecture included:

* server-side page rendering;
* MVC structure;
* business logic layer;
* repository layer;
* jQuery-based interactions for partial updates without full page reloads.

## Integration Flows

## Polyline generation via routing service

The tool generates polylines through a routing service, producing route-based geometry for railway graph segments.

## Polyline repair via route recalculation

Existing polylines can be repaired through route recalculation when geometry is incorrect or incomplete.

## Asynchronous polyline loading and update flows

The application supports asynchronous polyline retrieval and update flows, including polyline caching, enabling partial UI updates without full page reloads.
