#!/usr/bin/env python3
"""
ISO 27001:2022 Gap Analysis Tool
Maps current control status against Annex A and calculates
compliance score per theme. Outputs a prioritised remediation plan.

Usage:
    python compliance/gap_analysis.py --run
    python compliance/gap_analysis.py --file compliance/gap_results.json --report
"""

import json, argparse, os
from datetime import datetime

CONTROLS = [
    # (id, title, theme, priority)
    ("5.1",  "Policies for information security",               "Organisational", "high"),
    ("5.2",  "Roles and responsibilities",                      "Organisational", "high"),
    ("5.7",  "Threat intelligence",                             "Organisational", "high"),
    ("5.9",  "Inventory of assets",                             "Organisational", "medium"),
    ("5.19", "Supplier relationship security",                  "Organisational", "high"),
    ("5.20", "Security requirements in supplier agreements",    "Organisational", "high"),
    ("5.22", "Monitoring and review of supplier services",      "Organisational", "medium"),
    ("5.23", "Cloud services security",                         "Organisational", "high"),
    ("5.24", "Incident management planning",                    "Organisational", "high"),
    ("5.30", "ICT readiness for business continuity",           "Organisational", "medium"),
    ("6.1",  "Screening (personnel background checks)",         "People",         "high"),
    ("6.3",  "Information security awareness and training",     "People",         "medium"),
    ("7.1",  "Physical security perimeters",                    "Physical",       "medium"),
    ("7.4",  "Physical security monitoring",                    "Physical",       "medium"),
    ("8.2",  "Privileged access rights",                        "Technological",  "high"),
    ("8.5",  "Secure authentication",                           "Technological",  "high"),
    ("8.7",  "Protection against malware",                      "Technological",  "high"),
    ("8.8",  "Management of technical vulnerabilities",         "Technological",  "high"),
    ("8.9",  "Configuration management",                        "Technological",  "medium"),
    ("8.15", "Logging",                                         "Technological",  "high"),
    ("8.16", "Monitoring activities",                           "Technological",  "high"),
    ("8.24", "Use of cryptography",                             "Technological",  "medium"),
    ("8.28", "Secure coding",                                   "Technological",  "medium"),
    ("8.30", "Outsourced development",                          "Technological",  "low"),
]

STATUS_SCORE = {"compliant": 2, "partial": 1, "gap": 0, "na": None}

def load_file(p):
    with open(p) as f: return json.load(f)

def save_file(data, p):
    with open(p,"w") as f: json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"Saved to {p}")

def run_assessment():
    print("\n" + "="*62)
    print("  ISO 27001:2022 GAP ANALYSIS")
    print("  Status: compliant / partial / gap / na (not applicable)")
    print("="*62)

    results   = []
    org_n     = input("\nOrganisation: ").strip()
    assessor  = input("Assessor: ").strip()

    for cid, title, theme, priority in CONTROLS:
        print(f"\n[{cid}] ({theme} / {priority}) {title}")
        status = input("Status (compliant/partial/gap/na): ").strip().lower() or "gap"
        if status not in STATUS_SCORE: status = "gap"
        evidence = input("Evidence or note: ").strip()
        action   = input("Required action (if gap/partial): ").strip() if status in ("gap","partial") else ""
        results.append({
            "control":  cid,
            "title":    title,
            "theme":    theme,
            "priority": priority,
            "status":   status,
            "evidence": evidence,
            "action":   action,
        })

    return {
        "organisation": org_n,
        "assessor":     assessor,
        "date":         datetime.today().strftime("%Y-%m-%d"),
        "standard":     "ISO 27001:2022",
        "results":      results,
    }

def print_report(data):
    results = data.get("results", [])
    themes  = {}
    for r in results:
        themes.setdefault(r["theme"], []).append(r)

    print("\n" + "="*64)
    print(f"  ISO 27001:2022 GAP ANALYSIS REPORT")
    print(f"  Organisation : {data.get('organisation','N/A')}")
    print(f"  Assessor     : {data.get('assessor','N/A')}")
    print(f"  Date         : {data.get('date','N/A')}")
    print("="*64)

    total_score = 0
    total_max   = 0

    for theme, controls in themes.items():
        applicable = [c for c in controls if c["status"] != "na"]
        score  = sum(STATUS_SCORE.get(c["status"],0) for c in applicable)
        maxsc  = len(applicable) * 2
        pct    = round(score/maxsc*100) if maxsc else 0
        total_score += score
        total_max   += maxsc
        bar_filled   = round(pct/5)
        bar          = "=" * bar_filled + "-" * (20-bar_filled)
        print(f"\n  {theme}  [{bar}]  {pct}%")
        gaps = [c for c in applicable if c["status"] in ("gap","partial")]
        for g in sorted(gaps, key=lambda x: x["priority"] != "high"):
            flag = "[!]" if g["priority"]=="high" else "[ ]"
            print(f"    {flag} {g['control']} -- {g['title']} -- {g['status'].upper()}")
            if g.get("action"): print(f"         Action: {g['action']}")

    overall = round(total_score/total_max*100) if total_max else 0
    print(f"\n  Overall compliance: {overall}%")

    high_gaps = [r for r in results if r["status"]=="gap" and r["priority"]=="high"]
    if high_gaps:
        print(f"\n  PRIORITY ACTIONS ({len(high_gaps)} high-priority gaps)")
        for r in high_gaps:
            print(f"    {r['control']} -- {r['title']}")
            if r.get("action"): print(f"    Action: {r['action']}")

    print("\n" + "="*64 + "\n")

def main():
    p = argparse.ArgumentParser(description="ISO 27001:2022 Gap Analysis")
    p.add_argument("--run",    action="store_true", help="Run interactive assessment")
    p.add_argument("--file",   help="Path to existing gap analysis JSON")
    p.add_argument("--report", action="store_true")
    args = p.parse_args()

    out = os.path.join(os.path.dirname(__file__), "gap_results.json")

    if args.run:
        data = run_assessment()
        save_file(data, out)
        print_report(data)
    elif args.file and args.report:
        print_report(load_file(args.file))
    else:
        p.print_help()

if __name__ == "__main__":
    main()
