"""Generate all-in-one.md for a structured project directory."""

from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from assembly_toc import contents_section  # noqa: E402

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

INCLUDES = "\n".join(
    f'{{% include-markdown "./{name}" heading-offset=1 %}}' for name in MODULES
)

EN_INTRO = (
    "This page is assembled from modular project documentation files. "
    "Individual modules remain the source of truth; this page is for sequential reading, "
    "review, and PDF-style export."
)
RU_INTRO = (
    "Эта страница собирается из модулей проектной документации. "
    "Отдельные модули остаются источником истины; эта страница предназначена "
    "для последовательного чтения, ревью и экспорта в стиле PDF."
)


def project_title(project_dir: Path) -> str:
    index = (project_dir / "index.md").read_text(encoding="utf-8")
    match = re.match(r"^#\s+(.+?)\s*$", index, re.MULTILINE)
    if not match:
        raise ValueError(f"No H1 in {project_dir / 'index.md'}")
    return match.group(1).strip()


def generate(project_dir: Path) -> str:
    lang = "ru" if "ru" in project_dir.parts else "en"
    title = project_title(project_dir)
    suffix = "всё вместе" if lang == "ru" else "all-in-one"
    intro = RU_INTRO if lang == "ru" else EN_INTRO
    toc = contents_section(lang, project_dir)
    adr_footer = (
        "## Architecture Decision Records\n\n"
        + ("См. " if lang == "ru" else "See ")
        + "[Architecture Decision Records](adr/index.md).\n"
    )
    return (
        f"# {title} — {suffix}\n\n"
        f"{intro}\n\n"
        f"{toc}\n"
        f"{INCLUDES}\n\n"
        f"{adr_footer}"
    )


def main() -> int:
    if len(sys.argv) < 2:
        print("Usage: python scripts/generate_all_in_one.py <project_dir> [...]", file=sys.stderr)
        return 2
    for arg in sys.argv[1:]:
        project_dir = Path(arg)
        out = project_dir / "all-in-one.md"
        out.write_text(generate(project_dir), encoding="utf-8", newline="\n")
        print(f"Wrote {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
