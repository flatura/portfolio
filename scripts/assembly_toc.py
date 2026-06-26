"""Generate the Contents section for all-in-one.md from module headings.

Simulates the assembled page: page Contents h2, then each module with
heading-offset=1, using Python-Markdown slug rules (including global _N
fallbacks for non-ASCII headings).

Usage:
  python scripts/assembly_toc.py docs/en/projects/ai_oip
  python scripts/assembly_toc.py docs/ru/projects/ai_oip
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

from markdown.extensions.toc import slugify

MODULES = [
    "01-overview.md",
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

HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$")
ADR_LABEL = "Architecture Decision Records"
ADR_ANCHOR = "architecture-decision-records"
HEADING_OFFSET = 1


def parse_headings(text: str) -> list[tuple[int, str]]:
    headings: list[tuple[int, str]] = []
    for line in text.splitlines():
        match = HEADING_RE.match(line)
        if match:
            level = len(match.group(1))
            title = match.group(2).strip()
            headings.append((level, title))
    return headings


class AnchorRegistry:
    def __init__(self) -> None:
        self._counts: dict[str, int] = {}
        self._numeric = 0

    def assign(self, title: str) -> str:
        base = slugify(title, "-")
        if not base:
            self._numeric += 1
            anchor = f"_{self._numeric}"
            self._counts[anchor] = 1
            return anchor
        if base not in self._counts:
            self._counts[base] = 0
        self._counts[base] += 1
        if self._counts[base] == 1:
            return base
        return f"{base}_{self._counts[base] - 1}"


def module_entry_anchors(project_dir: Path, lang: str) -> list[tuple[str, str]]:
    registry = AnchorRegistry()
    entries: list[tuple[str, str]] = []

    registry.assign("Contents" if lang == "en" else "Содержание")

    for name in MODULES:
        headings = parse_headings((project_dir / name).read_text(encoding="utf-8"))
        module_title = headings[0][1]
        module_anchor: str | None = None

        for level, title in headings:
            adjusted = level + HEADING_OFFSET
            anchor = registry.assign(title)
            if adjusted == 2 and title == module_title and module_anchor is None:
                module_anchor = anchor

        if module_anchor is None:
            raise ValueError(f"Could not resolve module anchor for {name}")
        entries.append((module_title, module_anchor))

    return entries


def contents_section(lang: str, project_dir: Path) -> str:
    heading = "## Contents" if lang == "en" else "## Содержание"
    lines = [heading, ""]
    for title, anchor in module_entry_anchors(project_dir, lang):
        lines.append(f"- [{title}](#{anchor})")
    lines.append(f"- [{ADR_LABEL}](#{ADR_ANCHOR})")
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    if len(sys.argv) != 2:
        print(__doc__, file=sys.stderr)
        return 2
    project_dir = Path(sys.argv[1])
    lang = "ru" if "ru" in project_dir.parts else "en"
    print(contents_section(lang, project_dir))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
