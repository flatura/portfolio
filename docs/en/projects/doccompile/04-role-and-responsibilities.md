# Role and Responsibilities

## My Role

The project is founder-led and end-to-end. I own the product hypothesis, the architecture, and the implementation.

Work included:

* product discovery and positioning, including the pivot from docs-as-code publisher and workspace ideas to a processing-layer / Compiler platform;
* requirements definition and constraints (local-first, credits, no proprietary document store as the core);
* solution architecture and system analysis: domain model, job lifecycle, identity, billing, and AI transformation boundaries;
* UX and product workflow design for local rendering versus explicit server-side compilation;
* AWS architecture: CloudFront / private S3, API Gateway, Lambda, DynamoDB, Cognito, and related serverless services;
* Terraform infrastructure and GitHub Actions CI/CD with OIDC;
* authentication and authorization design (Cognito; USER / ADMIN / SUPER_ADMIN);
* billing and credit architecture (Paddle as merchant of record; credits as compute metering);
* AI transformation architecture, prompt / contract design, and runtime versioning;
* observability and quality strategy (transformation history, admin control plane, target Compiler Health);
* privacy and cost trade-offs;
* implementation, debugging, dogfooding, and roadmap prioritization.

AI assistants were used as a development accelerator for routine implementation. Architectural decisions, product direction, data boundaries, access model, review, and deployment remained under my control.

## AI Usage

LLMs were used to accelerate routine implementation, generate boilerplate, and iterate quickly. They were not treated as authors or owners of the system.

Kept under manual control:

* requirements interpretation and product positioning;
* domain modeling;
* architecture decisions;
* privacy and cost boundaries;
* access model;
* prompt / contract design;
* code review and debugging;
* deployment decisions;
* technical documentation.
