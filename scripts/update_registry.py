#!/usr/bin/env python3
"""
Auto-generate the Claims Doctor Document Registry (CD-STR-000)
from YAML frontmatter in all markdown files.

Scans the repo for .md files, reads their YAML frontmatter,
deduplicates by doc_id (keeping highest version), and rebuilds
sections 04 (Document Register) and 05 (Statistics) in the
registry file.
"""

import re
import sys
from collections import defaultdict
from pathlib import Path

import yaml

# ── Category metadata (order defines table output order) ─────────────────────

CATEGORIES = {
    "STR": "Strategy & Planning",
    "FIN": "Financial",
    "MKT": "Marketing & Growth",
    "SAL": "Sales & Partnerships",
    "OPS": "Operations & Service Delivery",
    "GOV": "Clinical Governance",
    "LEG": "Compliance & Legal",
    "HR": "HR & Team",
    "PAT": "Patient-Facing",
    "RPT": "Reporting & Measurement",
    "BRD": "Brand",
}

CATEGORY_ORDER = list(CATEGORIES.keys())

REGISTRY_DOC_ID = "CD-STR-000"
TEMPLATE_PREFIX = "CD-TEMPLATE"
SKIP_PREFIXES = ("README", "LICENSE", "CHANGELOG", ".")

START_MARKER = "<!-- AUTO-GENERATED:START -->"
END_MARKER = "<!-- AUTO-GENERATED:END -->"


# ── Helpers ──────────────────────────────────────────────────────────────────


def parse_frontmatter(filepath: Path) -> dict | None:
    """Extract YAML frontmatter from a markdown file."""
    try:
        text = filepath.read_text(encoding="utf-8")
    except (UnicodeDecodeError, OSError):
        return None
    match = re.match(r"^---\s*\n(.*?)\n---", text, re.DOTALL)
    if not match:
        return None
    try:
        return yaml.safe_load(match.group(1))
    except yaml.YAMLError:
        return None


def version_tuple(version) -> tuple:
    """Convert a version string/number to a comparable tuple.
    e.g. '1.0' -> (1, 0), 0.1 -> (0, 1), None -> (-1, -1)
    """
    if version is None:
        return (-1, -1)
    parts = str(version).split(".")
    try:
        return tuple(int(p) for p in parts)
    except ValueError:
        return (-1, -1)


def deduplicate_docs(docs: list[dict]) -> list[dict]:
    """Keep only the highest version per doc_id."""
    best: dict[str, dict] = {}
    for doc in docs:
        doc_id = doc.get("doc_id", "")
        if doc_id not in best or version_tuple(doc.get("version")) > version_tuple(
            best[doc_id].get("version")
        ):
            best[doc_id] = doc
    return list(best.values())


def get_category(doc_id: str) -> str | None:
    """Extract category code from a doc_id like CD-GOV-001."""
    parts = doc_id.split("-")
    return parts[1] if len(parts) >= 3 else None


def fmt_version(version) -> str:
    if version is None:
        return "—"
    return str(version)


def fmt_deps(deps) -> str:
    if not deps:
        return "—"
    if isinstance(deps, list):
        return ", ".join(str(d) for d in deps) if deps else "—"
    return str(deps)


# ── Table builders ───────────────────────────────────────────────────────────


def build_category_table(docs: list[dict]) -> str:
    rows = [
        "| Doc ID | Title | Version | Status | Visibility | Owner | Dependencies |",
        "|--------|-------|---------|--------|------------|-------|-------------|",
    ]
    for doc in sorted(docs, key=lambda d: d.get("doc_id", "")):
        rows.append(
            f"| {doc.get('doc_id', '—')} "
            f"| {doc.get('title', '—')} "
            f"| {fmt_version(doc.get('version'))} "
            f"| {doc.get('status', '—')} "
            f"| {doc.get('visibility', '—')} "
            f"| {doc.get('owner', '—')} "
            f"| {fmt_deps(doc.get('dependencies'))} |"
        )
    return "\n".join(rows)


