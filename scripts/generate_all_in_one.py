"""Generate all-in-one.md for a structured project directory."""

from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from assembly_toc import ALL_IN_ONE_MODULES, contents_section  # noqa: E402

INCLUDES = "\n".join(
    f'{{% include-markdown "./{name}" heading-offset=1 %}}' for name in ALL_IN_ONE_MODULES
)

EN_INTRO = (
    "This page is assembled from compact project documentation sections. "
    "Individual section files remain the source of truth; this page is for sequential reading, "
    "review, and PDF-style export."
)
RU_INTRO = (
    "Эта страница собирается из компактных разделов проектной документации. "
    "Отдельные файлы разделов остаются источником истины; эта страница предназначена "
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
    toc = contents_section(lang, project_dir, include_adr=True)
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
