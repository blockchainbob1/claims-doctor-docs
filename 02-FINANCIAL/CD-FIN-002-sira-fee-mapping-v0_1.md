---
doc_id: CD-FIN-002
title: Pricing Schedule — SIRA Fee Mapping
version: 0.1
status: DRAFT
visibility: INTERNAL
owner: Robert Laidlaw
last_updated: 2026-02-27
approved_date: null
next_review: 2026-03-29
dependencies: []
changelog:
  - version: 0.1
    date: 2026-02-27
    summary: Initial draft — WorkCover (WC) fees only. CTP fees deferred to next review.
---

# Pricing Schedule — SIRA Fee Mapping

**Claims Doctor** · Same-day WorkCover & CTP medical certificates.

---

## 01 Purpose

This document maps every billable Claims Doctor service to the correct SIRA payment classification code, gazetted maximum fee, and GST treatment. It is the single source of truth for what Claims Doctor charges, how invoices are itemised, and which regulatory fee schedule governs each line item.

---

## 02 Scope

**In scope:** All services billed to WorkCover insurers under the Workers Compensation (Medical Practitioner Fees) Order, effective 1 November 2025 (or as subsequently indexed).

**Not in scope (deferred to v0.2, due 2026-03-29):** CTP (Motor Accident Injuries Act 2017) fees. CTP medical practitioner fees are not gazetted by SIRA — they are capped at the applicable AMA List of Medical Services and Fees rates per Motor Accident Guidelines clause 4.101. CTP fee mapping will be added at the next scheduled review once AMA rates are confirmed and insurer billing arrangements are established.

**Applies to:** Robert Laidlaw (sole practitioner, owner-operator) and any future practitioners or billing staff engaged by Claims Doctor.

---

## 03 Definitions

| Term | Definition |
|------|-----------|
| Certificate of Capacity | The SIRA-mandated WorkCover document recording a worker's injury, fitness for work, and treatment needs. Issued by the treating medical practitioner. |
| Certificate of Fitness | The SIRA-mandated CTP document recording a motor accident claimant's injury, fitness for work, and treatment needs. **Out of scope for this version.** |
| AMA Fees List | The Australian Medical Association List of Medical Services and Fees — the reference schedule adopted by the Workers Compensation (Medical Practitioner Fees) Order for consultation item descriptors and codes. |
| Gazetted maximum | The maximum fee a medical practitioner may charge for a service under the relevant SIRA Fees Order. Charging above this amount is prohibited and recovery may be sought. |
| Telehealth | Delivery of consultations via video or telephone, consented to by both worker and practitioner, billed using the standard AMA item number with a 'T' suffix. The fee is the same as the equivalent face-to-face consultation. |
| SIRA provider number | The Claims Doctor practice provider number registered with SIRA: **433219VH**. |

---

## 04 Regulatory Framework

All WorkCover fees are governed by:

- **Workers Compensation (Medical Practitioner Fees) Order 2025** (effective 1 February 2025), as updated by the general practitioner rates effective 1 November 2025.
- **Workers Compensation (Medical Practitioner Fees) Order 2026** (effective 1 February 2026, indexed up to 4.57%) — once the updated GP summary rates sheet is published, this document must be updated to reflect the new figures.
- The Fees Order adopts the **AMA Fees List** for consultation item descriptors. To bill an AMA item, the practitioner must meet the service requirements specified in the item descriptor.
- Medical practitioners cannot bill any item in excess of the gazetted maximum fee. Recovery may be sought for fees charged above the maximum.

**Claims Doctor billing policy: all services are billed at the gazetted maximum.**

---

## 05 WorkCover Fee Schedule

### 05.1 Consultation Fees

All consultations are delivered via telehealth. Consultation fees are GST-free.

