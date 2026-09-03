#!/usr/bin/env python3
"""
Risk Assessment Tool
Structured risk assessment following NSM Grunnprinsipper and ISO 27001:2022.
VSR methodology: Value / Vulnerability / Risk.

Usage:
    python risk/risk_assessment.py --new
    python risk/risk_assessment.py --file risk/sample_risks.json --report
    python risk/risk_assessment.py --file risk/sample_risks.json --add
"""

import json, argparse, os
from datetime import datetime

LIKELIHOOD_LABELS = {1:"Very unlikely",2:"Unlikely",3:"Possible",4:"Likely",5:"Almost certain"}
IMPACT_LABELS     = {1:"Negligible",2:"Minor",3:"Moderate",4:"Serious",5:"Critical"}

def level(score):
    if score>=17: return "Critical"
    if score>=10: return "High"
    if score>=5:  return "Medium"
    return "Low"

def deadline(lvl):
    return {"Critical":"Immediate -- escalate to management","High":"30 days","Medium":"90 days","Low":"Monitor annually"}.get(lvl,"")

def load_file(path):
    with open(path) as f: return json.load(f)

def save_file(data, path):
    with open(path,"w") as f: json.dump(data,f,indent=2,ensure_ascii=False)
    print(f"Saved to {path}")

def new_risk():
    print("\n" + "="*60)
    print("  NEW RISK -- NSM / ISO 27001:2022")
    print("="*60)
    r = {}
    r["id"]          = input("\nRisk ID (e.g. RISK-007): ").strip() or "RISK-NEW"
    r["title"]       = input("Short title: ").strip()
    r["asset"]       = input("Asset or system at risk: ").strip()
    r["threat"]      = input("Threat scenario: ").strip()
    r["description"] = input("What could happen and why: ").strip()

    print("\nLikelihood 1-5:")
    for k,v in LIKELIHOOD_LABELS.items(): print(f"  {k}. {v}")
    r["likelihood"] = int(input("Score: ").strip() or "3")

    print("\nImpact 1-5:")
    for k,v in IMPACT_LABELS.items(): print(f"  {k}. {v}")
    r["impact"] = int(input("Score: ").strip() or "3")

    r["score"]     = r["likelihood"] * r["impact"]
    r["level"]     = level(r["score"])
    r["treatment"] = input("\nTreatment (mitigate/accept/transfer/avoid): ").strip() or "mitigate"
    r["owner"]     = input("Risk owner: ").strip()
    r["controls"]  = input("Planned controls: ").strip()
    r["status"]    = "open"
    r["created"]   = datetime.today().strftime("%Y-%m-%d")
    r["updated"]   = datetime.today().strftime("%Y-%m-%d")

    print(f"\n  Score: {r['score']} ({r['level']}) -- {deadline(r['level'])}\n")
    return r

def print_report(risks):
    if not isinstance(risks, list): risks = [risks]
    open_r  = [r for r in risks if r.get("status") != "closed"]
    closed  = [r for r in risks if r.get("status") == "closed"]
    print("\n" + "="*64)
    print(f"  RISK REPORT  |  {datetime.today().strftime('%Y-%m-%d')}  |  {len(open_r)} open  |  {len(closed)} closed")
    print("="*64)
    for lvl in ["Critical","High","Medium","Low"]:
        group = [r for r in open_r if r.get("level")==lvl]
        if not group: continue
        print(f"\n  [{lvl.upper()}]")
        print("  " + "-"*58)
        for r in group:
            print(f"\n  {r['id']} -- {r['title']}")
            print(f"  Asset      : {r.get('asset','N/A')}")
            print(f"  Threat     : {r.get('threat','N/A')}")
            print(f"  Score      : {r['score']}  (L:{r['likelihood']} x I:{r['impact']})")
            print(f"  Owner      : {r.get('owner','N/A')}")
            print(f"  Treatment  : {r.get('treatment','N/A')}")
            print(f"  Action by  : {deadline(lvl)}")
            if r.get("controls"): print(f"  Controls   : {r['controls']}")
    if closed:
        print(f"\n  CLOSED ({len(closed)})")
        for r in closed: print(f"  {r['id']} -- {r['title']}")
    print("\n" + "="*64 + "\n")

def main():
    p = argparse.ArgumentParser(description="Risk Assessment -- NSM / ISO 27001:2022")
    p.add_argument("--new",    action="store_true")
    p.add_argument("--file",   help="Path to risk register JSON")
    p.add_argument("--report", action="store_true")
    p.add_argument("--add",    action="store_true")
    args = p.parse_args()

    if args.new:
        risk = new_risk()
        out  = os.path.join(os.path.dirname(__file__), "sample_risks.json")
        data = load_file(out) if os.path.exists(out) else []
        if not isinstance(data, list): data = [data]
        data.append(risk)
        save_file(data, out)
    elif args.file and args.report:
        print_report(load_file(args.file))
    elif args.file and args.add:
        data = load_file(args.file)
        if not isinstance(data, list): data = [data]
        data.append(new_risk())
        save_file(data, args.file)
        print_report(data)
    else:
        p.print_help()

if __name__ == "__main__":
    main()
