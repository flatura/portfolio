"""Generate architecture-review, srs-pack, and demo-pack assembly pages."""

from __future__ import annotations

import re
from pathlib import Path

from assembly_toc import ADR_ANCHOR, ADR_LABEL, HEADING_OFFSET, AnchorRegistry, parse_headings

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
            "01-overview.md",
            "06-constraints.md",
            "12-security-and-access-model.md",
            "13-non-functional-requirements.md",
            "14-architecture.md",
            "15-key-decisions.md",
            "16-trade-offs.md",
            "17-failure-modes.md",
            "18-sizing-and-cost-notes.md",
            "19-roadmap.md",
        ],
        "include_adr": True,
        "en": {
            "suffix": "architecture review",
            "intro": (
                "This page assembles modules relevant to architecture review: constraints, "
                "security, non-functional requirements, architecture, decisions, trade-offs, "
                "failure modes, sizing, and roadmap."
            ),
            "index_label": "Architecture review",
            "index_desc": "constraints through roadmap for architecture review sessions",
        },
        "ru": {
            "suffix": "архитектурное ревью",
            "intro": (
                "Эта страница собирает модули для архитектурного ревью: ограничения, "
                "безопасность, нефункциональные требования, архитектура, решения, "
                "компромиссы, режимы отказа, оценка масштаба и дорожная карта."
            ),
            "index_label": "Архитектурное ревью",
            "index_desc": "от ограничений до дорожной карты для сессий архитектурного ревью",
        },
    },
    "srs-pack": {
        "modules": [
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
        ],
        "include_adr": False,
        "en": {
            "suffix": "SRS pack",
            "intro": (
                "This page assembles modules relevant to a software requirements specification: "
                "overview through non-functional requirements."
            ),
            "index_label": "SRS pack",
            "index_desc": "overview through non-functional requirements for SRS-style review",
        },
        "ru": {
            "suffix": "SRS-сборка",
            "intro": (
                "Эта страница собирает модули для спецификации требований к ПО: "
                "от обзора до нефункциональных требований."
            ),
            "index_label": "SRS-сборка",
            "index_desc": "от обзора до нефункциональных требований для ревью в формате SRS",
        },
    },
    "demo-pack": {
        "modules": [
            "01-overview.md",
            "07-role-and-responsibilities.md",
            "14-architecture.md",
            "15-key-decisions.md",
            "20-screenshots-and-demo.md",
            "21-what-this-demonstrates.md",
        ],
        "include_adr": False,
        "en": {
            "suffix": "demo pack",
            "intro": (
                "This page assembles modules relevant to demos and stakeholder presentations: "
                "overview, role, architecture highlights, key decisions, screenshots, and outcomes."
            ),
            "index_label": "Demo pack",
            "index_desc": "overview, role, architecture, decisions, screenshots, and outcomes",
        },
        "ru": {
            "suffix": "демо-сборка",
            "intro": (
                "Эта страница собирает модули для демо и презентаций стейкхолдерам: "
                "обзор, роль, архитектура, ключевые решения, скриншоты и результаты."
            ),
            "index_label": "Демо-сборка",
            "index_desc": "обзор, роль, архитектура, решения, скриншоты и результаты",
        },
    },
}


def pack_toc(lang: str, project_dir: Path, modules: list[str], include_adr: bool) -> str:
    heading = "## Contents" if lang == "en" else "## Содержание"
    registry = AnchorRegistry()
    registry.assign("Contents" if lang == "en" else "Содержание")
    lines = [heading, ""]

    for name in modules:
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
        lines.append(f"- [{module_title}](#{module_anchor})")

    if include_adr:
        lines.append(f"- [{ADR_LABEL}](#{ADR_ANCHOR})")
    lines.append("")
    return "\n".join(lines)


def pack_body(modules: list[str], include_adr: bool) -> str:
    lines = [f'{{% include-markdown "./{name}" heading-offset=1 %}}' for name in modules]
    if include_adr:
        lines.extend(
            [
                "",
                "## Architecture Decision Records",
                "",
                "See [Architecture Decision Records](adr/index.md).",
            ]
        )
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
        pack_toc(lang, project_dir, meta["modules"], meta["include_adr"]),
        pack_body(meta["modules"], meta["include_adr"]),
    ]
    return "\n".join(lines)


def update_index(index_path: Path, lang: str) -> None:
    text = index_path.read_text(encoding="utf-8")
    section = "## Document assemblies" if lang == "en" else "## Документные сборки"
    if section not in text:
        raise ValueError(f"Missing section in {index_path}")

    pack_lines = []
    if lang == "en":
        pack_lines = [
            "- [All-in-one](all-in-one.md) - all modules assembled for sequential reading and export",
            "- [Architecture review](architecture-review.md) - constraints through roadmap for architecture review sessions",
            "- [SRS pack](srs-pack.md) - overview through non-functional requirements for SRS-style review",
            "- [Demo pack](demo-pack.md) - overview, role, architecture, decisions, screenshots, and outcomes",
        ]
    else:
        pack_lines = [
            "- [Всё вместе](all-in-one.md) - все модули собраны для последовательного чтения и экспорта",
            "- [Архитектурное ревью](architecture-review.md) - от ограничений до дорожной карты для сессий архитектурного ревью",
            "- [SRS-сборка](srs-pack.md) - от обзора до нефункциональных требований для ревью в формате SRS",
            "- [Демо-сборка](demo-pack.md) - обзор, роль, архитектура, решения, скриншоты и результаты",
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
