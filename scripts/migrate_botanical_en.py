"""One-off: migrate docs/en/projects/botanical to compact structure."""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROJECT = ROOT / "docs" / "en" / "projects" / "botanical"

COMPACT_SPECS: list[tuple[str, str, list[str], bool]] = [
    ("01-overview.md", "Overview", ["01-overview.md"], True),
    ("02-context-and-problem.md", "Context and Problem", ["02-context.md", "03-problem.md"], False),
    (
        "03-goals-requirements-and-constraints.md",
        "Goals, Requirements, and Constraints",
        ["04-goals-and-non-goals.md", "05-requirements.md", "06-constraints.md"],
        False,
    ),
    ("04-role-and-responsibilities.md", "Role and Responsibilities", ["07-role-and-responsibilities.md"], True),
    (
        "05-system-model.md",
        "System Model",
        ["08-domain-model.md", "09-data-model.md", "10-api-contracts.md"],
        False,
    ),
    (
        "06-architecture-and-integrations.md",
        "Architecture and Integrations",
        ["14-architecture.md", "11-integration-flows.md"],
        False,
    ),
    (
        "07-security-quality-and-operations.md",
        "Security, Quality, and Operations",
        [
            "12-security-and-access-model.md",
            "13-non-functional-requirements.md",
            "17-failure-modes.md",
            "18-sizing-and-cost-notes.md",
        ],
        False,
    ),
    (
        "08-decisions-trade-offs-and-risks.md",
        "Decisions, Trade-offs, and Risks",
        ["15-key-decisions.md", "16-trade-offs.md"],
        False,
    ),
    (
        "09-roadmap-and-demonstration.md",
        "Roadmap and Demonstration",
        ["19-roadmap.md", "20-screenshots-and-demo.md", "21-what-this-demonstrates.md"],
        False,
    ),
]

OLD_GRANULAR = [
    "02-context.md",
    "03-problem.md",
    "04-goals-and-non-goals.md",
    "05-requirements.md",
    "06-constraints.md",
    "07-role-and-responsibilities.md",
    "08-domain-model.md",
    "09-data-model.md",
    "10-api-contracts.md",
    "11-integration-flows.md",
    "12-security-and-access-model.md",
    "13-non-functional-requirements.md",
    "14-architecture.md",
    "15-key-decisions.md",
    "16-trade-offs.md",
    "17-failure-modes.md",
    "18-sizing-and-cost-notes.md",
    "19-roadmap.md",
    "20-screenshots-and-demo.md",
    "21-what-this-demonstrates.md",
]

LINK_REWRITES = {
    "../07-role-and-responsibilities.md": "../04-role-and-responsibilities.md",
    "../15-key-decisions.md": "../08-decisions-trade-offs-and-risks.md#key-decisions",
    "07-role-and-responsibilities.md": "04-role-and-responsibilities.md",
    "15-key-decisions.md": "08-decisions-trade-offs-and-risks.md#key-decisions",
    "16-trade-offs.md": "08-decisions-trade-offs-and-risks.md#trade-offs",
}


def read(path: Path) -> str:
    if path.is_file():
        return path.read_text(encoding="utf-8")
    return ""


def rewrite_links(text: str) -> str:
    for old, new in LINK_REWRITES.items():
        text = text.replace(f"]({old})", f"]({new})")
        text = text.replace(f"](./{old})", f"](./{new})")
    return text


def promote_h2_to_h1(text: str) -> str:
    lines = text.splitlines()
    if lines and lines[0].startswith("## "):
        lines[0] = "# " + lines[0][3:]
    return "\n".join(lines).strip() + "\n"


def merge_sources(title: str, sources: list[str], promote_single: bool) -> str:
    bodies: list[str] = []
    for name in sources:
        body = read(PROJECT / name).strip()
        if body:
            bodies.append(body)

    if not bodies:
        return f"# {title}\n\n*Section content not yet documented.*\n"

    if promote_single and len(sources) == 1:
        return rewrite_links(promote_h2_to_h1(bodies[0]))

    parts = [f"# {title}\n"]
    for body in bodies:
        parts.append(rewrite_links(body))
    return "\n".join(parts).strip() + "\n"


