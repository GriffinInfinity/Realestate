"""Daily operating report for the Realestate pipeline.

Consumes the validator structured output and turns it into a compact operator
queue. It does not change source records.
"""

from __future__ import annotations

from collections import Counter
from datetime import date
from typing import Any

QUEUE_ORDER = ["verification", "compliance", "follow_up", "opportunity_review", "research", "revenue", "suppression"]

def build_daily_report(report: dict[str, Any], today: str | None = None) -> dict[str, Any]:
    today_date = date.fromisoformat(today) if today else date.today()
    issues = report.get("issues", [])
    queues = report.get("queues", {})
    by_queue = {name: sorted(set(queues.get(name, []))) for name in QUEUE_ORDER if queues.get(name)}
    severity = Counter(str(i.get("severity", "unknown")) for i in issues)
    return {
        "report_date": today_date.isoformat(),
        "records_checked": report.get("checked", 0),
        "valid": report.get("valid", False),
        "issue_counts": dict(severity),
        "queue_counts": {k: len(v) for k, v in by_queue.items()},
        "queues": by_queue,
        "priority_actions": [
            {"priority": 1, "queue": "compliance", "reason": "Resolve compliance gates before regulated activity."},
            {"priority": 2, "queue": "verification", "reason": "Resolve data-quality and qualification blockers."},
            {"priority": 3, "queue": "follow_up", "reason": "Complete documented next actions."},
            {"priority": 4, "queue": "opportunity_review", "reason": "Advance evidence-backed opportunities or move them to nurture/disqualified."},
            {"priority": 5, "queue": "revenue", "reason": "Complete evidence for realized revenue records."},
            {"priority": 6, "queue": "research", "reason": "Refresh sources and develop verified candidates."},
        ],
    }

def render_markdown(report: dict[str, Any]) -> str:
    lines = [
        f"# Realestate Daily Operating Report — {report['report_date']}",
        "",
        f"- Records checked: **{report['records_checked']}**",
        f"- Validation status: **{'PASS' if report['valid'] else 'REVIEW REQUIRED'}**",
        "",
        "## Queue Counts",
        "",
        "| Queue | Records |",
        "|---|---:|",
    ]
    for queue, count in report["queue_counts"].items():
        lines.append(f"| {queue} | {count} |")
    lines += ["", "## Priority Order", ""]
    for item in report["priority_actions"]:
        lines.append(f"{item['priority']}. **{item['queue']}** — {item['reason']}")
    return "\n".join(lines) + "\n"