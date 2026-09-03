#!/usr/bin/env python3
"""
Risk Matrix
-----------
Loads a risk register and prints a sorted report.
Built to practice the kind of risk scoring a security advisor does in practice.

Run: python risk/risk_matrix.py
"""

import json
import os


def score_to_level(score):
    if score >= 17:
        return "Critical"
    if score >= 10:
        return "High"
    if score >= 5:
        return "Medium"
    return "Low"


def main():
    path = os.path.join(os.path.dirname(__file__), "risk_register.json")
    with open(path) as f:
        risks = json.load(f)

    open_risks = [r for r in risks if r.get("status", "open") == "open"]
    closed     = [r for r in risks if r.get("status") == "closed"]

    sorted_risks = sorted(open_risks, key=lambda r: r["score"], reverse=True)

    print("\nRisk Register")
    print("=" * 70)
    print(f"{'ID':<12} {'Risk':<35} {'Score':<7} {'Level':<10} {'Owner'}")
    print("-" * 70)

    for r in sorted_risks:
        level = score_to_level(r["score"])
        print(f"{r['id']:<12} {r['title'][:34]:<35} {r['score']:<7} {level:<10} {r['owner']}")

    print("-" * 70)
    print(f"\nOpen: {len(open_risks)}   Closed: {len(closed)}")

    critical = [r for r in open_risks if score_to_level(r["score"]) == "Critical"]
    if critical:
        print(f"\nAction required immediately:")
        for r in critical:
            print(f"  {r['id']} -- {r['title']} (owner: {r['owner']})")

    print()


if __name__ == "__main__":
    main()