def create_summary() -> str:
    index = read(PROJECT / "index.md")
    demonstrates = read(PROJECT / "21-what-this-demonstrates.md").strip()

    status = re.search(r"\*\*Status:\*\*\s*(.+)", index)
    role = re.search(r"\*\*Role:\*\*\s*(.+)", index)
    stack = re.search(r"\*\*Stack:\*\*\s*(.+)", index)
    value_match = re.search(
        r"\*\*Stack:\*\*.+\n\n(.+?)(?=\n## )", index, re.DOTALL
    )

    demo_section = ""
    if demonstrates:
        demo_section = demonstrates
        if demo_section.startswith("## What This Demonstrates"):
            demo_section = re.sub(
                r"^## What This Demonstrates\s*\n+### Relevance\s*\n+",
                "",
                demo_section,
            )
            demo_section = re.sub(
                r"^## What This Demonstrates\s*\n+",
                "",
                demo_section,
            )

    lines = [
        "# Summary",
        "",
        "## Status",
        "",
        (status.group(1).strip() if status else "TBD"),
        "",
        "## Role",
        "",
        (role.group(1).strip() if role else "TBD"),
        "",
        "## Stack",
        "",
        (stack.group(1).strip() if stack else "TBD"),
        "",
        "## Project value",
        "",
        (value_match.group(1).strip() if value_match else "TBD"),
    ]
    if demo_section.strip():
        lines.extend(["", "## What this demonstrates", "", demo_section.strip()])
    lines.append("")
    return "\n".join(lines)


def create_index() -> str:
    return """# Botanical SaaS

{% include-markdown "./summary.md" heading-offset=1 %}

## Quick reading path

1. [Overview](01-overview.md) — product summary and stack
2. [Context and Problem](02-context-and-problem.md) — background and problem statement
3. [Architecture and Integrations](06-architecture-and-integrations.md) — C4 container diagram
4. [Goals, Requirements, and Constraints](03-goals-requirements-and-constraints.md) — key implemented capabilities
5. [All-in-one](all-in-one.md) — full case study in one page

## Document assemblies

- [All-in-one](all-in-one.md) - all sections assembled for sequential reading and export
- [Architecture review](architecture-review.md) - goals through decisions for architecture review sessions
- [SRS pack](srs-pack.md) - context through operations for SRS-style review
- [Demo pack](demo-pack.md) - overview, role, architecture, decisions, roadmap, and demonstration

## Full structure

- [Summary](summary.md)
- [01 — Overview](01-overview.md)
- [02 — Context and Problem](02-context-and-problem.md)
- [03 — Goals, Requirements, and Constraints](03-goals-requirements-and-constraints.md)
- [04 — Role and Responsibilities](04-role-and-responsibilities.md)
- [05 — System Model](05-system-model.md)
- [06 — Architecture and Integrations](06-architecture-and-integrations.md)
- [07 — Security, Quality, and Operations](07-security-quality-and-operations.md)
- [08 — Decisions, Trade-offs, and Risks](08-decisions-trade-offs-and-risks.md)
- [09 — Roadmap and Demonstration](09-roadmap-and-demonstration.md)
- [Architecture Decision Records](adr/index.md)
"""


def update_adr_index() -> None:
    path = PROJECT / "adr" / "index.md"
    text = read(path)
    text = rewrite_links(text)
    if "adr/index.md" not in text and "08-decisions" in text:
        pass
    if "See also" not in text and "architecture documentation" in text:
        pass
    path.write_text(text, encoding="utf-8", newline="\n")


def append_adr_link_to_decisions(content: str) -> str:
    if "adr/index.md" in content:
        return content
    return content.rstrip() + "\n\nSee also [Architecture Decision Records](adr/index.md).\n"


def main() -> int:
    (PROJECT / "summary.md").write_text(create_summary(), encoding="utf-8", newline="\n")

    for target, title, sources, promote in COMPACT_SPECS:
        content = merge_sources(title, sources, promote)
        if target == "08-decisions-trade-offs-and-risks.md":
            content = append_adr_link_to_decisions(content)
        (PROJECT / target).write_text(content, encoding="utf-8", newline="\n")

    (PROJECT / "index.md").write_text(create_index(), encoding="utf-8", newline="\n")
    update_adr_index()

    for name in OLD_GRANULAR:
        path = PROJECT / name
        if path.is_file():
            path.unlink()

    subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "generate_all_in_one.py"), str(PROJECT)],
        check=True,
    )

    sys.path.insert(0, str(ROOT / "scripts"))
    from generate_packs import PACKS, render_pack, update_index  # noqa: E402

    for pack_name, meta in PACKS.items():
        content = render_pack(PROJECT, "en", pack_name, meta)
        (PROJECT / f"{pack_name}.md").write_text(content, encoding="utf-8", newline="\n")
    update_index(PROJECT / "index.md", "en")

    print(f"Migrated {PROJECT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
