#!/usr/bin/env python3
"""
Compliance Report Generator
----------------------------
Reads the risk register and produces a markdown report.
Run: python reporting/generate_report.py
"""

import json
import os
from datetime import datetime


def load_risks():
    path = os.path.join(os.path.dirname(__file__), "..", "risk", "risk_register.json")
    with open(path) as f:
        return json.load(f)


def score_level(score):
    if score >= 17: return "Critical"
    if score >= 10: return "High"
    if score >= 5:  return "Medium"
    return "Low"


def build_report(risks, today):
    open_risks = [r for r in risks if r.get("status", "open") == "open"]
    closed     = [r for r in risks if r.get("status") == "closed"]
    sorted_r   = sorted(open_risks, key=lambda r: r["score"], reverse=True)

    lines = []
    lines.append(f"# Security Status Report -- {today}")
    lines.append(f"Frameworks: ISO 27001:2022 / NIST CSF 2.0 / NSM Grunnprinsipper")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    lines.append(f"- Open risks: {len(open_risks)}")
    lines.append(f"- Critical: {sum(1 for r in open_risks if score_level(r['score']) == 'Critical')}")
    lines.append(f"- High: {sum(1 for r in open_risks if score_level(r['score']) == 'High')}")
    lines.append(f"- Closed this period: {len(closed)}")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## Risk register")
    lines.append("")
    lines.append("| ID | Risk | Score | Level | Owner |")
    lines.append("|---|---|---|---|---|")

    for r in sorted_r:
        lvl = score_level(r["score"])
        lines.append(f"| {r['id']} | {r['title']} | {r['score']} | {lvl} | {r['owner']} |")

    if closed:
        lines.append("")
        lines.append("### Closed")
        for r in closed:
            lines.append(f"- ~~{r['id']} -- {r['title']}~~")

    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## 2026 regulatory items")
    lines.append("")
    lines.append("| Area | Status |")
    lines.append("|---|---|")
    lines.append("| NIS2 -- incident reporting (24h/72h) | Review needed |")
    lines.append("| DORA -- digital resilience (financial sector) | Assess applicability |")
    lines.append("| AI governance -- ISO/IEC 42001 | Gap identified |")
    lines.append("| NSM Grunnprinsipper | Ongoing |")
    lines.append("")
    lines.append("---")
    lines.append(f"*Generated {today}*")

    return "\n".join(lines)


def main():
    today = datetime.today().strftime("%Y-%m-%d")
    risks = load_risks()
    report = build_report(risks, today)

    out_dir = os.path.join(os.path.dirname(__file__), "..", "reports")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, f"report-{today}.md")

    with open(out_path, "w") as f:
        f.write(report)

    print(f"Report saved to {out_path}")


if __name__ == "__main__":
    main()
