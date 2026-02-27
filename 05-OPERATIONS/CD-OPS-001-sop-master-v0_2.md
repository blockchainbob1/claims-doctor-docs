---
doc_id: CD-OPS-001
title: Standard Operating Procedures (Master)
version: 0.2
status: DRAFT
visibility: INTERNAL
owner: Robert Laidlaw
last_updated: 2026-02-27
approved_date: null
next_review: 2026-05-27
dependencies:
  - CD-GOV-001
  - CD-OPS-002
changelog:
  - version: 0.2
    date: 2026-02-27
    summary: Technology stack resolved (HubSpot, Halaxy, Google Meet, Heidi Health). Dependencies CD-GOV-001 v1.0 and CD-OPS-002 v1.0 now satisfied. Booking flow confirmed — HubSpot for booking/CRM/billing/comms, Halaxy for clinical records only. Promotion criteria 1 and 2 met.
  - version: 0.1
    date: 2026-02-27
    summary: Initial draft — Pilot-stage operating model, stage definitions, workflow ownership
---

# Standard Operating Procedures — Master

**Claims Doctor** · Same-day WorkCover & CTP medical certificates.

---

## 01 Purpose

This document defines the operational framework for Claims Doctor service delivery. It establishes the stage-gated operating model, assigns ownership for each workflow area, and sets the maturity roadmap that governs when manual processes must be replaced with automation or delegation. All subordinate SOPs (CD-OPS-003 through CD-OPS-010) inherit their scope and escalation paths from this document.

---

## 02 Scope

**Applies to:** All Claims Doctor operational activities including patient intake, consultation booking, clinical consultations, certificate issuance, billing, complaints handling, adverse event management, and post-consultation follow-up.

**Applies to personnel:** Currently Dr. Robert Laidlaw (sole operator). Extends to all contracted doctors and administrative staff as the business scales.

**Does not cover:** Clinical decision-making protocols (see CD-GOV-003), marketing execution (see CD-MKT-001), or financial modelling (see CD-FIN-001).

---

## 03 Definitions

| Term | Definition |
|------|-----------|
| Certificate of Capacity | The SIRA-mandated document for WorkCover injury assessment |
| Certificate of Fitness | The SIRA-mandated document for CTP injury assessment |
| Stage gate | A defined set of criteria that must be met before the business transitions to the next operational stage |
| SOP | Standard Operating Procedure — a documented workflow for a specific operational function |
| Sole operator model | Operating mode where a single individual (Dr. Laidlaw) performs all clinical, administrative, and business functions |

---

## 04 Operating Stages

Claims Doctor operates through three sequential stages in its first year. Each stage has defined entry criteria, an exit gate, and a distinct operating model. Movement between stages is not time-bound — it is criteria-bound. The timelines below are targets, not triggers.

### 04.1 Pilot — 5 Patients in 30 Days

**Objective:** Prove the end-to-end workflow works. Get 5 patients through the full cycle from intake to certificate issuance to payment received.

**Target duration:** First 30 days of operation.

