<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0d1117,30:050a1a,100:0a1628&height=210&section=header&text=Security%20Advisor%20Toolkit&fontSize=50&fontColor=4488ff&animation=fadeIn&fontAlignY=42&desc=Risk%20Assessment%20%7C%20Supplier%20Security%20%7C%20ISO%2027001%20Gap%20Analysis%20%7C%20Compliance%20Reporting&descAlignY=65&descColor=555555&descSize=13"/>

<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&size=14&duration=2500&pause=900&color=4488FF&center=true&vCenter=true&width=700&lines=Risk+assessment+following+NSM+and+ISO+27001%3A2022;Supplier+security+evaluation+against+Annex+A+5.19-5.22;ISO+27001%3A2022+gap+analysis+with+remediation+plan;Management-ready+compliance+reports;Security+policy+and+contract+clause+templates"/>

<br/>

![ISO](https://img.shields.io/badge/ISO-27001%3A2022-0d1117?style=flat-square&logoColor=4488ff)
![NIST](https://img.shields.io/badge/NIST-CSF%202.0-0d1117?style=flat-square&logoColor=4488ff)
![NSM](https://img.shields.io/badge/NSM-Grunnprinsipper-0d1117?style=flat-square&logoColor=4488ff)
![NIS2](https://img.shields.io/badge/NIS2-2024-0d1117?style=flat-square&logoColor=00e676)
![Python](https://img.shields.io/badge/Python-3.8+-0d1117?style=flat-square&logo=python&logoColor=4488ff)

</div>

---

## What this is

A practical toolkit for security advisors working in organisations that need to manage information security risk, demonstrate compliance and handle supplier relationships systematically.

The tools here are built around the frameworks and methodologies that actually come up in GRC work: ISO 27001:2022 Annex A controls, NSM Grunnprinsipper, NIS2 incident reporting obligations and the VSR (value / vulnerability / risk) methodology used in Norwegian security assessments. Each tool produces output that is ready to use in a real security programme, not a simulation.

---

## Tools

### Risk assessment

Structured risk identification, scoring and treatment planning. Follows NSM methodology and ISO 27001:2022 section 6.1. Outputs a prioritised risk register sorted by score.

```bash
# Start a new risk assessment interactively
python risk/risk_assessment.py --new

# Print the full risk register report
python risk/risk_assessment.py --file risk/sample_risks.json --report
```

```
================================================================
  RISK REPORT  |  2026-09-03  |  7 open  |  1 closed
================================================================

  [CRITICAL]
  ----------------------------------------------------------

  RISK-001 -- Phishing attack against personnel
  Asset      : User accounts and corporate email
  Threat     : Targeted spear-phishing
  Score      : 20  (L:5 x I:4)
  Owner      : Security Team
  Treatment  : mitigate
  Action by  : Immediate -- escalate to management
  Controls   : FIDO2 keys for privileged accounts, AI email threat detection

  RISK-003 -- Ransomware affecting operational systems
  Score      : 15  (L:3 x I:5)
  Action by  : 30 days
```

---

### Supplier security assessment

Evaluates suppliers against 14 security criteria based on ISO 27001:2022 Annex A 5.19-5.22. Produces an APPROVED / CONDITIONAL / NOT APPROVED recommendation with a gap list.

```bash
python supplier/supplier_assessment.py --new
python supplier/supplier_assessment.py --file supplier/assessments.json --report
```

```
  [X] Acme Software Ltd -- 52% -- NOT APPROVED
       Service     : IT maintenance tooling
       Criticality : high
       High gaps   : 3
         - ISO 27001 or equivalent certification
         - Security incident notification clause
         - Personnel security and background checks

  [!] Cloud Systems AS -- 74% -- CONDITIONAL
       Service     : Cloud storage
       Criticality : high
       High gaps   : 1
         - Data processing agreement in place
```

---

### ISO 27001:2022 gap analysis

Walks through 24 Annex A controls across all four themes. Calculates compliance score per theme and outputs a prioritised remediation plan.

```bash
python compliance/gap_analysis.py --run
python compliance/gap_analysis.py --file compliance/gap_results.json --report
```

```
  Organisational  [================----]  82%
  People          [==============------]  72%
    [!] 6.1 -- Screening -- GAP
         Action: Implement background check process for all new hires
  Technological   [============--------]  64%
    [!] 8.8 -- Management of technical vulnerabilities -- GAP
    [!] 8.15 -- Logging -- PARTIAL

  Overall compliance: 74%

  PRIORITY ACTIONS (3 high-priority gaps)
```

---

### Compliance report generator

Combines risk register, supplier assessments and compliance data into a management-ready markdown report. Covers ISO 27001:2022, NIST CSF 2.0, NSM Grunnprinsipper and 2026 regulatory requirements (NIS2, DORA, AI governance).

```bash
python reporting/generate_report.py --risks risk/sample_risks.json
```

Reports are saved to `reports/` with an auto-updated index. Ready to share with management or include in an audit package.

---

## Policy and contract templates

**`policy/security_policy_template.md`**

A complete security policy template covering governance, access control, supplier security, incident response, AI governance and personnel security. Built around ISO 27001:2022 and NSM Grunnprinsipper. Includes NIS2 obligations where relevant.

**`policy/supplier_security_clause.md`**

Seven standard contract clauses covering information security requirements, data protection, incident notification, right to audit, personnel security, subcontractors and data deletion. Ready to insert into supplier agreements.

---

## Risk register -- current findings

The sample risk register (`risk/sample_risks.json`) contains 8 realistic risk scenarios relevant to organisations handling sensitive information:

| Risk | Score | Level |
|---|---|---|
| Phishing attack against personnel | 20 | Critical |
| Inadequate logging and monitoring | 12 | High |
| Ransomware affecting operational systems | 15 | High |
| Supply chain compromise via third-party software | 10 | High |
| Insider threat -- unauthorised data access | 10 | High |
| Missing security requirements in supplier contracts | 9 | Medium |
| Weak endpoint security on remote workers | 9 | Medium |
| Lost or stolen laptop | 4 | Low -- Closed |

---

## 2026 regulatory context

Security advisors in 2026 need to navigate a more complex regulatory environment than two years ago.

**NIS2 Directive** came into force across EU member states in October 2024. It significantly expands who is covered, requires board-level accountability for security, mandates 24-hour incident early warning and 72-hour full notification, and sets strict requirements for supply chain security. Organisations in essential or important sectors that have not done a NIS2 gap assessment are exposed.

**DORA** (Digital Operational Resilience Act) came into force in January 2025 for financial sector organisations. It requires documented ICT risk management, resilience testing and third-party risk oversight.

**ISO/IEC 42001:2023** is the AI management system standard. As organisations adopt AI tools including LLMs, regulators and auditors are starting to ask what governance exists around them. This toolkit includes AI governance requirements in both the security policy template and the gap analysis.

**NSM Grunnprinsipper** remain the Norwegian baseline. The risk assessment tool uses the VSR methodology that aligns with how NSM expects risk to be documented.

---

## Usage

```bash
git clone https://github.com/Speed-boo3/security-advisor-toolkit.git
cd security-advisor-toolkit
pip install -r requirements.txt

# Run a full risk report
python risk/risk_assessment.py --file risk/sample_risks.json --report

# Run the compliance report generator
python reporting/generate_report.py

# Start a new supplier assessment
python supplier/supplier_assessment.py --new
```

---

## Related projects

- [soc-project](https://github.com/Speed-boo3/soc-project) -- detection engineering tools referenced in the logging and monitoring risk entries
- [grc-project](https://github.com/Speed-boo3/grc-project) -- broader GRC framework with ISO 27001 and NIST CSF documentation
- [cloud-security](https://github.com/Speed-boo3/cloud-security) -- cloud misconfiguration scanning with CIS benchmark compliance scoring

<div align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0a1628,50:050a1a,100:0d1117&height=100&section=footer&text=Structure.%20Evidence.%20Accountability.&fontSize=15&fontColor=4488ff&animation=twinkling"/>
</div>
