# Goals, Requirements, and Constraints

## Goals and Non-Goals

### Primary project goals

* Preserve portable source formats (Markdown / GFM, Mermaid, conventional assets) as the working representation.
* Produce professional deliverables (print layout and PDF) from that source without a proprietary editor format.
* Support diagrams-as-code so architecture and sequence diagrams stay in the same file as the text.
* Isolate rendering failures so one broken diagram does not break the whole document.
* Keep client-side-first / local behavior for rendering, styling, local assets, and PDF operations.
* Make AI usage financially bounded through credits and cost controls.
* Make AI behavior configurable and versioned independently of application deploys.
* Provide transformation history and admin observability for server-side AI jobs.
* Evolve toward explicit Artifact Contracts: compilation succeeded, produced warnings, or failed.
* Support Git-native outputs so the artifact can return to the user's existing workflow.

### Out of scope

* Not a general-purpose cloud document workspace or Notion/Confluence replacement.
* Not a WYSIWYG Word clone and not a proprietary block editor as the source of truth.
* Not a guarantee of hallucination-free AI output. Target checks are deterministic validation, source-grounding, and bounded repair — not an unprovable "fully verified AI" claim.
* Not tied permanently to a single LLM vendor.
* Does not invent missing professional facts when source evidence is absent; unresolved items should remain unresolved.
* Does not include formal SLA / RTO / RPO values in this portfolio pack. Those values are Unknown / TBD unless defined in project operations artifacts.
* Current architecture does not assume EC2 or always-on containers unless the product repository actually contains them.

## Requirements

### Business Requirements

- **BR-001. Portable source of truth.**  
  The user must be able to work in Markdown (GFM), with Mermaid, architecture icons, YAML front matter, and conventional image links, without converting into a proprietary storage format.

- **BR-002. Professional publishing last mile.**  
  The system must render a professional document and support PDF export from the local source, including print layout and pagination hardening.

- **BR-003. Local-first by default.**  
  Rendering, styling, local assets, Mermaid, and local PDF operations must work in the browser. Document content must not leave the browser unless the user explicitly requests a server-side operation.

- **BR-004. Bounded AI compilation.**  
  Server-side AI transformations must be metered (credits), cost-controlled, and attributable to a user and a transformation type.

- **BR-005. Configurable AI behavior.**  
  Prompts and related runtime configuration must be versioned and publishable / rollable back without redeploying the application.

- **BR-006. Identity and administration.**  
  Authenticated SaaS operations must use managed identity. An admin control plane must exist for configuration, observability, and elevated roles.

- **BR-007. Commercial contour.**  
  Variable-cost intelligence is the monetization unit. Local rendering quality must not be artificially degraded to force payment.

- **BR-008. Artifact contract direction.**  
  The product should evolve from "the model generated something" to an explicit compilation result: success, warnings, or failure against a Compiler contract.

- **BR-009. Evidence grounding direction.**  
  Important output claims should become traceable to source evidence. Missing evidence must not be filled in silently.

- **BR-010. Git-native outputs.**  
  Compiled artifacts should be able to return to local files, downloads, and later Git / CLI workflows rather than remaining locked in a proprietary store.

The public version includes a shortened requirements fragment. Internal billing amounts, prompt texts, and unpublished Compiler contracts are not disclosed.

## Rules and Constraints

### Business Rules

* **RULE-001. Local work does not require upload.**  
  Opening, editing, rendering, and exporting a document locally must not require sending document body to the backend.

* **RULE-002. Server-side processing is explicit.**  
  Content is sent to the backend only when the user invokes a server-side capability such as AI compilation.

* **RULE-003. Credits meter compute, not publishing quality.**  
  Free / local capabilities provide the creation and publishing foundation. Credits pay for AI / compute-heavy operations.

* **RULE-004. Do not invent missing facts.**  
  A compilation must not present unsupported professional facts as if they were present in the source. Unresolved decisions remain unresolved.

* **RULE-005. Compiler invariants outrank templates.**  
  A custom output template may change artifact structure. It must not weaken Compiler guarantees (grounding, validators, repair bounds).

* **RULE-006. LLM provider is replaceable.**  
  Product value sits in Compiler specifications, contracts, evidence models, validators, repair, and quality evaluation — not in one prompt or one vendor.

### Constraints

* **CON-001. Founder-led, cost-sensitive serverless architecture.**  
  Idle cost must stay low. Continuously running backends are avoided unless a workload justifies them.

* **CON-002. No unnecessary persistent document backend.**  
  The system must not require proprietary cloud document storage for the core publishing path.

* **CON-003. No mandatory authentication for purely local / free features.**  
  Identity is required for SaaS / AI / billing operations, not for local rendering.

* **CON-004. Privacy-sensitive professional content.**  
  Drafts may include unpublished architecture, requirements, and personal career data. Default processing stays in the browser.

* **CON-005. AWS infrastructure must be reproducible through Terraform.**  
  Production environment is not a click-ops console setup.

* **CON-006. Serverless orchestration first.**  
  Specialized compute (for example ECS Fargate) is introduced only when Lambda boundaries are insufficient. EC2 / GPU only if future self-hosted inference or sustained workloads justify it.

* **CON-007. Formal operational SLAs are TBD.**  
  This portfolio pack does not invent RTO / RPO / availability targets.