def build_statistics(all_docs: list[dict]) -> str:
    status_counts: dict[str, int] = defaultdict(int)
    visibility_counts: dict[str, int] = defaultdict(int)

    for doc in all_docs:
        status_counts[doc.get("status", "UNKNOWN")] += 1
        visibility_counts[doc.get("visibility", "UNKNOWN")] += 1

    rows = [
        "| Metric | Count |",
        "|--------|-------|",
        f"| Total documents registered | {len(all_docs)} |",
    ]

    for status in ["ACTIVE", "DRAFT", "UNDER REVIEW", "SUPERSEDED", "RETIRED"]:
        count = status_counts.get(status, 0)
        if count > 0:
            rows.append(f"| {status} | {count} |")

    for vis in ["EXTERNAL", "INTERNAL"]:
        count = visibility_counts.get(vis, 0)
        if count > 0:
            rows.append(f"| {vis} visibility | {count} |")

    return "\n".join(rows)


# ── Main generation ──────────────────────────────────────────────────────────


def generate_section(docs_by_category: dict, all_docs: list[dict]) -> str:
    """Generate the full content between the AUTO-GENERATED markers."""
    lines = [START_MARKER, "", "## 04 Document Register", ""]

    for cat_code in CATEGORY_ORDER:
        if cat_code not in docs_by_category:
            continue
        cat_name = CATEGORIES.get(cat_code, cat_code)
        lines.append(f"### {cat_code} — {cat_name}")
        lines.append("")
        lines.append(build_category_table(docs_by_category[cat_code]))
        lines.append("")

    lines.extend(["---", "", "## 05 Statistics", ""])
    lines.append(build_statistics(all_docs))
    lines.append("")
    lines.append(END_MARKER)

    return "\n".join(lines)


def main() -> None:
    repo_root = Path(__file__).resolve().parent.parent
    registry_path: Path | None = None
    raw_docs: list[dict] = []

    # Scan all markdown files
    for md_file in sorted(repo_root.rglob("*.md")):
        if any(md_file.name.startswith(p) for p in SKIP_PREFIXES):
            continue

        fm = parse_frontmatter(md_file)
        if not fm or "doc_id" not in fm:
            continue

        doc_id = fm["doc_id"]

        # Skip templates
        if str(doc_id).startswith(TEMPLATE_PREFIX):
            continue

        # Track registry location
        if doc_id == REGISTRY_DOC_ID:
            registry_path = md_file

        raw_docs.append(fm)

    if not registry_path:
        print(f"ERROR: Registry file ({REGISTRY_DOC_ID}) not found in repo.")
        sys.exit(1)

    # Deduplicate — keep only highest version per doc_id
    all_docs = deduplicate_docs(raw_docs)

    # Group by category
    docs_by_category: dict[str, list[dict]] = defaultdict(list)
    for doc in all_docs:
        category = get_category(doc.get("doc_id", ""))
        if category:
            docs_by_category[category].append(doc)

    # Read existing registry content
    content = registry_path.read_text(encoding="utf-8")

    if START_MARKER not in content or END_MARKER not in content:
        print(
            f"ERROR: Markers not found in registry.\n"
            f"Add these lines to CD-STR-000 around sections 04 and 05:\n"
            f"  {START_MARKER}\n"
            f"  ... (sections 04 & 05) ...\n"
            f"  {END_MARKER}"
        )
        sys.exit(1)

    # Generate and replace
    new_section = generate_section(docs_by_category, all_docs)
    pattern = re.compile(
        re.escape(START_MARKER) + r".*?" + re.escape(END_MARKER),
        re.DOTALL,
    )
    updated = pattern.sub(new_section, content)

    if updated != content:
        registry_path.write_text(updated, encoding="utf-8")
        print(
            f"Registry updated: {len(all_docs)} documents "
            f"across {len(docs_by_category)} categories."
        )
    else:
        print("Registry already up to date. No changes.")


if __name__ == "__main__":
    main()
