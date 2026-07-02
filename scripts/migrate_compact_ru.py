"""Migrate docs/ru/projects/* from 21-file to compact structure."""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LANG = "ru"
PROJECTS = [
    "ai_oip",
    "serverless_transcriber",
    "enterprise_gis",
    "fastmbo",
    "polyline-mechanic",
    "graph-mechanic",
    "expendit",
]

COMPACT_SPECS: list[tuple[str, str, list[str], bool]] = [
    ("01-overview.md", "Обзор", ["01-overview.md"], True),
    ("02-context-and-problem.md", "Контекст и проблема", ["02-context.md", "03-problem.md"], False),
    (
        "03-goals-requirements-and-constraints.md",
        "Цели, требования и ограничения",
        ["04-goals-and-non-goals.md", "05-requirements.md", "06-constraints.md"],
        False,
    ),
    ("04-role-and-responsibilities.md", "Роль и обязанности", ["07-role-and-responsibilities.md"], True),
    (
        "05-system-model.md",
        "Модель системы",
        ["08-domain-model.md", "09-data-model.md", "10-api-contracts.md"],
        False,
    ),
    (
        "06-architecture-and-integrations.md",
        "Архитектура и интеграции",
        ["14-architecture.md", "11-integration-flows.md"],
        False,
    ),
    (
        "07-security-quality-and-operations.md",
        "Безопасность, качество и эксплуатация",
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
        "Решения, компромиссы и риски",
        ["15-key-decisions.md", "16-trade-offs.md"],
        False,
    ),
    (
        "09-roadmap-and-demonstration.md",
        "Дорожная карта и демонстрация",
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
    "../15-key-decisions.md": "../08-decisions-trade-offs-and-risks.md#_2",
    "../16-trade-offs.md": "../08-decisions-trade-offs-and-risks.md#_3",
    "07-role-and-responsibilities.md": "04-role-and-responsibilities.md",
    "15-key-decisions.md": "08-decisions-trade-offs-and-risks.md#_2",
    "16-trade-offs.md": "08-decisions-trade-offs-and-risks.md#_3",
    "02-context.md": "02-context-and-problem.md",
    "03-problem.md": "02-context-and-problem.md",
    "04-goals-and-non-goals.md": "03-goals-requirements-and-constraints.md",
    "05-requirements.md": "03-goals-requirements-and-constraints.md",
    "06-constraints.md": "03-goals-requirements-and-constraints.md",
    "08-domain-model.md": "05-system-model.md",
    "09-data-model.md": "05-system-model.md",
    "10-api-contracts.md": "05-system-model.md",
    "11-integration-flows.md": "06-architecture-and-integrations.md",
    "12-security-and-access-model.md": "07-security-quality-and-operations.md",
    "13-non-functional-requirements.md": "07-security-quality-and-operations.md",
    "14-architecture.md": "06-architecture-and-integrations.md",
    "17-failure-modes.md": "07-security-quality-and-operations.md",
    "18-sizing-and-cost-notes.md": "07-security-quality-and-operations.md",
    "19-roadmap.md": "09-roadmap-and-demonstration.md",
    "20-screenshots-and-demo.md": "09-roadmap-and-demonstration.md",
    "21-what-this-demonstrates.md": "09-roadmap-and-demonstration.md",
}

FULL_STRUCTURE = """## Полная структура

- [Краткое описание](summary.md)
- [01 — Обзор](01-overview.md)
- [02 — Контекст и проблема](02-context-and-problem.md)
- [03 — Цели, требования и ограничения](03-goals-requirements-and-constraints.md)
- [04 — Роль и обязанности](04-role-and-responsibilities.md)
- [05 — Модель системы](05-system-model.md)
- [06 — Архитектура и интеграции](06-architecture-and-integrations.md)
- [07 — Безопасность, качество и эксплуатация](07-security-quality-and-operations.md)
- [08 — Решения, компромиссы и риски](08-decisions-trade-offs-and-risks.md)
- [09 — Дорожная карта и демонстрация](09-roadmap-and-demonstration.md)
- [Architecture Decision Records](adr/index.md)
"""


def read(path: Path) -> str:
    if path.is_file():
        return path.read_text(encoding="utf-8")
    return ""


def rewrite_links(text: str) -> str:
    def replace_link(match: re.Match[str]) -> str:
        target = match.group(1)
        base = target.split("#", 1)[0]
        anchor = target[len(base) :] if "#" in target else ""
        if base.startswith("./"):
            key = base[2:]
            prefix = "./"
        elif base.startswith("../"):
            key = base
            prefix = ""
        else:
            key = base
            prefix = ""
        new_base = LINK_REWRITES.get(key, LINK_REWRITES.get(base, base))
        if new_base == base:
            return match.group(0)
        if prefix == "./" and not new_base.startswith("../"):
            new_target = f"./{new_base}"
        else:
            new_target = new_base
        if anchor and "#" not in new_base:
            new_target += anchor
        return f"]({new_target})"

    return re.sub(r"\]\(([^)]+)\)", replace_link, text)


def promote_h2_to_h1(text: str) -> str:
    lines = text.splitlines()
    if lines and lines[0].startswith("## "):
        lines[0] = "# " + lines[0][3:]
    return "\n".join(lines).strip() + "\n"


def demote_h1_to_h2(text: str) -> str:
    lines = text.splitlines()
    if lines and lines[0].startswith("# "):
        lines[0] = "## " + lines[0][2:]
    return "\n".join(lines).strip() + "\n"


def merge_sources(project: Path, title: str, sources: list[str], promote_single: bool) -> str:
    bodies: list[str] = []
    for name in sources:
        body = read(project / name).strip()
        if body:
            bodies.append(body)

    if not bodies:
        return f"# {title}\n\n*Содержимое раздела пока не задокументировано.*\n"

    if promote_single and len(sources) == 1:
        body = bodies[0]
        if body.startswith("## "):
            body = promote_h2_to_h1(body)
        return rewrite_links(body)

    parts = [f"# {title}\n"]
    for body in bodies:
        if body.startswith("# "):
            body = demote_h1_to_h2(body)
        parts.append(rewrite_links(body))
    return "\n".join(parts).strip() + "\n"


def extract_demonstrates(project: Path, source: str | None = None) -> str:
    demonstrates = source if source is not None else read(project / "21-what-this-demonstrates.md")
    demonstrates = demonstrates.strip()
    if not demonstrates:
        return ""
    demonstrates = re.sub(r"^#\s+.+\n+", "", demonstrates)
    demonstrates = re.sub(r"^##\s+.+\n+", "", demonstrates, count=1)
    demonstrates = demonstrates.strip()
    if demonstrates.startswith("#"):
        return ""
    return demonstrates


def create_summary(project: Path, index_source: str | None = None) -> str:
    index = index_source if index_source is not None else read(project / "index.md")
    header_match = re.match(r"^#\s+[^\n]+\n+(.*?)(?=\n## )", index, re.DOTALL)
    header_block = header_match.group(1) if header_match else ""

    metadata: dict[str, str] = {}
    value_paragraphs: list[str] = []
    for line in header_block.splitlines():
        meta = re.match(r"\*\*(.+?):\*\*\s*(.+)", line)
        if meta:
            metadata[meta.group(1).strip()] = meta.group(2).strip()
        elif line.strip() and not line.startswith("**"):
            value_paragraphs.append(line.strip())

    status = metadata.get("Статус") or metadata.get("Status") or "TBD"
    role = metadata.get("Роль") or metadata.get("Role") or "TBD"

    if "Стек" in metadata:
        stack = metadata["Стек"]
    elif "Stack" in metadata:
        stack = metadata["Stack"]
    else:
        stack_keys = ["Тип", "Реализация", "Домен", "NDA", "Масштаб", "Период", "Происхождение"]
        stack_parts = [f"{k}: {metadata[k]}" for k in stack_keys if k in metadata]
        stack = "; ".join(stack_parts) if stack_parts else "TBD"

    value = "\n\n".join(value_paragraphs) if value_paragraphs else "TBD"
    demo_section = extract_demonstrates(project, read(project / "21-what-this-demonstrates.md"))

    lines = [
        "# Краткое описание",
        "",
        "## Статус",
        "",
        status,
        "",
        "## Роль",
        "",
        role,
        "",
        "## Стек",
        "",
        stack,
        "",
        "## Ценность проекта",
        "",
        value,
    ]
    if demo_section:
        lines.extend(["", "## Что демонстрирует", "", demo_section])
    lines.append("")
    return "\n".join(lines)


def extract_quick_path(index: str) -> str:
    match = re.search(r"## Быстрый маршрут\n\n(.*?)(?=\n## )", index, re.DOTALL)
    if not match:
        return ""
    path = rewrite_links(match.group(1).strip())
    seen_targets: set[str] = set()
    deduped: list[str] = []
    for line in path.splitlines():
        link = re.search(r"\]\(([^)]+)\)", line)
        if link:
            target = link.group(1).split("#", 1)[0]
            if target in seen_targets and target not in ("all-in-one.md", "./all-in-one.md"):
                continue
            seen_targets.add(target)
        deduped.append(line)
    renumbered: list[str] = []
    for i, line in enumerate(deduped, start=1):
        renumbered.append(re.sub(r"^\d+\.", f"{i}.", line))
    return "\n".join(renumbered)


def extract_extra_sections(index: str) -> str:
    match = re.search(r"## Полная структура\n\n.*?(?=\n## |\Z)", index, re.DOTALL)
    if match:
        tail = index[match.end() :].strip()
    else:
        table_end = re.search(r"## Все разделы\n\n.*?(?=\n## |\Z)", index, re.DOTALL)
        tail = index[table_end.end() :].strip() if table_end else ""
    known = {
        "## Быстрый маршрут",
        "## Документные сборки",
        "## Все разделы",
        "## Полная структура",
    }
    extras: list[str] = []
    for section in re.split(r"(?=^## )", tail, flags=re.MULTILINE):
        section = section.strip()
        if not section:
            continue
        heading = section.splitlines()[0]
        if heading in known:
            continue
        extras.append(section)
    return "\n\n".join(extras)


def create_index(project: Path, title: str, index_source: str | None = None) -> str:
    old_index = index_source if index_source is not None else read(project / "index.md")
    quick_path = extract_quick_path(old_index)
    if not quick_path:
        quick_path = (
            "1. [Обзор](01-overview.md) — краткое описание продукта и стек\n"
            "2. [Контекст и проблема](02-context-and-problem.md) — предпосылки и формулировка проблемы\n"
            "3. [Архитектура и интеграции](06-architecture-and-integrations.md) — архитектура и потоки\n"
            "4. [Цели, требования и ограничения](03-goals-requirements-and-constraints.md) — ключевые возможности\n"
            "5. [Всё вместе](all-in-one.md) — полный кейс на одной странице"
        )
    extras = extract_extra_sections(old_index)
    body = f"""# {title}

{{% include-markdown "./summary.md" heading-offset=1 %}}

## Быстрый маршрут

{quick_path}

## Документные сборки

- [Всё вместе](all-in-one.md) - все разделы собраны для последовательного чтения и экспорта
- [Архитектурное ревью](architecture-review.md) - от целей до решений для сессий архитектурного ревью
- [SRS-сборка](srs-pack.md) - от контекста до эксплуатации для ревью в формате SRS
- [Демо-сборка](demo-pack.md) - обзор, роль, архитектура, решения, дорожная карта и демонстрация

{FULL_STRUCTURE}"""
    if extras:
        body += "\n" + extras + "\n"
    return body


def update_adr_index(project: Path) -> None:
    path = project / "adr" / "index.md"
    if not path.is_file():
        return
    text = rewrite_links(read(path))
    path.write_text(text, encoding="utf-8", newline="\n")


def append_adr_link_to_decisions(content: str) -> str:
    if "adr/index.md" in content:
        return content
    return content.rstrip() + "\n\nСм. также [Architecture Decision Records](adr/index.md).\n"


def migrate_project(slug: str) -> None:
    project = ROOT / "docs" / LANG / "projects" / slug
    if not project.is_dir():
        raise FileNotFoundError(project)

    title_match = re.match(r"^#\s+(.+?)\s*$", read(project / "index.md"), re.MULTILINE)
    title = title_match.group(1).strip() if title_match else slug

    (project / "summary.md").write_text(create_summary(project), encoding="utf-8", newline="\n")

    for target, section_title, sources, promote in COMPACT_SPECS:
        content = merge_sources(project, section_title, sources, promote)
        if target == "08-decisions-trade-offs-and-risks.md":
            content = append_adr_link_to_decisions(content)
        (project / target).write_text(content, encoding="utf-8", newline="\n")

    (project / "index.md").write_text(create_index(project, title), encoding="utf-8", newline="\n")
    update_adr_index(project)

    for name in OLD_GRANULAR:
        path = project / name
        if path.is_file():
            path.unlink()

    subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "generate_all_in_one.py"), str(project)],
        check=True,
    )

    sys.path.insert(0, str(ROOT / "scripts"))
    from generate_packs import PACKS, render_pack, update_index  # noqa: E402

    for pack_name, meta in PACKS.items():
        content = render_pack(project, LANG, pack_name, meta)
        (project / f"{pack_name}.md").write_text(content, encoding="utf-8", newline="\n")
    update_index(project / "index.md", LANG)

    print(f"Migrated {project}")


def main() -> int:
    targets = sys.argv[1:] if len(sys.argv) > 1 else PROJECTS
    for slug in targets:
        migrate_project(slug)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
