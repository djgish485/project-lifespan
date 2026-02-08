#!/usr/bin/env python3
"""Render debates/backlog.yaml into docs/debates/backlog.md."""

from pathlib import Path
import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
BACKLOG_YAML = REPO_ROOT / "debates" / "backlog.yaml"
OUTPUT_MD = REPO_ROOT / "docs" / "debates" / "backlog.md"

TYPE_LABELS = {
    "measurement-gap": "Measurement Gap",
    "bridge-assumption": "Bridge Assumption",
    "missing-severe-test": "Missing Severe Test",
    "definitional-escape": "Definitional Escape",
}

STATUS_ICONS = {
    "open": "Open",
    "in-progress": "In Progress",
    "resolved": "Resolved",
}


def render():
    items = yaml.safe_load(BACKLOG_YAML.read_text())
    open_items = [i for i in items if i["status"] == "open"]
    in_progress = [i for i in items if i["status"] == "in-progress"]
    resolved = [i for i in items if i["status"] == "resolved"]

    lines = [
        "---",
        "title: Open Criticisms Backlog",
        "---",
        "",
        "# Open Criticisms Backlog",
        "",
        "Surviving criticisms extracted from debate judge verdicts. Each item is tracked",
        "until resolved by new evidence, experiment results, or theoretical revision.",
        "",
        f"**Total:** {len(items)} | **Open:** {len(open_items)} | "
        f"**In Progress:** {len(in_progress)} | **Resolved:** {len(resolved)}",
        "",
        "**See also:** [Research Agenda](../experiments/research_agenda.md) for the decisive experiments that would resolve many of these.",
        "",
        "---",
        "",
    ]

    # Group by type
    by_type: dict[str, list] = {}
    for item in open_items + in_progress:
        t = item["type"]
        by_type.setdefault(t, []).append(item)

    for type_key, type_label in TYPE_LABELS.items():
        group = by_type.get(type_key, [])
        if not group:
            continue
        lines.append(f"## {type_label} ({len(group)})")
        lines.append("")
        for item in group:
            theories = ", ".join(item["theories"])
            status = STATUS_ICONS.get(item["status"], item["status"])
            lines.append(f"### `{item['id']}`")
            lines.append("")
            lines.append(f"**Theories:** {theories}  ")
            lines.append(f"**Status:** {status}  ")
            lines.append(f"**Statement:** {item['statement']}")
            lines.append("")
            if item.get("born_from"):
                # Convert file path to relative link
                debate_file = item["born_from"].split("/")[-1]
                lines.append(f"**Source:** [{debate_file}]({debate_file})")
            if item.get("resolution_path"):
                path = item["resolution_path"]
                # Convert docs/ path to relative
                if path.startswith("docs/experiments/"):
                    rel = "../experiments/" + path.split("docs/experiments/")[1]
                elif path.startswith("docs/debates/"):
                    rel = path.split("docs/debates/")[1]
                else:
                    rel = path
                lines.append(f"  ")
                lines.append(f"**Resolution path:** [{path}]({rel})")
            lines.append("")
            lines.append("---")
            lines.append("")

    if resolved:
        lines.append("## Resolved")
        lines.append("")
        for item in resolved:
            theories = ", ".join(item["theories"])
            kind = item.get("resolution_kind", "unknown")
            kind_label = {"spec": "Spec-resolved (definitional fix, no new data)", "evidence": "Evidence-resolved (severe test produced data)"}.get(kind, kind)
            lines.append(f"### ~~`{item['id']}`~~")
            lines.append("")
            lines.append(f"**Theories:** {theories}  ")
            lines.append(f"**Statement:** {item['statement']}  ")
            lines.append(f"**Resolution kind:** {kind_label}  ")
            lines.append(f"**Resolution:** {item.get('resolution_evidence', 'N/A')}")
            lines.append("")
            lines.append("---")
            lines.append("")

    OUTPUT_MD.write_text("\n".join(lines))
    print(f"Rendered {len(items)} items to {OUTPUT_MD}")


if __name__ == "__main__":
    render()
