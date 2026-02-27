---
doc_id: CD-GOV-001
title: Clinical Governance Framework
version: 0.1
status: DRAFT
visibility: INTERNAL
owner: Robert Laidlaw
last_updated: 2026-02-27
approved_date: null
next_review: 2026-08-27
dependencies: []
changelog:
  - version: 0.1
    date: 2026-02-27
    summary: Initial draft created. Phased governance model for pre-revenue telehealth platform.
---

# Clinical Governance Framework

**Claims Doctor** · Same-day WorkCover & CTP medical certificates.

---

## 01 Purpose

This framework defines the minimum clinical governance structures, accountabilities, and standards required for Claims Doctor to operate safely and lawfully as a telehealth platform delivering WorkCover and CTP medical certificates in New South Wales. It establishes what is mandatory before the first patient consultation and what scales as the business grows.

---

## 02 Scope

**Applies to:** All persons delivering, supporting, or overseeing clinical services on the Claims Doctor platform — including the Responsible Officer, contracted medical practitioners, and any operational or administrative staff.

**Covers:** Clinical safety, practitioner credentialing, incident management, informed consent, privacy, quality improvement, and telehealth-specific standards for the delivery of WorkCover Certificates of Capacity and CTP Certificates of Fitness via video consultation.

**Does not cover:** Non-clinical business operations (see CD-OPS-001), financial management (see CD-FIN-001), or marketing and brand compliance (see CD-MKT-001, CD-LEG-001). Allied health services are out of scope until formally added to the service catalogue.

---

## 03 Definitions

| Term | Definition |
|------|-----------|
| Certificate of Capacity | The SIRA-mandated document issued under the Workers Compensation Act 1987 (NSW) for workplace injury assessment and return-to-work planning. |
| Certificate of Fitness | The SIRA-mandated document issued under the Motor Accident Injuries Act 2017 (NSW) for CTP injury assessment. |
| Responsible Officer | The individual accountable for clinical governance at Claims Doctor. Currently the Founder/Director. |
| Nominated Practitioner | A medical practitioner credentialed and authorised to deliver consultations on the Claims Doctor platform. |
| Clinical Incident | Any event or circumstance that resulted in, or could have resulted in, harm to a patient. Includes near misses. |
| Open Disclosure | The open discussion of a clinical incident with the affected patient, as defined by the Australian Open Disclosure Framework. |
| AHPRA | Australian Health Practitioner Regulation Agency. The national body regulating registered health practitioners. |
| SIRA | State Insurance Regulatory Authority (NSW). The regulator for workers' compensation and CTP schemes. |
| ACSQHC | Australian Commission on Safety and Quality in Health Care. Sets the National Safety and Quality Health Service Standards. |
| Telehealth Consultation | A real-time, audio-visual clinical consultation conducted via the Claims Doctor platform between a Nominated Practitioner and a patient. |

---

## 04 Governance Phasing Model

This framework operates across three phases. Each phase defines the minimum governance requirements for that stage of business maturity. All Phase 1 requirements are mandatory before the first patient consultation. Phase 2 and 3 requirements are triggered by the thresholds specified.

| Phase | Trigger | Focus |
|-------|---------|-------|
| Phase 1 — Launch | Pre-revenue through first 50 consultations | Minimum viable governance. Safety-critical controls only. |
| Phase 2 — Early Operations | 50–500 consultations or 3+ active practitioners | Formalised review cadence, expanded audit, peer review introduced. |
| Phase 3 — Scale | 500+ consultations or 5+ active practitioners | Clinical Advisory Committee, systematic QI program, external audit. |

The Responsible Officer must assess phase transitions quarterly and document the assessment in the Monthly Business Review (CD-RPT-002).

---

## 05 Accountability Structure

### 05.1 Phase 1 — Responsible Officer Model

Robert Laidlaw (Founder/Director) is the Responsible Officer for clinical governance at Claims Doctor. This means:

- Ultimate accountability for patient safety, clinical quality, and regulatory compliance rests with one person.
- The Responsible Officer personally approves all practitioner credentialing decisions.
- The Responsible Officer is the first point of escalation for all clinical incidents.
- The Responsible Officer conducts or directly oversees all governance activities described in this framework.

