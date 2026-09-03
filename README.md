<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0d1117,30:050a1a,100:0a1628&height=200&section=header&text=Security%20Advisor%20Toolkit&fontSize=50&fontColor=4488ff&animation=fadeIn&fontAlignY=42&desc=Risk%20Assessment%20%7C%20Supplier%20Security%20%7C%20ISO%2027001%3A2022%20%7C%20Compliance%20Reporting&descAlignY=65&descColor=555555&descSize=13"/>

<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&size=14&duration=2500&pause=900&color=4488FF&center=true&vCenter=true&width=700&lines=Risk+register+with+NSM+scoring+methodology;Supplier+assessment+against+ISO+27001+Annex+A+5.19-5.22;ISO+27001%3A2022+gap+analysis+checklist;Automated+compliance+report+generation;NIS2+and+DORA+2026+regulatory+coverage"/>

<br/>

![ISO](https://img.shields.io/badge/ISO-27001%3A2022-0d1117?style=flat-square&logoColor=4488ff)
![NIST](https://img.shields.io/badge/NIST-CSF%202.0-0d1117?style=flat-square&logoColor=4488ff)
![NSM](https://img.shields.io/badge/NSM-Grunnprinsipper-0d1117?style=flat-square&logoColor=4488ff)
![NIS2](https://img.shields.io/badge/NIS2-2024-0d1117?style=flat-square&logoColor=00e676)
![Python](https://img.shields.io/badge/Python-3.8+-0d1117?style=flat-square&logo=python&logoColor=4488ff)

</div>

---

## Background

I built this while preparing for a role as a security advisor. The goal was to understand what the job actually involves day to day, not just the theory. A security advisor spends a lot of time on three things: assessing and prioritising risks, evaluating suppliers, and producing documentation that management and auditors can act on.

This project covers all three. The risk register follows the VSR methodology referenced in NSM guidance. The supplier checklist maps to ISO 27001:2022 Annex A 5.19-5.22, which is the part of the standard that deals specifically with supplier relationships. The compliance checklist covers the controls most commonly tested in ISO 27001 audits. And the report generator pulls it all together into something that could actually be handed to a manager.

---

## What is in here

```
security-advisor-toolkit/
├── risk/
│   ├── risk_matrix.py          <- reads the register and prints a sorted report
│   └── risk_register.json      <- 8 realistic risk scenarios
├── supplier/
│   └── supplier_checklist.md   <- 17-point assessment, ISO 27001 Annex A 5.19-5.22
├── compliance/
│   └── iso27001_checklist.md   <- gap analysis across 24 Annex A controls
├── policy/
│   └── security_policy_template.md  <- policy template with NIS2 requirements
├── reporting/
│   └── generate_report.py      <- produces a markdown report from the risk register
└── reports/
    └── report-2026-09-03.md    <- example output
```

---

## Risk register

The register covers eight scenarios that come up frequently in real risk assessments. Scored by likelihood x impact on a 1 to 5 scale, following the approach NSM uses.

```bash
python risk/risk_matrix.py
```

```
Risk Register
======================================================================
ID           Risk                                Score   Level      Owner
----------------------------------------------------------------------
RISK-001     Phishing against personnel          20      Critical   Security Team
RISK-002     Ransomware via initial access        15      High       IT Operations
RISK-006     Insufficient logging and monitoring  12      High       Security Operations
RISK-007     Missing AI governance policy         12      High       Security / HR
RISK-003     Supply chain compromise              10      High       Procurement / IT
RISK-004     Insider threat -- data exfiltration  10      High       HR / Security
RISK-005     Weak supplier contract security       9      Medium     Procurement / Legal
----------------------------------------------------------------------

Open: 7    Closed: 1
```

The supply chain and AI governance risks are the ones I find most interesting to think about in 2026. Supply chain compromise is high impact because it bypasses most perimeter defences, and AI governance is a gap in almost every organisation right now because the tools moved faster than the policies did.

---

## Supplier assessment

The checklist in `supplier/supplier_checklist.md` covers 17 criteria across five areas: documentation and certification, access and personnel, technical controls, and supply chain resilience. It produces an Approved / Conditional / Not Approved recommendation.

This maps directly to ISO 27001:2022 Annex A 5.19-5.22, which is what most auditors will check when they ask about your supplier security programme.

---

## ISO 27001:2022 gap analysis

The checklist in `compliance/iso27001_checklist.md` covers 24 controls across all four Annex A themes. It is designed to be filled in during an internal assessment before an external audit.

The controls that most organisations have gaps on, in my experience reading case studies and audit reports, are 5.7 (threat intelligence), 5.22 (supplier review), 8.8 (vulnerability management) and 8.15 (logging).

---

## Compliance report

```bash
python reporting/generate_report.py
```

Reads the risk register and produces a markdown report covering risk status, 2026 regulatory requirements (NIS2, DORA, AI governance) and recommended actions. Saved to `reports/`.

---

## 2026 regulatory context

Three things have changed recently that a security advisor needs to understand:

**NIS2** came into force across EU member states in October 2024. It expanded the scope significantly and introduced 24-hour early warning obligations for significant incidents. Board-level accountability is now explicit. Supply chain security requirements are much stricter than under the original NIS Directive.

**DORA** came into force in January 2025 for financial sector organisations. It requires documented ICT risk management, resilience testing and specific third-party oversight obligations.

**AI governance** is still catching up with practice. ISO/IEC 42001:2023 provides a framework, but most organisations do not yet have a policy that covers how staff are allowed to use AI tools. This is showing up as a finding in security assessments more and more.

---

## Quickstart

```bash
git clone https://github.com/Speed-boo3/security-advisor-toolkit.git
cd security-advisor-toolkit
python risk/risk_matrix.py
python reporting/generate_report.py
```

<div align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0a1628,50:050a1a,100:0d1117&height=100&section=footer&text=Structure.%20Evidence.%20Accountability.&fontSize=15&fontColor=4488ff&animation=twinkling"/>
</div>
