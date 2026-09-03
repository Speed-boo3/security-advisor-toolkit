# Information Security Policy

**Version:** 1.0
**Date:** September 2026
**Owner:** Security Advisor
**Review cycle:** Annual or after significant change

This template is built around ISO 27001:2022, NIST CSF 2.0 and NSM Grunnprinsipper.
Sections marked **(NIS2)** apply to organisations in scope of the NIS2 Directive.
Sections marked **(NSM)** reflect Norwegian NSM baseline requirements.

---

## 1. Purpose and scope

This policy establishes the requirements for protecting information assets and systems.
It applies to all employees, contractors, suppliers and anyone who accesses
organisation systems or handles organisation data.

Non-compliance may result in disciplinary action, access revocation or legal consequences.

---

## 2. Governance and roles

| Role | Responsibility |
|---|---|
| Board / management | Overall accountability for information security risk **(NIS2)** |
| Security advisor | Policy ownership, risk oversight, audit coordination |
| IT / system owners | Control implementation, monitoring, patch management |
| All personnel | Follow policy, complete training, report incidents immediately |
| Suppliers | Comply with supplier security requirements and contractual obligations |

---

## 3. Risk management **(NSM)**

Risk is assessed using a structured value / vulnerability / risk (VSR) methodology.

- Risk register is maintained and reviewed quarterly
- Risks are scored by likelihood x impact on a 1 to 5 scale
- Critical risks (score 17-25) require immediate management escalation
- Risk treatment decisions require documented management approval
- Supply chain risks are assessed before onboarding any critical supplier

---

## 4. Access control

- Principle of least privilege applies to all accounts and systems
- Multi-factor authentication is mandatory for all privileged and remote access
- Access is reviewed every 90 days -- unused accounts are disabled within 7 days
- Joiner / mover / leaver process is completed within 24 hours of a role change
- Service accounts and API keys are inventoried and rotated on a defined schedule

---

## 5. Personnel security

- Background checks are conducted for all personnel in security-sensitive roles
- Security awareness training is completed annually by all personnel
- Personnel handling classified information must be authorised in accordance with applicable regulations

---

## 6. Supplier and third-party security **(NIS2 / ISO 27001 5.19-5.22)**

- All suppliers with access to organisation data or systems complete a security assessment before onboarding
- Contracts include documented security requirements, data processing agreements and breach notification obligations
- Critical supplier security posture is reviewed annually
- Subcontractor arrangements require prior written approval and equivalent security requirements

---

## 7. Incident response **(NIS2)**

- All suspected security incidents are reported to the Security Advisor within 1 hour of detection
- Incident response follows a documented procedure based on NIST SP 800-61
- NIS2 obligations: early warning to relevant authority within 24 hours, full notification within 72 hours
- Post-incident reports are completed within 5 business days
- Lessons learned are fed back into risk register and detection rule updates

---

## 8. Logging and monitoring

- Security-relevant logs are collected centrally and retained for a minimum of 12 months
- Logs are protected against tampering
- Anomaly detection and alerting is in place for privileged account activity
- Mean time to detect (MTTD) is measured and reviewed quarterly

---

## 9. AI and technology governance

- Use of AI tools and large language models (LLMs) for work purposes requires prior approval
- Classified, sensitive or personal data must not be submitted to external AI services
- AI-generated outputs in security-relevant contexts require human review
- Aligns with ISO/IEC 42001:2023 (AI management systems)

---

## 10. Physical security

- Access to server rooms and sensitive areas is badge-controlled and logged
- Clean desk policy applies in all open work areas
- Visitors to secure areas are escorted at all times

---

## 11. Exceptions

Exceptions require written approval from the Security Advisor.
All exceptions are time-limited (maximum 90 days) and documented in the risk register.

---

## Review history

| Version | Date | Change |
|---|---|---|
| 1.0 | September 2026 | Initial release |