This is a deliberate, resource-appropriate structure for a pre-revenue startup. It is not a permanent state.

### 05.2 Phase 2 — Medical Director Appointment

When Claims Doctor reaches Phase 2, the Responsible Officer must appoint a Medical Director (who may be a contracted Nominated Practitioner) with the following minimum responsibilities:

- Clinical oversight of practitioner performance.
- Leadership of peer review activities.
- Co-signatory on credentialing decisions.
- First point of clinical escalation (replacing the Responsible Officer in this role).

### 05.3 Phase 3 — Clinical Advisory Committee

At Phase 3, a Clinical Advisory Committee (CAC) must be established comprising a minimum of the Responsible Officer, the Medical Director, and one independent external clinician with occupational medicine experience. The CAC meets quarterly and is responsible for reviewing governance performance, incident trends, and recommending policy changes.

---

## 06 Pillar 1 — Credentialing and Scope of Practice

**Operationalised in:** CD-GOV-002 (Credentialing & Privileging Policy)

### 06.1 Mandatory Requirements — All Phases

Before any practitioner delivers a consultation on the Claims Doctor platform, the Responsible Officer must verify and document the following:

1. **AHPRA registration** — Current, unconditional general or specialist registration. Any conditions, undertakings, or reprimands are a disqualifying factor unless the Responsible Officer documents in writing why the condition does not affect fitness to deliver Claims Doctor services.
2. **Professional indemnity insurance** — Current policy with coverage adequate for telehealth occupational health consultations. Minimum $20 million recommended.
3. **Workers' compensation provider number** — Valid for the relevant state/territory.
4. **Qualifications** — Medical degree and, at minimum, Fellowship of RACGP or equivalent. Occupational medicine qualifications (AFOEM/RACP) are preferred but not mandatory at Phase 1.
5. **Right to work** — Evidence of Australian citizenship, permanent residency, or valid work visa.
6. **National Police Check** — Issued within the preceding 12 months.
7. **Working With Children Check** — If the service catalogue expands to include minors.

### 06.2 Scope of Practice Definition

Each Nominated Practitioner is authorised to perform the following on the Claims Doctor platform:

- Initial injury assessment via video consultation.
- Issuance of SIRA Certificates of Capacity (WorkCover NSW).
- Issuance of SIRA Certificates of Fitness (CTP NSW).
- Return-to-work capacity recommendations.
- Referral to specialists, allied health, or emergency services where clinically indicated.

Nominated Practitioners are **not** authorised to:

- Prescribe Schedule 8 medications via the platform.
- Conduct independent medical examinations (IMEs) unless separately credentialed for this purpose.
- Issue certificates for jurisdictions outside NSW unless the Responsible Officer has confirmed regulatory compliance for that jurisdiction.

### 06.3 Re-credentialing

- **Phase 1:** AHPRA registration status checked manually at onboarding and every 6 months.
- **Phase 2:** Automated AHPRA register checks integrated into the platform. Full re-credentialing annually.
- **Phase 3:** Annual re-credentialing with peer review input from the Medical Director.

---

## 07 Pillar 2 — Incident and Risk Management

**Operationalised in:** CD-GOV-005 (Incident Reporting & Management Policy)

### 07.1 Incident Classification

| Severity | Definition | Example | Response Timeframe |
|----------|-----------|---------|-------------------|
| SAC 1 — Catastrophic | Death or permanent serious harm. | Patient death following missed diagnosis. | Immediate. External notification within 24 hours. |
| SAC 2 — Major | Serious harm requiring intervention. | Significant misdiagnosis leading to delayed treatment. | Within 24 hours. |
| SAC 3 — Moderate | Harm with temporary impact. | Incorrect certificate issued, requiring amendment. | Within 72 hours. |
| SAC 4 — Minor / Near Miss | No harm, but potential identified. | Platform outage during consultation, resolved by phone. | Within 7 days. |

### 07.2 Phase 1 — Minimum Incident Management

- All clinical incidents are reported directly to the Responsible Officer via a standardised incident report form (to be developed as part of CD-GOV-005).
- The Responsible Officer investigates all SAC 1–3 incidents personally within the specified timeframe.
- SAC 1 incidents trigger mandatory notification to AHPRA and/or the relevant coroner as required by law.
- A simple incident register (spreadsheet) is maintained from day one.
- Open disclosure is conducted for all SAC 1–3 incidents in accordance with the Australian Open Disclosure Framework.

