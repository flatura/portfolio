#!/usr/bin/env python3
"""Detect include-markdown cycles and bloated HTML output."""

from __future__ import annotations

import json
import re
import time
from collections import defaultdict
from pathlib import Path

LOG_PATH = Path(__file__).resolve().parents[1] / "debug-e7730a.log"
SESSION_ID = "e7730a"
INCLUDE_RE = re.compile(r"""include-markdown\s+["'](?:\./)?([^"']+)["']""")


def log(hypothesis_id: str, location: str, message: str, data: dict, run_id: str = "pre-fix") -> None:
    entry = {
        "sessionId": SESSION_ID,
        "runId": run_id,
        "hypothesisId": hypothesis_id,
        "location": location,
        "message": message,
        "data": data,
        "timestamp": int(time.time() * 1000),
    }
    with LOG_PATH.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(entry, ensure_ascii=False) + "\n")


def build_graph(docs_root: Path) -> dict[str, set[str]]:
    graph: dict[str, set[str]] = defaultdict(set)
    for md in docs_root.rglob("*.md"):
        text = md.read_text(encoding="utf-8", errors="replace")
        for target in INCLUDE_RE.findall(text):
            graph[str(md)].add(str((md.parent / target).resolve()))
    return graph


def find_cycles(graph: dict[str, set[str]]) -> list[list[str]]:
    cycles: list[list[str]] = []
    visited: set[str] = set()
    stack: set[str] = set()
    path: list[str] = []

    def dfs(node: str) -> None:
        if node in stack:
            start = path.index(node)
            cycles.append(path[start:] + [node])
            return
        if node in visited:
            return
        visited.add(node)
        stack.add(node)
        path.append(node)
        for nbr in graph.get(node, ()):
            dfs(nbr)
        path.pop()
        stack.remove(node)

    for node in graph:
        dfs(node)
    return cycles


def html_stats(site_dir: Path) -> dict:
    if not site_dir.is_dir():
        return {"exists": False}
    html_files = list(site_dir.rglob("*.html"))
    sizes = sorted((p.stat().st_size for p in html_files), reverse=True)
    return {
        "exists": True,
        "html_count": len(html_files),
        "max_kb": round(sizes[0] / 1024, 1) if sizes else 0,
        "top5_kb": [round(s / 1024, 1) for s in sizes[:5]],
    }


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    graph = build_graph(root / "docs")
    cycles = find_cycles(graph)

    # region agent log
    log(
        "H9",
        "check_include_cycles.py:main",
        "include graph scan",
        {
            "nodes": len(graph),
            "edges": sum(len(v) for v in graph.values()),
            "cycle_count": len(cycles),
            "cycles": cycles[:10],
        },
    )
    # endregion

    # region agent log
    log("H9", "check_include_cycles.py:main", "html output sizes", html_stats(root / "site"))
    # endregion

    print(json.dumps({"cycles": len(cycles), "html": html_stats(root / "site")}, indent=2))
    return 1 if cycles else 0


if __name__ == "__main__":
    raise SystemExit(main())
