# Context and Problem

## Context

LLMs and technical professionals are good at producing structured text, Markdown, code, requirements, diagrams, and architecture discussions. Turning that material into a professional deliverable still often requires manual copy/paste into Word, Google Docs, or another document editor.

Diagrams are a typical fracture point. A Mermaid sequence or C4 sketch lives next to the source in Git, then has to be re-drawn or exported into a slide or Word file. The published PDF drifts from the source. The docs-as-code workflow breaks at the last mile.

The initial product therefore focused on a portable path:

```text
portable Markdown
→ diagrams-as-code
→ professional rendering
→ PDF
```

Markdown remains the source of truth. The product favors portable standards: GFM / Markdown, Mermaid, Iconify-compatible architecture icons, YAML front matter, conventional image/asset links, and later potentially LaTeX. Content should stay compatible with Git / GitHub, VS Code / Cursor, MkDocs, Mermaid tooling, and ordinary Markdown tooling.

## Problem

Two problems stacked on top of each other.

### 1. Publishing last mile

Professionals already have source material. They do not need another place to type. They need a reliable way to:

- keep Markdown as the working format;
- render diagrams without a proprietary canvas;
- produce a professional PDF that matches the source;
- avoid one broken diagram collapsing the whole document;
- do this without uploading confidential drafts to a workspace they do not control.

Raw meeting notes and transcripts make the last mile more expensive. An expert still has to turn messy source into an ADR, a requirements pack, a resume, or a proposal. That work is repetitive, easy to get slightly wrong, and hard to check.

### 2. Workspace gravity

During product development, the natural SaaS expansion was a proprietary cloud document store: workspace, document management, a broader editor. That path would put DocCompile into competition for where documents live — against Notion, Confluence, GitBook, Google Docs, and the user's own Git repository.

That is the wrong fight for this product. Technical users already have a home for documents. Switching cost is high. A workspace also pulls the architecture toward persistent document storage, which conflicts with the local-first privacy position.

## Strategic pivot

The decision:

> Do not own the document. Own the transformation.

DocCompile should not compete for the place where documents live. It should compete for the moment where messy source material becomes a correct professional artifact.

Possible persistence and output sinks stay where the user already works: local files, portable packages, Git repositories, CLI, downloads, and later APIs / integrations.

The interesting engineering problem is not calling an LLM. It is building a controlled compilation system around it: contracts, evidence, validation, repair, cost bounds, and measurable quality.
