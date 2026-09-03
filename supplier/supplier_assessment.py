#!/usr/bin/env python3
"""
Supplier Security Assessment Tool
Evaluates suppliers against security requirements before onboarding
and during annual reviews. Based on ISO 27001:2022 Annex A 5.19-5.22
and NSM supply chain guidance.

Usage:
    python supplier/supplier_assessment.py --new
    python supplier/supplier_assessment.py --file supplier/assessments.json --report
"""

import json, argparse, os
from datetime import datetime

CRITERIA = [
    ("ISO 27001 or equivalent certification",         "high",   "5.19"),
    ("Data processing agreement in place",            "high",   "5.20"),
    ("Security incident notification clause",         "high",   "5.20"),
    ("Right to audit clause in contract",             "medium", "5.20"),
    ("Personnel security and background checks",      "high",   "5.21"),
    ("Access control -- principle of least privilege","high",   "5.21"),
    ("Encrypted data transfer and storage",           "high",   "5.21"),
    ("Patch management and vulnerability handling",   "medium", "5.21"),
    ("Subcontractor security requirements",           "medium", "5.22"),
    ("Annual security review process",                "medium", "5.22"),
    ("Security awareness training for staff",         "medium", "5.21"),
    ("Documented incident response procedure",        "high",   "5.24"),
    ("Business continuity and recovery capability",   "medium", "5.30"),
    ("Software bill of materials (SBOM) available",  "low",    "8.30"),
]

ANSWER_SCORES = {"yes": 2, "partial": 1, "no": 0, "unknown": 0}

def load_file(path):
    with open(path) as f: return json.load(f)

def save_file(data, path):
    with open(path,"w") as f: json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"Saved to {path}")

def new_assessment():
    print("\n" + "="*62)
    print("  SUPPLIER SECURITY ASSESSMENT")
    print("  ISO 27001:2022 Annex A 5.19-5.22")
    print("="*62)

    a = {}
    a["supplier"]        = input("\nSupplier name: ").strip()
    a["service"]         = input("Service or product provided: ").strip()
    a["data_shared"]     = input("Data shared with supplier (describe): ").strip()
    a["criticality"]     = input("Criticality (critical/high/medium/low): ").strip() or "medium"
    a["assessor"]        = input("Assessed by: ").strip()
    a["date"]            = datetime.today().strftime("%Y-%m-%d")
    a["answers"]         = {}
    a["notes"]           = {}

    print("\nAnswer each criterion: yes / partial / no / unknown")
    print("-"*62)

    total_score    = 0
    max_score      = 0
    high_gaps      = []

    for criterion, priority, ref in CRITERIA:
        ans = input(f"\n[{ref}] {criterion}\n({priority}) Answer: ").strip().lower() or "unknown"
        if ans not in ANSWER_SCORES: ans = "unknown"
        score = ANSWER_SCORES[ans]
        weight = 2 if priority == "high" else 1
        total_score += score * weight
        max_score   += 2 * weight
        a["answers"][criterion] = ans
        note = input("Note (optional): ").strip()
        if note: a["notes"][criterion] = note
        if ans in ("no","unknown") and priority == "high":
            high_gaps.append(criterion)

    pct = round(total_score / max_score * 100) if max_score else 0
    a["score_pct"]  = pct
    a["high_gaps"]  = high_gaps
    a["recommendation"] = (
        "APPROVED"      if pct >= 80 and not high_gaps else
        "CONDITIONAL"   if pct >= 60 else
        "NOT APPROVED"
    )

    print(f"\n  Score: {pct}%  |  Recommendation: {a['recommendation']}")
    if high_gaps:
        print(f"  High-priority gaps: {len(high_gaps)}")
        for g in high_gaps: print(f"    - {g}")

    return a

def print_report(assessments):
    if not isinstance(assessments, list): assessments = [assessments]
    print("\n" + "="*64)
    print(f"  SUPPLIER SECURITY REPORT  |  {datetime.today().strftime('%Y-%m-%d')}")
    print(f"  Suppliers assessed: {len(assessments)}")
    print("="*64)
    for a in sorted(assessments, key=lambda x: x.get("score_pct", 0)):
        rec = a.get("recommendation","N/A")
        col = "[OK]" if rec=="APPROVED" else "[!]" if rec=="CONDITIONAL" else "[X]"
        print(f"\n  {col} {a.get('supplier','?')} -- {a.get('score_pct','?')}% -- {rec}")
        print(f"       Service     : {a.get('service','N/A')}")
        print(f"       Criticality : {a.get('criticality','N/A')}")
        print(f"       Assessed    : {a.get('date','N/A')} by {a.get('assessor','N/A')}")
        gaps = a.get("high_gaps",[])
        if gaps:
            print(f"       High gaps   : {len(gaps)}")
            for g in gaps: print(f"         - {g}")
    print("\n" + "="*64 + "\n")

def main():
    p = argparse.ArgumentParser(description="Supplier Security Assessment -- ISO 27001:2022")
    p.add_argument("--new",    action="store_true")
    p.add_argument("--file",   help="Assessments JSON file")
    p.add_argument("--report", action="store_true")
    args = p.parse_args()

    out = os.path.join(os.path.dirname(__file__), "assessments.json")

    if args.new:
        a    = new_assessment()
        data = load_file(out) if os.path.exists(out) else []
        if not isinstance(data, list): data = [data]
        data.append(a)
        save_file(data, out)
    elif args.file and args.report:
        print_report(load_file(args.file))
    else:
        p.print_help()

if __name__ == "__main__":
    main()
