# Decisions, Trade-offs, and Risks

## Key Decisions

### Markdown as the portable source of truth

LLM and technical output is already Markdown. The product keeps Markdown, Mermaid, icons, and conventional assets instead of a proprietary editor format. Compatibility with Git, VS Code / Cursor, MkDocs, and ordinary Markdown tooling is a product requirement, not an export afterthought.

### Client-side-first rendering

Professional drafts stay in the browser for render, theme, Mermaid, local assets, and PDF. Server-side processing is an explicit compile action, not the default path.

### Terraform-managed AWS infrastructure

A single-person operation needs a rebuildable environment. Production AWS is expressed in Terraform, deployed through GitHub Actions with OIDC.

### Cognito for authentication

Managed identity for SaaS instead of a custom JWT stack. Roles (USER / ADMIN / SUPER_ADMIN) sit on top of Cognito identity.

### Credits as compute metering

Variable-cost AI is the monetization unit. Local rendering is not degraded to force payment. Credits bound cost per user and per job.

### Runtime / versioned prompts

AI behavior must change independently of application deploys. Prompts and related configuration live in DynamoDB-backed runtime configuration with publish / rollback.

### Universal Harness vs per-Compiler logic (target)

Current transformations are per-artifact implementations. The target is generic orchestration that executes a Compiler contract. Adding a Compiler should not require changing Harness core logic.

### Processing layer vs Cloud Workspace (strategic pivot)

Proprietary document storage and workspace features are deprioritized. DocCompile owns compilation, not the place where documents live.

See also [Architecture Decision Records](adr/index.md).

## Architectural Trade-offs

### 1. Markdown as the portable source of truth

#### Context

LLMs and engineers already produce Markdown. A proprietary canvas would capture lock-in and break Git-native workflows.

#### Decision

Keep GFM / Markdown, Mermaid, Iconify-compatible icons, YAML front matter, and conventional asset links as the working representation.

#### Rejected alternatives

WYSIWYG Word-like format; Notion-style blocks as the source of truth.

#### Rationale

Portable standards lower switching cost, match the author's existing tools, and keep diagrams-as-code in the same file as the text.

#### Trade-offs

* Print/PDF fidelity is harder than in InDesign or Word.
* Users who want a block editor may bounce.
* Mermaid and pagination edge cases become product work.

#### Compensating measures

* Pagination hardening and professional themes on the client.
* Isolate a broken diagram from the rest of the document.
* Later LaTeX as an option, not a required source format.

#### Review trigger

A paying segment that cannot accept Markdown as source; or print constraints that cannot be met in the browser.

---

### 2. Client-side-first rendering instead of a server-side editor

#### Context

Drafts include unpublished architecture, requirements, and personal career data. A mandatory upload-to-preview path would fight the privacy position and raise baseline cost.

#### Decision

The browser renders and exports locally. The server is used when the user requests compilation, billing, or admin operations.

#### Rejected alternatives

Server-side rendering pipeline as the only path; storing every document in a cloud workspace to enable preview.

#### Rationale

Privacy by default, low idle cost, and no document database as a prerequisite for publishing.

#### Trade-offs

* Server-side capabilities require an explicit upload / compile.
* Browser CPU and print CSS become first-class constraints.
* Cross-device document sync is not a platform feature.

#### Compensating measures

* Clear UI boundary between local export and AI compile.
* Credits and identity only on the server path.
* Target Git / CLI sinks instead of a proprietary store.

#### Review trigger

Need for server-side Chromium pagination at a quality the browser cannot meet; then a bounded Fargate worker, not a default editor backend.

---

### 3. Terraform-managed AWS instead of console or CDK

#### Context

Founder-led operations need a reproducible environment and cheap disaster recovery of infrastructure, not a unique snowflake account.

#### Decision

AWS production topology is Terraform.

#### Rejected alternatives

Click-ops console; AWS CDK; Pulumi.

#### Rationale

Declarative infra matches the rest of the docs-as-code posture. Terraform is sufficient for this serverless topology.

#### Trade-offs

* Terraform state and blast-radius discipline are operational duties.
* CDK might map more naturally to some AWS APIs.
* Drift still has to be watched.

#### Compensating measures

* GitHub Actions apply with OIDC.
* Least-privilege IAM in the same codebase.
* No long-lived deploy keys in CI.

#### Review trigger

Team growth that needs a different IaC standard; or AWS features that Terraform cannot express cleanly.

---

### 4. Cognito for authentication

#### Context

SaaS needs registration, session, and roles without building a custom identity platform.

#### Decision

Amazon Cognito as the identity provider for authenticated routes.

#### Rejected alternatives

Auth0; custom JWT issuance; Firebase Auth.

#### Rationale

Stays inside the AWS account, integrates with API Gateway authorizers, and avoids another vendor for a small product.

#### Trade-offs

* Cognito UX and quota limits are AWS's.
* Hosted UI constraints versus a fully custom login.
* Multi-region identity is not free.

#### Compensating measures

* RBAC enforced again in the backend, not only in the token.
* Local features remain usable without sign-in.

#### Review trigger

