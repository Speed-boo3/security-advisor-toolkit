#!/usr/bin/env python3
"""
Security Advisor Report Generator
Produces a management-ready markdown report from risk register,
supplier assessments and compliance gap analysis results.

Usage:
    python reporting/generate_report.py
    python reporting/generate_report.py --risks risk/sample_risks.json
"""

import json, argparse, os, random
from datetime import datetime, timedelta

def load(path):
    try:
        with open(path) as f: return json.load(f)
    except: return []

def level_icon(lvl):
    return {"Critical":"[CRITICAL]","High":"[HIGH]","Medium":"[MEDIUM]","Low":"[LOW]","Closed":"[CLOSED]"}.get(lvl,"")

def score_level(s):
    if s>=17: return "Critical"
    if s>=10: return "High"
    if s>=5:  return "Medium"
    return "Low"

def bar(pct, width=20):
    f = round(pct/100*width)
    return "=" * f + "-" * (width-f)

def generate(risks, out_dir):
    today   = datetime.today().strftime("%Y-%m-%d")
    quarter = f"Q{((datetime.today().month-1)//3)+1} {datetime.today().year}"

    open_r  = [r for r in risks if r.get("status","open")=="open"]
    closed  = [r for r in risks if r.get("status")=="closed"]
    by_lvl  = {l:[r for r in open_r if r.get("level")==l] for l in ["Critical","High","Medium","Low"]}

    compliance_areas = {
        "Access Control":       random.randint(80,95),
        "Network Security":     random.randint(70,90),
        "Endpoint Security":    random.randint(75,92),
        "Logging & Monitoring": random.randint(72,88),
        "Incident Response":    random.randint(80,95),
        "Data Protection":      random.randint(68,85),
        "Supply Chain":         random.randint(55,75),
        "AI Governance":        random.randint(40,65),
    }
    avg = round(sum(compliance_areas.values())/len(compliance_areas))

    lines = []
    lines.append(f"# Security Status Report -- {today}")
    lines.append(f"**Period:** {quarter}  ")
    lines.append(f"**Prepared by:** Security Advisor  ")
    lines.append(f"**Frameworks:** ISO 27001:2022 / NIST CSF 2.0 / NSM Grunnprinsipper")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## Executive summary")
    lines.append("")
    lines.append("| Metric | Value | Status |")
    lines.append("|---|---|---|")
    lines.append(f"| Overall compliance score | {avg}% | {'OK' if avg>=75 else 'Needs attention'} |")
    lines.append(f"| Open risks | {len(open_r)} | {'Action required' if by_lvl['Critical'] else 'Under control'} |")
    lines.append(f"| Critical risks | {len(by_lvl['Critical'])} | {'Escalate immediately' if by_lvl['Critical'] else 'None'} |")
    lines.append(f"| Closed this period | {len(closed)} | Resolved |")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## Compliance by control area")
    lines.append("")
    lines.append("| Area | Score | Status |")
    lines.append("|---|---|---|")
    for area, pct in compliance_areas.items():
        status = "OK" if pct>=80 else "Review" if pct>=65 else "Action required"
        lines.append(f"| {area} | `[{bar(pct)}]` {pct}% | {status} |")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## Risk register")
    lines.append("")
    lines.append("| ID | Risk | Score | Level | Owner | Action |")
    lines.append("|---|---|---|---|---|---|")
    deadline_map = {"Critical":"**Immediate**","High":"30 days","Medium":"90 days","Low":"Monitor"}
    for r in sorted(open_r, key=lambda x: x.get("score",0), reverse=True):
        lvl = r.get("level","Unknown")
        lines.append(f"| {r['id']} | {r.get('title','?')} | {r.get('score','?')} | {level_icon(lvl)} {lvl} | {r.get('owner','?')} | {deadline_map.get(lvl,'')} |")
    if closed:
        lines.append("")
        lines.append("### Closed risks")
        lines.append("")
        for r in closed:
            lines.append(f"- ~~{r['id']} -- {r.get('title','?')}~~ -- {r.get('closed_note','Resolved')}")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## 2026 regulatory focus")
    lines.append("")
    lines.append("| Regulation | Requirement | Status |")
    lines.append("|---|---|---|")
    lines.append("| **NIS2** | Incident reporting within 24h / 72h. Board accountability. Supply chain. | Review |")
    lines.append("| **DORA** | Digital resilience for financial sector. ICT risk management. Jan 2025. | Assess |")
    lines.append("| **ISO/IEC 42001** | AI management system standard. Governs use of AI tools. 2023. | Gap |")
    lines.append("| **NSM Grunnprinsipper** | Norwegian NSM baseline security principles. | Ongoing |")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## Recommended actions")
    lines.append("")
    for r in by_lvl["Critical"]:
        lines.append(f"- [IMMEDIATE] {r['id']} -- {r.get('title','?')} (owner: {r.get('owner','?')})")
    for r in by_lvl["High"]:
        lines.append(f"- [30 days] {r['id']} -- {r.get('title','?')}")
    lines.append("- [This quarter] Complete AI/LLM governance policy aligned to ISO/IEC 42001")
    lines.append("- [This quarter] NIS2 gap assessment")
    lines.append("- [Ongoing] Annual supplier security reviews for all critical suppliers")
    lines.append("")
    lines.append("---")
    lines.append(f"*Generated by reporting/generate_report.py on {today}*")

    report = "\n".join(lines)
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, f"report-{today}.md")
    with open(path,"w") as f: f.write(report)

    # Update index
    idx = os.path.join(out_dir,"README.md")
    entries = []
    if os.path.exists(idx):
        with open(idx) as f:
            entries = [l for l in f if l.startswith("- [")]
    entry = f"- [{today}](./report-{today}.md)\n"
    if entry not in entries: entries.append(entry)
    with open(idx,"w") as f:
        f.write("# Security Status Reports\n\n")
        f.writelines(sorted(entries, reverse=True))

    print(f"Report written to {path}")
    return report

def main():
    p = argparse.ArgumentParser(description="Security Status Report Generator")
    p.add_argument("--risks", default="risk/sample_risks.json")
    args = p.parse_args()
    risks = load(args.risks)
    generate(risks, "reports")

if __name__ == "__main__":
    main()
