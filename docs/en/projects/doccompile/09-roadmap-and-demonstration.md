# Roadmap and Demonstration

## Implemented

The working foundation, as described in product materials (confirm against the product repository before treating any line as a hard inventory):

* Markdown / GFM renderer;
* Mermaid and architecture icons;
* professional themes, images/assets, print layout, PDF, pagination hardening;
* local-first rendering in a client-side SPA;
* AWS delivery (CloudFront, private S3 / OAC);
* Terraform and GitHub Actions with OIDC;
* Cognito authentication and admin control plane with USER / ADMIN / SUPER_ADMIN;
* runtime configuration and versioned prompts with publish / rollback;
* AI transformations for at least ADR, requirements (FR/NFR, business rules / constraints), and Resume / CV;
* credits / cost controls and a Paddle billing contour;
* transformation history and admin observability.

Not claimed as implemented: Step Functions Harness, ECS Fargate workers, Evidence / Canonical Fact Model, Situations, Patch Compile, GitHub App / CLI as a shipped workflow.

## Current / next focus

Epoch numbers are provisional. Prefer the product repository if it has a newer roadmap.

| Epoch | Focus | Status |
|---|---|---|
| - | Renderer, SaaS contour, first AI transformations, credits / Paddle | Implemented |
| E22 | Product and Compiler quality telemetry; Compiler publication lifecycle (PUBLIC / INTERNAL / DISABLED) | Next |
| E23 | Universal Transformation Harness; Artifact Contract | Planned |
| E24 | Evidence / Canonical Fact Model | Planned |
| E25 | Compiler specification; custom output templates | Planned |
| E26 | Reference-quality Requirements Compiler | Planned |
| E27 | API Contract Compiler; Mermaid quality engine | Planned |
| E28 | Page-accurate publishing; Resume Compiler hardening | Planned |
| E29 | CLI / Git-native workflow | Planned |
| E30 | Situation engine | Planned |
| E31 | First Situation packs | Planned |
| E32 | Patch Compile | Planned |
| E33 | Organization rules / custom validators | Planned |
| E34 | GitHub App / CI integration | Planned |

## Screenshots and Demo

Screenshots are not fabricated in this pack. Add verified assets under `docs/assets/doccompile/` when they exist in the product repository. Recommended set:

* `editor_main.png` - main editor / compiler interface;
* `mermaid_document.png` - document with Mermaid and architecture icons;
* `transformation_before_after.png` - AI transformation input vs output;
* `admin_history.png` - admin transformation history / observability.

Architecture is documented as diagrams in [Architecture and Integrations](06-architecture-and-integrations.md) rather than a static PNG.

Live URL, sample requests, and GIFs should be linked here only after they are confirmed.

## What this project demonstrates

This project demonstrates the ability to:

* ship a local-first publishing engine and a serverless AWS SaaS contour as one product;
* meter AI as a bounded system (jobs, credits, versioned prompts) rather than an unbounded chat;
* reverse a workspace hypothesis when it competes with the user's existing document home;
* design the next architecture (Compiler, Harness, Artifact Contract) without presenting it as already deployed.