| Code | Service | Duration / Descriptor | Fee (excl. GST) | GST | Total |
|------|---------|----------------------|-----------------|-----|-------|
| AA045T | Level E consultation via telehealth | 60+ minutes. Prolonged consultation involving detailed history, comprehensive examination, and/or complex management plan per AMA Level E descriptor. | $450.00 | Nil | $450.00 |
| AA030T | Level C consultation via telehealth | 20+ minutes. Standard follow-up consultation involving history review, focused examination, and certificate update per AMA Level C descriptor. | $205.00 | Nil | $205.00 |

**Notes:**

- The 'T' suffix denotes telehealth delivery. The fee is identical to the equivalent face-to-face item.
- No facility fee may be charged in addition to the telehealth consultation fee.
- The practitioner must meet the full AMA descriptor criteria for the level billed. A 60-minute initial assessment with certificate completion supports Level E (AA045T). A follow-up review and certificate update typically supports Level C (AA030T).

### 05.2 Certificate of Capacity Fee

| Code | Service | Fee (excl. GST) | GST | Total (incl. GST) |
|------|---------|-----------------|-----|--------------------|
| WCO001 | Initial Certificate of Capacity — completion of the SIRA certificate for a new WorkCover claim | $56.20 | $5.62 | $61.82 |

**Notes:**

- This fee is payable **once per claim only**, for completion of the initial Certificate of Capacity.
- It is billed on the same invoice as the initial consultation (AA045T) but as a separate line item.
- Subsequent/follow-up Certificates of Capacity do not attract an additional WCO001 fee — certificate updates are included in the follow-up consultation fee.

### 05.3 Additional Services

| Code | Service | Fee (excl. GST) | GST | Total (incl. GST) |
|------|---------|-----------------|-----|--------------------|
| WCO002 | Services provided in addition to usual medical management — per 5 minutes | $28.10 | $2.81 | $30.91 |

**Billable activities under WCO002:**

- Discussions with employers regarding the worker's capacity, restrictions, and return-to-work planning.
- Case conferencing (face-to-face, video, or teleconference) with any combination of: the worker, employer, workplace rehabilitation provider, insurer, or other treating practitioners. A case conference must include at least one third party beyond the worker and their support person.
- Visits to worksites (not applicable to telehealth-only model at launch, but included for completeness).
- Time spent reviewing injury management or recovery-at-work/return-to-work plans.
- Providing additional reports when requested and pre-approved by the insurer.

**Billing rules for WCO002:**

- Invoices must reflect time taken to the nearest 5 minutes.
- This fee covers time **in addition to** the standard consultation — it cannot be used to top up a consultation that did not meet the descriptor for the billed level.
- Case conferencing over 2 hours per practitioner requires insurer pre-approval.

### 05.4 Other Billable Items

| Code | Service | Fee | GST | Notes |
|------|---------|-----|-----|-------|
| WCO004 | Other medical items | Cost price | Subject to item | Bandages, dressings, etc. Not expected to be routinely billed by a telehealth service. |
| WCO005 | Medical records — electronic | $68.20 | Nil | Flat fee for provision of all requested clinical records held electronically. Includes postage and handling. |
| WCO005 | Medical records — hard copy | $43.30 (up to 33 pages) + $1.40/additional page | Nil | Should not be provided if records are maintained electronically. |

---

## 06 Standard Invoice Scenarios

### 06.1 Initial Consultation (New WorkCover Claim)

| Line | Code | Description | Fee | GST | Line Total |
|------|------|-------------|-----|-----|------------|
| 1 | AA045T | Level E consultation via telehealth — 60 min | $450.00 | — | $450.00 |
| 2 | WCO001 | Initial Certificate of Capacity | $56.20 | $5.62 | $61.82 |
| | | **Invoice total** | | | **$511.82** |

### 06.2 Follow-Up Consultation (Existing Claim)

| Line | Code | Description | Fee | GST | Line Total |
|------|------|-------------|-----|-----|------------|
| 1 | AA030T | Level C consultation via telehealth — 20 min | $205.00 | — | $205.00 |
| | | **Invoice total** | | | **$205.00** |

### 06.3 Follow-Up Consultation + Case Conference

