# Architecture Case-Study Documentation Template

Reusable placeholder tree for splitting a single-project architecture write-up into a structured, navigable case study.

## Purpose

Each project gets a folder under `docs/<locale>/projects/<slug>/` with a landing page (`index.md`), 21 numbered section files, and an ADR subtree. This template provides empty placeholders with headings and brief instructions — no project-specific content.

## How to use

1. Copy the locale subtree into your docs tree:

   ```text
   architecture-docs-template/en/  →  docs/en/projects/<slug>/
   architecture-docs-template/ru/  →  docs/ru/projects/<slug>/
   ```

2. Fill in placeholders. Move content from an existing single-page `projects/<slug>.md` into the matching section files (see mapping below).

3. Update `index.md`: project name, status, role, stack, value statement, and links.

4. Register the project in `mkdocs.yml` nav (both EN and RU blocks).

## Section-to-content mapping

| File | Typical content |
|------|-----------------|
| `index.md` | Landing: summary, status, role, stack, value statement, link list |
| `01-overview.md` | Product/system overview, technology stack |
| `02-context.md` | Background, business or organizational context |
| `03-problem.md` | Problem statement, pain points |
| `04-goals-and-non-goals.md` | Goals, explicit non-goals |
| `05-requirements.md` | Functional requirements, capabilities |
| `06-constraints.md` | Technical, legal, budget, timeline constraints |
| `07-role-and-responsibilities.md` | Your role, team, workflow |
| `08-domain-model.md` | Domain concepts, actors, bounded contexts |
| `09-data-model.md` | Entities, schemas, persistence |
| `10-api-contracts.md` | Endpoints, events, message formats |
| `11-integration-flows.md` | Sequences, process flows, external systems |
| `12-security-and-access-model.md` | Auth, RBAC, tenancy, isolation |
| `13-non-functional-requirements.md` | Performance, availability, deployment |
| `14-architecture.md` | C4, deployment, component diagrams |
| `15-key-decisions.md` | Major architectural decisions |
| `16-trade-offs.md` | Alternatives considered, compromises |
| `17-failure-modes.md` | Failure scenarios, mitigations |
| `18-sizing-and-cost-notes.md` | Scale, cost, capacity estimates |
| `19-roadmap.md` | Future work, documentation links |
| `20-screenshots-and-demo.md` | UI screenshots, demo scenarios |
| `21-what-this-demonstrates.md` | Portfolio relevance, skills demonstrated |
| `adr/index.md` | ADR index and links |
| `adr/adr-000-template.md` | Fillable ADR skeleton (copy per decision) |

## Empty-section rule

If a section has no source content, keep the file with **only its H1 heading**. Do not invent filler text.

## All-in-one assembly (`all-in-one.md`)

Copy `all-in-one.md` from the locale subtree alongside the numbered modules. The page uses `mkdocs-include-markdown-plugin` with `heading-offset=1` so each module H1 becomes H2 under a single assembly H1. Include paths must use the `./` prefix (e.g. `"./01-overview.md"`).

1. Set the assembly H1 (`# [Project Name] — all-in-one` / `# [Project Name] — всё вместе`).
2. Generate the Contents block:

   ```bash
   python scripts/assembly_toc.py docs/en/projects/<slug>
   python scripts/assembly_toc.py docs/ru/projects/<slug>
   ```

   EN headings get semantic anchors (`#overview`). RU Cyrillic headings get numeric fallbacks (`#_2`, `#_5`, …) because Python-Markdown slugify strips non-ASCII; the script simulates the full assembled page (Contents h2 + all module subheadings) so anchors match `mkdocs build`.
3. Add `All-in-one` / `Всё вместе` to `mkdocs.yml` nav (both EN and RU blocks).
4. Link from `index.md` (Quick reading path + Document assemblies).
5. Validate: `mkdocs build --strict`. Spot-check mermaid fences and `<figure markdown>` on diagram- or screenshot-heavy projects.

Cross-module `.md` links inside numbered modules resolve to standalone module pages when clicked from the assembly page; that is expected.

## Extraction

This directory lives at the repo root (outside `docs/`) so MkDocs does not build it. It can be copied or subtree-split into a standalone public template repository.