Identity requirements Cognito cannot meet (enterprise IdP complexity, specific compliance packaging) at a price that justifies Auth0 or a dedicated IdP.

---

### 5. Credits as compute metering

#### Context

LLM calls have variable cost. Charging for PDF export would tax the free local foundation and invite a worse product.

#### Decision

Credits meter AI / compute-heavy operations. Local creation and publishing stay capable without credits.

#### Rejected alternatives

Subscription-only with unlimited AI; per-PDF pricing; hiding rendering quality behind a paywall.

#### Rationale

Aligns price with actual provider cost. Preserves the publishing last mile as a trustworthy free/local path.

#### Trade-offs

* Credit UX is harder than a flat subscription.
* Users may under-use AI if packs are confusing.
* Does not by itself prevent quality problems.

#### Compensating measures

* Job-level cost accounting.
* Rate limits and failure timeouts.
* Paddle as merchant of record so tax/payment machinery is not built in-house.

#### Review trigger

A segment that only wants simple subscription AI; or provider pricing that makes packs unexplainable.

---

### 6. Runtime / versioned prompts instead of hardcoded AI behavior

#### Context

Compilation quality will change weekly. Redeploying the SPA or Lambdas to tweak a prompt is the wrong release coupling.

#### Decision

Prompts and related runtime configuration are versioned server-side, with publish and rollback.

#### Rejected alternatives

Prompts hardcoded in application builds; one global unversioned prompt blob.

#### Rationale

Separates model behavior releases from application releases. Enables INTERNAL testing before PUBLIC.

#### Trade-offs

* Runtime config becomes a production surface that needs access control.
* Prompt/code skew if the application cannot execute an old contract.
* Operators can ship a bad prompt quickly.

#### Compensating measures

* ADMIN / SUPER_ADMIN only.
* Rollback path.
* Target INTERNAL -> PUBLIC Compiler lifecycle.

#### Review trigger

Compiler contracts become code-defined artifacts whose prompts are only parameters; then config and contract versioning must stay aligned.

---

### 7. Universal Harness vs per-Compiler workflow logic (target)

#### Context

Working transformations exist as per-type implementations. That does not scale to many Compilers, Situations, or Patch Compile.

#### Decision

Evolve toward a generic Harness that executes Compiler-supplied contracts. Prefer Step Functions for bounded multi-stage orchestration over an autonomous agent graph.

#### Rejected alternatives

Keep per-Compiler hardcoded orchestration indefinitely; LangGraph-style agent routing as the default.

#### Rationale

The planned Harness is bounded, deterministic-first orchestration with optional semantic checks. An agent framework is optional only if routing becomes genuinely model-driven.

#### Trade-offs

* Migration cost from current per-type jobs.
* Step Functions operational complexity.
* Risk of building a framework before 2–3 Compilers are actually good.

#### Compensating measures

* Start with a small set of reference Compilers.
* Deterministic checks where possible; explicit failure instead of invented output.
* LangGraph remains a later option, not the current target core.

#### Review trigger

Routing becomes open-ended and model-driven; or Step Functions prove a poor fit for the stage graph.

---

### 8. Processing layer vs Cloud Workspace

#### Context

The earlier expansion path was proprietary cloud storage, workspace, and a broader editor. That competes with tools users already have.

#### Decision

Deprioritize proprietary document storage. Own the transformation. Persist to local files, downloads, Git, CLI, and later APIs.

#### Rejected alternatives

Full Notion-like workspace as the product center.

#### Rationale

Lower switching cost, better fit for technical workflows, and a cleaner privacy story.

#### Trade-offs

* No default cross-device document cloud.
* Harder to show "all your docs in DocCompile".
* Integrations become more important than an internal file tree.

#### Compensating measures

* Strong local/Git-native direction on the roadmap.
* Compile as an explicit, valuable moment rather than a place to live.

#### Review trigger

A B2B buyer that will not adopt without a hosted workspace; then a workspace would be an integration, not the core Compiler engine.

## Risks

| Risk | Why it matters | Mitigation |
|---|---|---|
| Transformation quality may not beat a good LLM prompt by enough | Users will not pay for a thin wrapper | Reference-quality Compilers first; contracts and validators, not prompt theatre |
| Semantic validation becomes validation theatre | False trust | Separate deterministic checks from probabilistic ones; never claim "AI verified" |
| Compiler-specific domain work scales poorly | Founder bandwidth | Small Compiler set; Harness invariants; INTERNAL -> PUBLIC |
| Multi-artifact Situations drift | Contradictory packs | Canonical facts and cross-artifact checks (target) |
| Patch Compile is hard | Brownfield is the real job | Treat as later epoch; depends on identity, facts, contracts, diffs |
| Cold start for eval datasets | No Compiler Health | Dogfood, outcome signals, local edit-distance buckets |
| Provider behavior and pricing change | Cost and quality shocks | Replaceable LLM; credits; versioned prompts |
| Technical audience resists SaaS lock-in | Distribution | Local/Git-native path; Markdown remains portable |
| Distribution | Product risk independent of architecture | Dogfooding, narrow Compilers, clear demo artifacts |
