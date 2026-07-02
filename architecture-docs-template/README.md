# Architecture Case-Study Documentation Template

Reusable placeholder tree for splitting a single-project architecture write-up into a compact, navigable case study.

## Purpose

Each project gets a folder under `docs/<locale>/projects/<slug>/` with:

- `summary.md` — single source of truth for status, role, stack, and value statement
- `index.md` — landing page (includes summary dynamically)
- nine compact section files (`01`–`09`)
- four assembled pages (`all-in-one.md`, `architecture-review.md`, `srs-pack.md`, `demo-pack.md`)
- an ADR subtree

This template provides empty placeholders with headings, brief instructions, and checklist items — no project-specific content.

## How to use

1. Copy the locale subtree into your docs tree:

   ```text
   architecture-docs-template/en/  →  docs/en/projects/<slug>/
   architecture-docs-template/ru/  →  docs/ru/projects/<slug>/
   ```

2. Fill in placeholders. Move content from an existing single-page `projects/<slug>.md` or from granular legacy modules into the matching compact section files (see mapping below).

3. Update `index.md` project name and `summary.md` fields (status, role, stack, value).

4. Regenerate assembled pages:

   ```bash
   python scripts/generate_all_in_one.py docs/en/projects/<slug>
   python scripts/generate_all_in_one.py docs/ru/projects/<slug>
   python scripts/generate_packs.py
   ```

5. Register the project in `mkdocs.yml` nav (both EN and RU blocks).

## Compact section semantics

| File | Typical content (merged from legacy modules) |
|------|-----------------------------------------------|
| `summary.md` | Status, role, stack, project value, optional portfolio note |
| `index.md` | Title, summary include, quick path, assemblies, full structure |
| `01-overview.md` | Product/system overview, technology stack |
| `02-context-and-problem.md` | Context + problem statement |
| `03-goals-requirements-and-constraints.md` | Goals/non-goals + requirements + constraints |
| `04-role-and-responsibilities.md` | Your role, team, workflow |
| `05-system-model.md` | Domain model + data model + API contracts |
| `06-architecture-and-integrations.md` | Architecture + integration flows |
| `07-security-quality-and-operations.md` | Security + NFR + failure modes + sizing/cost |
| `08-decisions-trade-offs-and-risks.md` | Key decisions + trade-offs (+ link to ADR index) |
| `09-roadmap-and-demonstration.md` | Roadmap + screenshots/demo + portfolio relevance |
| `adr/index.md` | ADR index and links |
| `adr/adr-000-template.md` | Fillable ADR skeleton (copy per decision) |

## Summary as single source of truth

`summary.md` holds the short project summary. Every page that needs it includes it dynamically:

```markdown
{% include-markdown "./summary.md" heading-offset=1 %}
```

Do not duplicate summary text in `index.md` or pack pages by hand.

## Include and heading-offset convention

Assembled pages use `mkdocs-include-markdown-plugin` with `heading-offset=1` so each included file's H1 becomes H2 under a single assembly H1. Include paths use the `./` prefix (e.g. `"./01-overview.md"`).

Compact section files start at H1 for standalone pages. Merged sub-parts use H2 (e.g. `## Context` inside `02-context-and-problem.md`).

## Empty-section rule

If a section has no source content, keep the file with its H1 heading and placeholders. Do not invent filler project facts.

## Document assemblies

| Assembly | Includes |
|----------|----------|
| `all-in-one.md` | `summary.md`, `01`–`09`, ADR footer |
| `architecture-review.md` | `summary.md`, `03`, `05`, `06`, `07`, `08` |
| `srs-pack.md` | `summary.md`, `02`, `03`, `04`, `05`, `06`, `07` |
| `demo-pack.md` | `summary.md`, `01`, `04`, `06`, `08`, `09` |

Regenerate Contents blocks with:

```bash
python scripts/assembly_toc.py docs/en/projects/<slug>
python scripts/assembly_toc.py docs/ru/projects/<slug>
```

EN headings get semantic anchors (`#overview`). RU Cyrillic headings get numeric fallbacks (`#_2`, `#_5`, …) because Python-Markdown slugify strips non-ASCII; the script simulates the full assembled page so anchors match `mkdocs build`.

Validate: `mkdocs build --strict`. Spot-check mermaid fences and `<figure markdown>` on diagram- or screenshot-heavy projects.

Cross-module `.md` links inside compact sections resolve to standalone section pages when clicked from an assembly page; that is expected.

## Extraction

This directory lives at the repo root (outside `docs/`) so MkDocs does not build it. It can be copied or subtree-split into a standalone public template repository.
