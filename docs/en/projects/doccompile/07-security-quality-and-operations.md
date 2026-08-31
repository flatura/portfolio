# Security, Quality, and Operations

## Security and Access Model

### Identity

Authenticated SaaS operations use Amazon Cognito. Local rendering and PDF export do not require identity.

Claimed RBAC roles: USER, ADMIN, SUPER_ADMIN. Exact permission matrix should be confirmed against the product repository.

### Backend authorization

API Gateway and Lambda enforce identity on server-side routes. Admin runtime configuration, prompt publish / rollback, and cross-user observability are restricted to elevated roles. Provider API keys and billing secrets stay server-side.

### Infrastructure

* private S3 origin for the SPA, accessed through CloudFront OAC rather than a public website bucket;
* least-privilege IAM for Terraform-managed roles;
* GitHub OIDC for deploys (no long-lived deployment access keys in CI);
* Paddle webhook signature verification before credit or entitlement changes;
* abuse and cost controls around transformation jobs (credits, rate limits).

### Privacy

Local-first renderer: Markdown, Mermaid, styling, local assets, and local PDF operations run in the browser. There is no mandatory upload for local document work.

Server-side content processing happens only for explicitly requested capabilities such as AI compilation.

Telemetry is designed as privacy-conscious operational data, not as another document store. Edited document text should not need to be uploaded merely to calculate quality signals (for example local edit-distance buckets). Do not over-read this as a certified privacy program; legal documents should be checked separately.

## Quality

### Current

* transformation history;
* admin observability of jobs;
* prompt versioning with publish / rollback;
* output handling for generated artifacts;
* cost / usage tracking through credits.

Depth of history, quality telemetry, and Compiler publication states (PUBLIC / INTERNAL / DISABLED) should be confirmed against the product repository.

### Target

* Artifact Contract as the definition of success;
* deterministic validators (parse, schema, required sections, renderable diagrams);
* semantic consistency checks (probabilistic; not "AI verified");
* evidence grounding;
* bounded repair loops;
* Compiler Health metrics: success rate, acceptance rate, accepted unchanged, repair rate, validation failures, cost, latency.

Deterministic validation and probabilistic semantic checking are different. A second LLM pass is not treated as proof.

### Quality telemetry direction

| Signal | Meaning |
|---|---|
| Pipeline trace | Operational path of an individual Compile |
| Outcome signal | Accept / accept with edits / reject / regenerate / export / abandon |
| Aggregate Compiler Health | Metrics by Compiler / version / template |

The long-term moat depends on measurable quality improvement, not on accumulating raw logs.

## Non-Functional Requirements

| Attribute | Scenario | Approach |
|---|---|---|
| Privacy | A draft ADR must not be uploaded just to preview PDF | local-first renderer |
| Security | USER must not publish prompt config | Cognito roles, server-side authorization |
| Cost | A runaway compile must not unbounded-bill the founder | credits, job limits, replaceable provider |
| Operability | Environment must be rebuildable | Terraform, GitHub Actions OIDC |
| Change isolation | AI behavior changes without app deploy | runtime / versioned prompts |
| Integrity | Missing source facts must not appear as truth | target: fail or warn instead of invent |

## Failure Modes

| Risk | Impact | Mitigation |
|---|---|---|
| Prompt or model regression | Worse artifacts in production | prompt versions, rollback, INTERNAL publication |
| Unbounded LLM cost | Bill shock | credits, limits, job timeouts |
| Webhook spoofing | Fake credit grants | Paddle signature verification |
| Public S3 origin | Asset or config exposure | private origin + OAC |
| Long-lived CI keys | Credential leak | GitHub OIDC |
| Semantic-check theatre | False confidence in output | distinguish deterministic vs probabilistic checks |
| Local/cloud split confusion | User thinks content stayed local after compile | explicit compile action |

## Sizing and Cost Notes

### Primary load drivers

- local rendering (client CPU; not billed as AWS compute);
- transformation job rate and token volume;
- admin observability queries;
- CloudFront traffic for the SPA;
- DynamoDB reads/writes for jobs, credits, and config.

### Primary cost drivers

- LLM provider usage (dominant variable cost);
- Lambda / API Gateway;
- DynamoDB;
- CloudFront and S3;
- Cognito MAU;
- Paddle fees;
- observability storage.

### Scaling tiers

See [Roadmap and Demonstration](09-roadmap-and-demonstration.md).

## Operations

* Terraform for AWS;
* GitHub Actions for build and deploy;
* logs / metrics in the AWS account (exact backends TBD in this pack);
* credit / cost protection on jobs;
* runtime configuration and admin control plane;
* prompt rollback without application redeploy.