**Entry criteria:**
- HubSpot booking URL live and connected (https://www.claimsdoctor.com.au/meetings/robert-laidlaw/consult-claims-doctor)
- At least one consultation time slot available every day
- Google Meet operational for telehealth consultations
- Halaxy configured: patient records, clinical notes, prescribing, certificate templates
- Heidi Health integrated and tested with Halaxy
- ABN registered, bank account active, invoicing capability confirmed in HubSpot
- Informed consent process operational per CD-LEG-008 and CD-LEG-011

**Operating model:**
- Sole operator: Dr. Robert Laidlaw performs all functions
- Intake: manual via phone call, website chat, or HubSpot booking URL
- Booking: HubSpot meeting link (https://www.claimsdoctor.com.au/meetings/robert-laidlaw/consult-claims-doctor), manually managed calendar
- Consultation: Google Meet (video); phone fallback only for documented patient-side technical failure
- Clinical records & notes: Halaxy (with Heidi Health AI note-taking feeding into Halaxy)
- Certificate issuance: prepared and issued via Halaxy
- Prescriptions: Halaxy electronic prescribing
- Billing: HubSpot — manual invoicing per CD-OPS-002 fee codes
- Patient communications: HubSpot (email, SMS)
- Clinical governance: Dr. Laidlaw is the responsible clinician and clinical governance lead per CD-GOV-001
- Complaints: Dr. Laidlaw handles directly
- Automation: minimal — deliberate choice to reduce friction and test the workflow before investing in systems

**Exit gate (move to Consolidate when ALL met):**
- [ ] 5 patients have completed the full cycle (intake → consult → certificate → payment received)
- [ ] No unresolved complaints or adverse events
- [ ] Average time from booking to certificate delivery measured and documented
- [ ] At least one iteration/improvement made to the workflow based on patient feedback or operational observation
- [ ] Financial model (CD-FIN-001) validated against actual unit economics from the 5 cases

### 04.2 Consolidate — 5 Patients/Week by Day 90

**Objective:** Establish repeatable throughput. Achieve 5 patients per week with consistent service quality and manageable operator workload.

**Target duration:** Achieved within 90 days of launch.

**Entry criteria:** All Pilot exit gate criteria met.

**Operating model changes from Pilot:**
- Intake: introduce structured intake form in HubSpot (replace or supplement phone/chat)
- Booking: evaluate whether HubSpot booking flow needs automation (e.g., automated confirmation, reminders via HubSpot workflows)
- Billing: evaluate batch invoicing or payment gateway integration within HubSpot
- Follow-up: introduce templated post-consultation communication via HubSpot email sequences
- Clinical governance: formalise incident log even if no incidents have occurred (per CD-GOV-001 s08)
- Begin documenting subordinate SOPs (OPS-003 through OPS-010) based on actual workflows, not theoretical ones

**Exit gate (move to Scale when ALL met):**
- [ ] Sustained 5 patients/week for at least 4 consecutive weeks
- [ ] All subordinate SOPs drafted to at least v0.1 based on real operational experience
- [x] Clinical Governance Framework (CD-GOV-001) at v1.0 — met 2026-02-27
- [ ] Patient satisfaction mechanism in place (even if informal)
- [ ] Operator workload assessed — documented estimate of hours per patient and hours per week
- [ ] Decision made: which functions get delegated first when a second operator joins

### 04.3 Scale — Multi-Practitioner Model by Day 180

**Objective:** Onboard additional doctors. Transition from sole operator to a multi-practitioner model with defined roles, delegated responsibilities, and systematised processes.

**Target duration:** Achieved within 180 days of launch.

**Context:** By this stage, Claims Doctor revenue should support Dr. Laidlaw reducing hours in other clinical work, creating the capacity to manage a multi-practitioner service. This is not a separate milestone — it is a natural consequence of hitting Consolidate throughput targets.

**Entry criteria:** All Consolidate exit gate criteria met.

**Operating model changes from Consolidate:**
- Second doctor onboarded under CD-OPS-005 (Doctor Onboarding & Credentialing SOP)
- Administrative functions partially or fully delegated
- HubSpot booking must support multiple provider calendars
- Halaxy must support multiple practitioner profiles with appropriate access controls
- Credentialing and privileging process operational (CD-GOV-002)
- Clinical governance requires peer review or audit capability per CD-GOV-001 s07
- Complaints pathway must not rely solely on Dr. Laidlaw
- Billing automation required — manual HubSpot invoicing does not scale past sole operator

**Exit gate (future — define when Consolidate is complete):**
- To be defined based on Consolidate learnings

---

## 05 Workflow Areas & Ownership

Each workflow area below has (or will have) a dedicated subordinate SOP. During Pilot, the subordinate SOPs do not need to exist — this master document is sufficient. Subordinate SOPs must be drafted during Consolidate based on actual operational experience.

| # | Workflow Area | Subordinate SOP | Current Owner | Pilot Method | Automation Trigger |
|---|--------------|----------------|---------------|----------------|-------------------|
| 1 | Patient intake & triage | CD-OPS-003 | Dr. Laidlaw | Phone, chat, HubSpot booking URL | When intake volume exceeds what can be managed manually between consultations |
| 2 | Consultation booking | CD-OPS-004 | Dr. Laidlaw | HubSpot meeting link, daily availability | When multiple providers need scheduling or no-show rate exceeds 20% |
| 3 | Doctor onboarding & credentialing | CD-OPS-005 | Dr. Laidlaw | Not applicable in Pilot | Scale entry |
| 4 | Certificate issuance | CD-OPS-006 | Dr. Laidlaw | Prepared and issued via Halaxy post-consult | When certificate volume exceeds 5/day or error rate is non-zero |
| 5 | Billing & invoicing | CD-OPS-007 | Dr. Laidlaw | Manual invoicing via HubSpot per CD-OPS-002 fee codes | When volume exceeds 25 invoices/week or payment collection lag exceeds 14 days |
| 6 | Post-consult follow-up | CD-OPS-008 | Dr. Laidlaw | Manual (HubSpot email or phone as needed) | When follow-up falls below 100% completion rate |
| 7 | Complaint handling | CD-OPS-009 | Dr. Laidlaw | Direct handling, logged | Any complaint — formalise immediately upon first occurrence |
| 8 | Adverse event management | CD-OPS-010 | Dr. Laidlaw | Direct handling per CD-GOV-001 s08 and CD-GOV-005 | Any adverse event — formalise immediately upon first occurrence |

---

## 06 Escalation & Decision Authority

During Pilot and Consolidate, all escalation paths terminate at Dr. Robert Laidlaw. This section exists to define the framework that will be populated as the team grows.

| Decision Type | Pilot / Consolidate Authority | Scale Authority |
|--------------|--------------------|--------------------|
| Clinical decisions | Dr. Laidlaw | Consulting doctor (with peer review per CD-GOV-001) |
| Complaints | Dr. Laidlaw | Designated complaints officer (may still be Dr. Laidlaw) |
| Adverse events | Dr. Laidlaw | Clinical governance lead + mandatory external reporting per CD-GOV-005 |
| Billing disputes | Dr. Laidlaw | Administrative function (TBD) |
| Operational changes | Dr. Laidlaw | Dr. Laidlaw (retained) |
| SOP approval | Dr. Laidlaw | Dr. Laidlaw (retained) |

---

## 07 SOP Standards

All subordinate SOPs created under this master document must follow these standards:

1. Use the Claims Doctor document template (CD-TEMPLATE).
2. Include: purpose, scope, step-by-step procedure, responsible person(s), escalation path, and review schedule.
3. Be written for the person doing the work, not for an auditor. Plain language. No ambiguity.
4. Be based on how the workflow actually operates, not how it should theoretically operate. Update the SOP when the workflow changes, not the other way around.
5. Include the stage applicability — which stages the SOP applies to and what changes between stages.
6. Be reviewed whenever the master SOP (this document) receives a major version bump, per the dependency rules in CD-STR-000.

---

## 08 Technology Stack (Pilot)

Detailed technology documentation lives in CD-OPS-011. This section captures the minimum viable stack for Pilot operations.

### 08.1 Platform Separation Principle

Claims Doctor operates on a two-platform model with a strict separation of concerns:

- **HubSpot** handles everything on the business side: booking, CRM, contact management, billing demographics, invoicing, patient communications, and marketing automation.
- **Halaxy** handles everything on the clinical side: patient medical records, clinical notes (ingested from Heidi Health), prescriptions, and sending/receiving clinical documents.

No clinical information is stored in HubSpot. No billing or marketing data is managed in Halaxy. This separation ensures clinical record integrity, simplifies privacy compliance, and prevents scope creep between systems.

### 08.2 Platform Register

| Function | Tool | Role | Notes |
|----------|------|------|-------|
| Booking | HubSpot | Initial consultation booking via meeting link (https://www.claimsdoctor.com.au/meetings/robert-laidlaw/consult-claims-doctor) | Follow-up bookings also managed via HubSpot |
| CRM / contact management | HubSpot | Patient demographics, claim details, communication history, billing data | Single source of truth for non-clinical patient data |
| Patient communications | HubSpot | Email, SMS, follow-up sequences, appointment reminders | All patient-facing comms except clinical documents |
| Invoicing / billing | HubSpot | Invoice generation, payment tracking, insurer billing | Fee codes and rates per CD-OPS-002 and CD-FIN-002 |
| Telehealth (video consultation) | Google Meet | Primary consultation modality | Phone fallback only for documented patient-side technical failure per CD-GOV-001 s04.1 |
| Clinical records / patient management | Halaxy | Medical history, consultation records, clinical documents | Must meet record-keeping requirements in CD-GOV-001 s09.2 |
| AI clinical note-taking | Heidi Health | Real-time consultation transcription and note generation | Notes ingested into Halaxy as the clinical record |
| Prescriptions | Halaxy | Electronic prescribing | Limited to medications relevant to injury management per CD-GOV-001 s09.3 |
| Clinical document exchange | Halaxy | Sending/receiving certificates, referrals, specialist letters | Certificates of Capacity and Certificates of Fitness issued via Halaxy |
| Document management (internal) | Google Drive | Business documents per CD-STR-000 conventions | Markdown files with YAML frontmatter |

---

## 09 Metrics & Monitoring

These metrics are tracked from day one, even during Pilot. Manual log (spreadsheet) is sufficient for Pilot. Migrate to HubSpot as tracked contact properties once volume justifies it (likely Consolidate stage). The manual baseline from Pilot is your benchmark — don't lose it when you migrate.

| Metric | How Measured | Frequency | Pilot Target |
|--------|-------------|-----------|----------------|
| Patients per week | HubSpot contact count | Weekly | ≥1 (any is a win) |
| Time: booking to consultation | HubSpot booking timestamp → Google Meet start | Per patient | <24 hours |
| Time: consultation to certificate delivered | Halaxy timestamps (consult end → certificate sent) | Per patient | <4 hours |
| Time: certificate to payment received | HubSpot invoice timestamp → payment received | Per patient | <14 days |
| Complaints | Count + log | Per occurrence | 0 |
| Adverse events | Count + log per CD-GOV-001 s08 | Per occurrence | 0 |
| No-show rate | HubSpot booked vs attended | Weekly | <20% |
| Operator hours per patient | Estimate | Per patient | Baseline — measure, don't target |

---

## 10 Dependency Note

This document depends on:

- **CD-GOV-001 (Clinical Governance Framework) — v1.0 ACTIVE.** Defines the clinical governance structure that all operational workflows must comply with. Satisfied as of 2026-02-27.
- **CD-OPS-002 (Service Catalogue) — v1.0 ACTIVE.** Defines what services Claims Doctor offers, eligibility criteria, delivery specifications, fee codes, and scope boundaries. Satisfied as of 2026-02-27.

### Documents that depend on this SOP

| Doc ID | Title | Impact |
|--------|-------|--------|
| CD-OPS-003 | Patient Intake & Triage SOP | Inherits stage model, ownership, standards |
| CD-OPS-004 | Consultation Booking SOP | Inherits stage model, ownership, standards |
| CD-OPS-005 | Doctor Onboarding & Credentialing SOP | Inherits stage model (Scale activation) |
| CD-OPS-006 | Certificate Issuance SOP | Inherits stage model, ownership, standards |
| CD-OPS-007 | Billing & Invoicing SOP | Inherits stage model, ownership, standards |
| CD-OPS-008 | Post-Consult Follow-Up SOP | Inherits stage model, ownership, standards |
| CD-OPS-009 | Complaint Handling SOP | Inherits stage model, escalation paths |
| CD-OPS-010 | Adverse Event Management SOP | Inherits stage model, escalation paths |
| CD-OPS-012 | Business Continuity / Disaster Recovery Plan | Inherits technology stack, operational model |

Any major version bump to this document triggers mandatory review of all nine dependent documents.

---

## 11 Related Documents

| Doc ID | Title | Relationship |
|--------|-------|-------------|
| CD-GOV-001 | Clinical Governance Framework | Dependency (v1.0 ACTIVE) — governs clinical standards for all workflows |
| CD-OPS-002 | Service Catalogue | Dependency (v1.0 ACTIVE) — defines service specifications, eligibility, fee codes |
| CD-FIN-002 | Pricing Schedule (SIRA Fee Mapping) | Informs billing workflow (via CD-OPS-002) |
| CD-OPS-011 | Technology Stack Documentation | Details tools referenced in Section 08 |
| CD-STR-000 | Document Registry | Governs document standards and dependency rules |

---

## 12 Review & Approval

| Role | Name | Date | Signature |
|------|------|------|-----------|
| Author | Robert Laidlaw | 2026-02-27 | |
| Reviewer | — | — | — |
| Approver | Robert Laidlaw | — | — |

**Promotion criteria:** This document may be promoted to v1.0 when:
1. ~~CD-GOV-001 is at v1.0 (ACTIVE)~~ — ✅ Met 2026-02-27
2. ~~CD-OPS-002 is at v1.0 (ACTIVE)~~ — ✅ Met 2026-02-27
3. Pilot exit gate has been met
4. All workflow areas have been validated through actual patient throughput

---

**Claims Doctor** · claimsdoctor.com.au
ABN 39 674 905 376 · Level 1/457-459 Elizabeth Street, Surry Hills NSW 2010

_This document is the property of Claims Doctor. Unauthorised distribution is prohibited._
_Document ID: CD-OPS-001 · Version 0.2 · Status: DRAFT · Visibility: INTERNAL_