### 07.3 Phase 2 Additions

- Formal Root Cause Analysis (RCA) for all SAC 1–2 incidents.
- Quarterly incident trend review by the Medical Director.
- Anonymous reporting option introduced.

### 07.4 Phase 3 Additions

- Incident trends reported to the Clinical Advisory Committee quarterly.
- Annual external review of incident management system.

---

## 08 Pillar 3 — Informed Consent

**Operationalised in:** CD-LEG-011 (Informed Consent Template), CD-LEG-008 (Telehealth Consent Policy)

### 08.1 Mandatory Requirements — All Phases

Before a consultation proceeds, every patient must provide informed consent covering:

1. **Nature of the service** — The consultation is a telehealth video consultation for the purpose of assessing work capacity and/or injury status. It is not a substitute for emergency care or ongoing treatment.
2. **Limitations of telehealth** — Physical examination is not possible. The practitioner may recommend an in-person follow-up if clinical assessment requires it.
3. **Information sharing** — The patient understands that certificate information will be shared with their employer and/or insurer as required by SIRA legislation. Clinical notes are not shared without additional consent unless required by law.
4. **Recording** — Whether the consultation is recorded, and for what purpose. If no recording occurs, this must be explicitly stated.
5. **Financial consent** — Who is paying (insurer, employer, or patient), what the fee is, and whether any out-of-pocket cost applies.
6. **Right to withdraw** — The patient may end the consultation at any time without prejudice to their claim.
7. **Complaints** — How to lodge a complaint about the service (see CD-LEG-009).

### 08.2 Consent Mechanism

- **Phase 1:** Digital consent form completed by the patient prior to consultation via the booking platform. Stored as part of the patient record. Consent is affirmative (checkbox + electronic signature), not implied.
- **Phase 2+:** Consent integrated into the patient intake workflow with version-controlled consent forms linked to the patient record.

---

## 09 Pillar 4 — Telehealth Standards and Clinical Appropriateness

**Operationalised in:** CD-GOV-003 (Clinical Protocols / Practice Guidelines)

### 09.1 Platform Requirements — All Phases

The Claims Doctor telehealth platform must meet the following minimum standards:

- **End-to-end encryption** of all audio and video.
- **Minimum video quality** of 720p to enable adequate visual assessment.
- **Australian data residency** — All consultation data, recordings (if any), and clinical notes stored on servers located in Australia.
- **Identity verification** — The practitioner must verify the patient's identity at the start of every consultation using government-issued photo ID.
- **Failover protocol** — If video fails, the practitioner may complete the consultation via phone only if clinically appropriate. The decision to proceed via phone-only must be documented in the clinical notes with the clinical rationale.

### 09.2 Clinical Appropriateness — Exclusion Criteria

The following presentations are **not appropriate** for telehealth assessment on the Claims Doctor platform and must be referred to in-person care:

- Acute trauma requiring physical examination or imaging within 24 hours.
- Suspected fractures, dislocations, or significant lacerations not yet assessed in person.
- Neurological deficits requiring physical neurological examination.
- Chest pain, breathing difficulty, or any presentation suggesting a medical emergency.
- Mental health crisis requiring immediate risk assessment beyond the capacity of a video consultation.
- Any presentation where the practitioner determines, in their clinical judgement, that adequate assessment cannot be performed via video.

The practitioner has final clinical authority to decline a telehealth consultation and recommend in-person assessment. This decision is never overridden by operational or commercial considerations.

### 09.3 Consultation Documentation Standards

Every consultation must result in a clinical note that includes, at minimum:

- Patient identification details.
- Date, time, and duration of the consultation.
- Mode of consultation (video or phone with documented rationale if phone).
- Presenting complaint and relevant history.
- Clinical findings (including limitations of telehealth assessment where relevant).
- Diagnosis or differential diagnoses.
- Certificate issued (type, capacity determination, recommended duration, restrictions).
- Referrals made.
- Follow-up plan.
- Practitioner name, provider number, and electronic signature.

---

## 10 Pillar 5 — Privacy, Data Security, and Confidentiality

