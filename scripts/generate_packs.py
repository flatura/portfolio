"""Generate architecture-review, srs-pack, and demo-pack assembly pages."""

from __future__ import annotations

import re
from pathlib import Path

from assembly_toc import SUMMARY, contents_section

ROOT = Path(__file__).resolve().parents[1]
PROJECTS = [
    "ai_oip",
    "botanical",
    "serverless_transcriber",
    "enterprise_gis",
    "fastmbo",
    "polyline-mechanic",
    "graph-mechanic",
    "expendit",
]

PACKS = {
    "architecture-review": {
        "modules": [
            SUMMARY,
            "03-goals-requirements-and-constraints.md",
            "05-system-model.md",
            "06-architecture-and-integrations.md",
            "07-security-quality-and-operations.md",
            "08-decisions-trade-offs-and-risks.md",
        ],
        "en": {
            "suffix": "architecture review",
            "intro": (
                "This page assembles sections relevant to architecture review: "
                "goals, requirements, and constraints; system model; architecture and integrations; "
                "security, quality, and operations; and decisions, trade-offs, and risks."
            ),
            "index_desc": (
                "goals through decisions for architecture review sessions"
            ),
        },
        "ru": {
            "suffix": "архитектурное ревью",
            "intro": (
                "Эта страница собирает разделы для архитектурного ревью: "
                "цели, требования и ограничения; модель системы; архитектура и интеграции; "
                "безопасность, качество и эксплуатация; решения, компромиссы и риски."
            ),
            "index_desc": (
                "от целей до решений для сессий архитектурного ревью"
            ),
        },
    },
    "srs-pack": {
        "modules": [
            SUMMARY,
            "02-context-and-problem.md",
            "03-goals-requirements-and-constraints.md",
            "04-role-and-responsibilities.md",
            "05-system-model.md",
            "06-architecture-and-integrations.md",
            "07-security-quality-and-operations.md",
        ],
        "en": {
            "suffix": "SRS pack",
            "intro": (
                "This page assembles sections relevant to a software requirements specification: "
                "context and problem through security, quality, and operations."
            ),
            "index_desc": (
                "context through operations for SRS-style review"
            ),
        },
        "ru": {
            "suffix": "SRS-сборка",
            "intro": (
                "Эта страница собирает разделы для спецификации требований к ПО: "
                "от контекста и проблемы до безопасности, качества и эксплуатации."
            ),
            "index_desc": (
                "от контекста до эксплуатации для ревью в формате SRS"
            ),
        },
    },
    "demo-pack": {
        "modules": [
            SUMMARY,
            "01-overview.md",
            "04-role-and-responsibilities.md",
            "06-architecture-and-integrations.md",
            "08-decisions-trade-offs-and-risks.md",
            "09-roadmap-and-demonstration.md",
        ],
        "en": {
            "suffix": "demo pack",
            "intro": (
                "This page assembles sections relevant to demos and stakeholder presentations: "
                "overview, role, architecture, decisions, roadmap, and demonstration."
            ),
            "index_desc": (
                "overview, role, architecture, decisions, roadmap, and demonstration"
            ),
        },
        "ru": {
            "suffix": "демо-сборка",
            "intro": (
                "Эта страница собирает разделы для демо и презентаций стейкхолдерам: "
                "обзор, роль, архитектура, решения, дорожная карта и демонстрация."
            ),
            "index_desc": (
                "обзор, роль, архитектура, решения, дорожная карта и демонстрация"
            ),
        },
    },
}


def pack_body(modules: list[str]) -> str:
    lines = [f'{{% include-markdown "./{name}" heading-offset=1 %}}' for name in modules]
    lines.append("")
    return "\n".join(lines)


def project_title(index_path: Path) -> str:
    for line in index_path.read_text(encoding="utf-8").splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    raise ValueError(f"No H1 in {index_path}")


def render_pack(project_dir: Path, lang: str, pack_name: str, meta: dict) -> str:
    pack_meta = meta[lang]
    title = project_title(project_dir / "index.md")
    lines = [
        f"# {title} — {pack_meta['suffix']}",
        "",
        pack_meta["intro"],
        "",
        contents_section(lang, project_dir, meta["modules"]),
        pack_body(meta["modules"]),
    ]
    return "\n".join(lines)


def update_index(index_path: Path, lang: str) -> None:
    text = index_path.read_text(encoding="utf-8")
    section = "## Document assemblies" if lang == "en" else "## Документные сборки"
    if section not in text:
        raise ValueError(f"Missing section in {index_path}")

    if lang == "en":
        pack_lines = [
            "- [All-in-one](all-in-one.md) - all sections assembled for sequential reading and export",
            f"- [Architecture review](architecture-review.md) - {PACKS['architecture-review']['en']['index_desc']}",
            f"- [SRS pack](srs-pack.md) - {PACKS['srs-pack']['en']['index_desc']}",
            f"- [Demo pack](demo-pack.md) - {PACKS['demo-pack']['en']['index_desc']}",
        ]
    else:
        pack_lines = [
            "- [Всё вместе](all-in-one.md) - все разделы собраны для последовательного чтения и экспорта",
            f"- [Архитектурное ревью](architecture-review.md) - {PACKS['architecture-review']['ru']['index_desc']}",
            f"- [SRS-сборка](srs-pack.md) - {PACKS['srs-pack']['ru']['index_desc']}",
            f"- [Демо-сборка](demo-pack.md) - {PACKS['demo-pack']['ru']['index_desc']}",
        ]

    block = section + "\n\n" + "\n".join(pack_lines) + "\n"
    text = re.sub(
        rf"{re.escape(section)}\n\n(?:- .+\n)+",
        block,
        text,
        count=1,
    )
    index_path.write_text(text, encoding="utf-8")


def main() -> None:
    for lang in ("en", "ru"):
        for project in PROJECTS:
            project_dir = ROOT / "docs" / lang / "projects" / project
            for pack_name, meta in PACKS.items():
                content = render_pack(project_dir, lang, pack_name, meta)
                (project_dir / f"{pack_name}.md").write_text(content, encoding="utf-8")
            update_index(project_dir / "index.md", lang)
            print(f"ok {lang}/{project}")


if __name__ == "__main__":
    main()