| Line | Code | Description | Fee | GST | Line Total |
|------|------|-------------|-----|-----|------------|
| 1 | AA030T | Level C consultation via telehealth — 20 min | $205.00 | — | $205.00 |
| 2 | WCO002 | Case conference with employer — 15 min (3 × 5 min) | $84.30 | $8.43 | $92.73 |
| | | **Invoice total** | | | **$297.73** |

---

## 07 Invoicing Requirements

All invoices submitted to WorkCover insurers must include:

1. **Claims Doctor ABN:** 39 674 905 376
2. **SIRA provider number:** 433219VH
3. **Practitioner's AHPRA number** and **Medicare provider number** (unless not registered with Medicare)
4. **Worker's details:** full name, date of birth, claim number
5. **Date of service** for each item
6. **SIRA payment classification code** (e.g., AA045T, WCO001) for each line item
7. **Fee for each item**, clearly itemised
8. **GST treatment** — clearly showing which items attract GST and which are GST-free
9. **Date of invoice** — must fall on the day of or after the last date of service listed on the invoice

**Submission deadline:** Invoices must be submitted to the insurer within **30 calendar days** of the service being provided.

---

## 08 Fee Indexation & Update Protocol

SIRA indexes WorkCover fees annually, typically effective 1 February. The 2026 indexation (up to 4.57%) has been gazetted but the updated GP summary rates document has not yet been published at the time of drafting.

**When updated rates are published:**

1. Update all fee amounts in sections 05 and 06 of this document.
2. Record the effective date of the new Fees Order.
3. Bump this document to the next minor version (e.g., v0.2).
4. Notify all downstream documents that depend on CD-FIN-002.

**Downstream documents dependent on CD-FIN-002:**

- CD-FIN-001 — Financial Model
- CD-OPS-002 — Service Catalogue
- CD-OPS-007 — Billing & Invoicing SOP
- CD-MKT-005 — Google Ads Playbook

---

## 09 CTP Fees — Placeholder

**Status: Deferred to next review (2026-03-29).**

CTP (Motor Accident Injuries Act 2017) medical practitioner fees are not gazetted by SIRA. The fee ceiling is the applicable AMA List of Medical Services and Fees rates at the time of service, per Motor Accident Guidelines clause 4.101.

Key differences from WorkCover that must be addressed in v0.2:

- No gazetted fee caps — rates are set by the AMA List, which is updated periodically.
- No separately billable certificate completion fee — the Certificate of Fitness is typically included in the consultation fee.
- Insurer must pay invoices within 20 calendar days (vs. 30 for WorkCover).
- Invoices must include AMA item numbers, patient name, date of crash, insurer reference/claim number, ABN, and GST where applicable.
- Insurer approval is required before treatment commences (with limited early intervention exceptions).

---

## 10 Related Documents

| Doc ID | Title | Relationship |
|--------|-------|-------------|
| CD-FIN-001 | Financial Model | Depends on this document for revenue-per-consult assumptions |
| CD-FIN-003 | Cash Flow Forecast | Depends on CD-FIN-001, which depends on this document |
| CD-OPS-002 | Service Catalogue | Depends on this document for service definitions and pricing |
| CD-OPS-007 | Billing & Invoicing SOP | Depends on this document for item codes, fees, and invoice requirements |
| CD-MKT-005 | Google Ads Playbook | Depends on this document for CPA/ROAS calculations |
| CD-LEG-002 | SIRA Compliance Manual | Informs compliance requirements referenced in this document |

---

## 11 Review & Approval

| Role | Name | Date | Signature |
|------|------|------|-----------|
| Author | Robert Laidlaw | 2026-02-27 | |
| Reviewer | | | |
| Approver | Robert Laidlaw | | |

---

**Claims Doctor** · claimsdoctor.com.au
ABN 39 674 905 376 · Level 1/457-459 Elizabeth Street, Surry Hills NSW 2010

_This document is the property of Claims Doctor. Unauthorised distribution is prohibited._
_Document ID: CD-FIN-002 · Version 0.1 · Status: DRAFT · Visibility: INTERNAL_