**Operationalised in:** CD-LEG-004 (Privacy Policy), CD-LEG-005 (Patient Privacy & Data Handling Policy), CD-GOV-004 (Medical Records Management Policy)

### 10.1 Legislative Compliance — All Phases

Claims Doctor must comply with:

- **Privacy Act 1988 (Cth)** and the Australian Privacy Principles (APPs).
- **Health Records and Information Privacy Act 2002 (NSW)** and the Health Privacy Principles.
- **My Health Records Act 2012 (Cth)** if integration with My Health Record is implemented.
- **Workers Compensation Act 1987 (NSW)** and **Motor Accident Injuries Act 2017 (NSW)** regarding the lawful sharing of medical information with insurers and employers.

### 10.2 Minimum Data Security Requirements — Phase 1

- All patient data encrypted at rest and in transit (AES-256 minimum).
- Multi-factor authentication (MFA) mandatory for all practitioner and staff accounts.
- Role-based access control — practitioners can only access records of patients they are treating or have treated.
- No patient data stored on personal devices, local drives, or non-approved cloud services.
- Data breach response plan documented before first consultation (see CD-LEG-005).
- All third-party software handling patient data must have a signed Business Associate Agreement or equivalent data processing agreement confirming Australian data residency and APP compliance.

### 10.3 Records Retention

- Clinical records retained for a minimum of **7 years** from the date of the last consultation, or until the patient reaches age 25 if the patient is under 18 (per NSW Health Records and Information Privacy Act 2002).
- Workers' compensation records retained in accordance with SIRA guidelines — minimum **7 years** after the claim is finalised.
- Destruction of records must be by secure, auditable means.

---

## 11 Pillar 6 — Quality Improvement

**Operationalised in:** CD-RPT-001 (KPI Dashboard Specification), CD-RPT-002 (Monthly Business Review Template)

### 11.1 Phase 1 — Minimum Viable QI

Quality improvement at Phase 1 is deliberately lightweight. The objective is to establish measurement habits, not bureaucratic overhead.

**Clinical KPIs tracked from the first consultation:**

| KPI | Target | Measurement Method |
|-----|--------|-------------------|
| Certificate turnaround time | Same-day (within 4 hours of consultation) | Platform timestamp |
| Certificate amendment rate | < 5% | Manual count from incident register |
| Patient complaint rate | < 2% of consultations | Complaint log |
| Consultation completion rate | > 95% (not abandoned due to tech failure) | Platform analytics |
| AHPRA credential currency | 100% of active practitioners | Credentialing register |

**Monthly review:** The Responsible Officer reviews all KPIs monthly as part of the business review cycle. No formal committee or meeting structure is required at Phase 1. A 30-minute self-review is sufficient.

### 11.2 Phase 2 Additions

- Randomised clinical note audit — 10% of consultations per month, reviewed by the Medical Director.
- Patient satisfaction survey introduced (post-consultation, optional, 3 questions maximum).
- Quarterly case review sessions with all active practitioners (30 minutes, virtual).

### 11.3 Phase 3 Additions

- Formal Quality Improvement Plan reviewed by the Clinical Advisory Committee annually.
- Benchmarking against industry standards (ACSQHC, RACGP Standards for General Practices — Telehealth Provisions).
- External clinical audit annually.

---

## 12 Pillar 7 — Complaints and Feedback

**Operationalised in:** CD-LEG-009 (Complaints & Feedback Policy), CD-OPS-009 (Complaint Handling SOP)

### 12.1 Phase 1 — Minimum Requirements

- A clearly communicated complaints pathway is published on the website and included in the post-consultation summary.
- Complaints can be submitted via email or an online form.
- The Responsible Officer acknowledges all complaints within 2 business days.
- The Responsible Officer investigates and responds to all complaints within 14 business days.
- A complaints register is maintained from day one (spreadsheet is acceptable at Phase 1).
- The patient is informed of their right to escalate to the Health Care Complaints Commission (HCCC) if unsatisfied with the resolution.

### 12.2 Phase 2 Additions

- Complaints triaged by severity (mirroring the incident classification in Section 07.1).
- Trend analysis reviewed quarterly by the Medical Director.

---

## 13 Regulatory Obligations Summary

