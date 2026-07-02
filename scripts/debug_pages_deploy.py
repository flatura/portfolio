#!/usr/bin/env python3
"""Local diagnostic for GitHub Pages deploy readiness. Writes NDJSON to debug-e7730a.log."""

from __future__ import annotations

import json
import subprocess
import sys
import time
from pathlib import Path

LOG_PATH = Path(__file__).resolve().parents[1] / "debug-e7730a.log"
SESSION_ID = "e7730a"


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


def site_stats(site_dir: Path) -> dict:
    files = list(site_dir.rglob("*"))
    file_paths = [p for p in files if p.is_file()]
    total_bytes = sum(p.stat().st_size for p in file_paths)
    return {
        "exists": site_dir.is_dir(),
        "file_count": len(file_paths),
        "size_mb": round(total_bytes / (1024 * 1024), 2),
        "has_index_html": (site_dir / "index.html").is_file(),
        "has_404_html": (site_dir / "404.html").is_file(),
    }


def read_site_url(mkdocs_yml: Path) -> str | None:
    for line in mkdocs_yml.read_text(encoding="utf-8").splitlines():
        if line.strip().startswith("site_url:"):
            return line.split(":", 1)[1].strip()
    return None


def git_remote() -> str | None:
    try:
        out = subprocess.check_output(["git", "remote", "get-url", "origin"], text=True).strip()
        return out
    except subprocess.CalledProcessError:
        return None


def workflow_checks(workflow: Path) -> dict:
    text = workflow.read_text(encoding="utf-8")
    return {
        "deploy_method": (
            "gh-pages-branch"
            if "peaceiris/actions-gh-pages" in text
            else "deployment-api"
        ),
        "uses_peaceiris_gh_pages": "peaceiris/actions-gh-pages" in text,
        "uses_deploy_pages": "actions/deploy-pages@" in text,
        "uses_configure_pages": "actions/configure-pages@" in text,
        "uses_upload_pages_artifact": "actions/upload-pages-artifact@" in text,
        "has_contents_write": "contents: write" in text,
        "has_concurrency": "concurrency:" in text,
    }


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    site_dir = root / "site"
    mkdocs_yml = root / "mkdocs.yml"
    workflow = root / ".github" / "workflows" / "pages.yml"

    # region agent log
    log("H3", "debug_pages_deploy.py:main", "artifact stats", site_stats(site_dir))
    # endregion

    # region agent log
    log(
        "H4",
        "debug_pages_deploy.py:main",
        "site_url vs remote",
        {"site_url": read_site_url(mkdocs_yml), "origin": git_remote()},
    )
    # endregion

    # region agent log
    log(
        "H13",
        "debug_pages_deploy.py:main",
        "deployment api failure pattern",
        {
            "symptom": "Deployment failed, try again later after artifact upload",
            "fix": "bypass deploy-pages API; push static site to gh-pages branch",
            "pages_source_required": "Settings -> Pages -> Deploy from branch gh-pages / root",
        },
    )
    # endregion

    # region agent log
    log("H5", "debug_pages_deploy.py:main", "workflow config flags", workflow_checks(workflow))
    # endregion

    # region agent log
    log(
        "H1",
        "debug_pages_deploy.py:main",
        "pages source checklist",
        {
            "note": "gh-pages branch deploy avoids Deployment API queue/failures",
            "check_repo_settings": [
                "Settings -> Pages -> Build and deployment -> Source: Deploy from a branch",
                "Branch: gh-pages, folder: / (root)",
                "Wait for first workflow run to create gh-pages branch before changing source",
            ],
        },
    )
    # endregion

    # region agent log
    log(
        "H2",
        "debug_pages_deploy.py:main",
        "queue/concurrency checklist",
        {
            "workflow_has_concurrency": "concurrency:" in workflow.read_text(encoding="utf-8"),
            "deploy_api_removed": "actions/deploy-pages@" not in workflow.read_text(encoding="utf-8"),
        },
    )
    # endregion

    print(json.dumps({"log_path": str(LOG_PATH), "site": site_stats(site_dir)}, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
