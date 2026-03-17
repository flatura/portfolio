# Verification: Internal links and /portfolio/assets/ images (both locales)

**Date:** 2025-03-17  
**Scope:** Internal links in `docs/en/` and `docs/ru/`, and `/portfolio/assets/` image references.

## Internal links

### Russian locale (`docs/ru/`)

| Source | Link | Resolved target | Status |
|--------|------|-----------------|--------|
| `index.md` | `projects/gis_bi_1.md` | `docs/ru/projects/gis_bi_1.md` | OK |
| `index.md` | `projects/fastmbo.md` | `docs/ru/projects/fastmbo.md` | OK |
| `index.md` | `projects/fastmbo-adr.md` | `docs/ru/projects/fastmbo-adr.md` | OK |
| `index.md` | `projects/graph-mechanic.md` | `docs/ru/projects/graph-mechanic.md` | OK |
| `projects/fastmbo.md` | `fastmbo-adr.md` | `docs/ru/projects/fastmbo-adr.md` | OK |

All linked target files exist. Relative links are correct within `docs/ru/`.

### English locale (`docs/en/`)

- No internal doc-to-doc links (only cross-locale links to `/ru/` and `/ru/projects/<name>/`).
- Cross-locale links point to the Russian site paths and are valid for mkdocs-static-i18n (e.g. `/ru/`, `/ru/projects/fastmbo/`).

## /portfolio/assets/ images

- **Used in:** `docs/ru/projects/graph-mechanic.md`, `docs/ru/projects/polyline-mechanic.md`.
- **Paths:** Absolute `/portfolio/assets/graphmechanic/ui/v1/*.webp` (5 images per file).
- **Resolution:** With `site_url: https://flatura.github.io/portfolio`, these resolve to `https://flatura.github.io/portfolio/assets/graphmechanic/...` from any page.
- **Both locales:** Same resolution from `/` (en) and `/ru/` (ru); no locale-specific path changes needed.

## Conclusion

- **Internal links:** Verified; all targets exist and relative links are correct in both locales.
- **Assets:** Verified; `/portfolio/assets/` references are absolute and resolve identically for en and ru.

To re-verify with MkDocs (e.g. in CI):  
`pip install mkdocs mkdocs-material ... mkdocs-static-i18n[material]` then  
`mkdocs build --strict --site-dir ./site`