This section maps Claims Doctor's primary regulatory obligations to ensure nothing is missed. It is not exhaustive but captures the critical compliance requirements for NSW telehealth WorkCover/CTP services.

| Obligation | Regulator / Legislation | Claims Doctor Requirement |
|-----------|------------------------|--------------------------|
| Practitioner registration | AHPRA / Health Practitioner Regulation National Law | All Nominated Practitioners hold current AHPRA registration. Verified at credentialing and 6-monthly. |
| Advertising compliance | AHPRA / National Law s.133 | All marketing materials reviewed against CD-LEG-001 before publication. |
| Privacy and data handling | OAIC / Privacy Act 1988, HRIP Act 2002 (NSW) | Privacy Policy published. APP compliance. Data breach plan in place. |
| Workers' compensation certificates | SIRA / Workers Compensation Act 1987 (NSW) | Certificates issued per SIRA guidelines. Practitioner holds valid WC provider number. |
| CTP certificates | SIRA / Motor Accident Injuries Act 2017 (NSW) | Certificates issued per SIRA CTP guidelines. |
| Telehealth standards | Medical Board of Australia / AHPRA | Compliance with Medical Board's Telehealth Guidelines. |
| Informed consent | Common law / ACSQHC | Consent obtained and documented per Section 08. |
| Incident notification | AHPRA / Coroners Act 2009 (NSW) | Mandatory notifications made within required timeframes per Section 07. |
| Complaints handling | HCCC / Health Care Complaints Act 1993 (NSW) | Complaints pathway published and accessible. HCCC escalation pathway communicated to patients. |
| Business registration | ASIC / ABN | ABN 39 674 905 376 current. Business name registered. |

---

## 14 Related Documents

| Doc ID | Title | Relationship |
|--------|-------|-------------|
| CD-GOV-002 | Credentialing & Privileging Policy | Operationalises Pillar 1 (Section 06) |
| CD-GOV-003 | Clinical Protocols / Practice Guidelines | Operationalises Pillar 4 (Section 09) |
| CD-GOV-004 | Medical Records Management Policy | Operationalises Pillar 5 (Section 10) |
| CD-GOV-005 | Incident Reporting & Management Policy | Operationalises Pillar 2 (Section 07) |
| CD-GOV-006 | Medication Management Policy | Referenced if prescribing is added to service catalogue |
| CD-GOV-007 | Infection Control Policy | Out of scope for telehealth-only operations. Required if in-person services added. |
| CD-LEG-004 | Privacy Policy (Website) | Supports Pillar 5 (Section 10) |
| CD-LEG-005 | Patient Privacy & Data Handling Policy | Supports Pillar 5 (Section 10) |
| CD-LEG-008 | Telehealth Consent Policy | Supports Pillar 3 (Section 08) |
| CD-LEG-009 | Complaints & Feedback Policy | Supports Pillar 7 (Section 12) |
| CD-LEG-011 | Informed Consent Template | Supports Pillar 3 (Section 08) |
| CD-OPS-001 | Standard Operating Procedures (Master) | Depends on this framework for clinical governance requirements |
| CD-RPT-001 | KPI Dashboard Specification | Supports Pillar 6 (Section 11) |
| CD-RPT-002 | Monthly Business Review Template | Supports Pillar 6 (Section 11) |

---

## 15 Review & Approval

| Role | Name | Date | Signature |
|------|------|------|-----------|
| Author | Claude (AI Assistant) | 2026-02-27 | — |
| Reviewer | | | |
| Approver | Robert Laidlaw | | |

**Review schedule:** This framework must be reviewed at minimum every 6 months, or immediately upon any of the following triggers:

- A SAC 1 or SAC 2 incident.
- A phase transition (see Section 04).
- A material change to SIRA, AHPRA, or privacy legislation affecting Claims Doctor's operations.
- The appointment of a Medical Director.

---

**Claims Doctor** · claimsdoctor.com.au
ABN 39 674 905 376 · Level 1/457-459 Elizabeth Street, Surry Hills NSW 2010

_This document is the property of Claims Doctor. Unauthorised distribution is prohibited._
_Document ID: CD-GOV-001 · Version 0.1 · Status: DRAFT · Visibility: INTERNAL_
