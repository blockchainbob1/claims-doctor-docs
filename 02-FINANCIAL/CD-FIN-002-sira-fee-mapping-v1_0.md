---
doc_id: CD-FIN-002
title: "Pricing Schedule — SIRA Fee Mapping"
version: 1.0
status: ACTIVE
visibility: INTERNAL
owner: Robert Laidlaw
last_updated: 2026-03-01
approved_date: 2026-03-01
next_review: 2026-06-01
dependencies: []
changelog:
  - version: 0.1
    date: 2026-02-27
    summary: Placeholder created
  - version: 1.0
    date: 2026-03-01
    summary: >
      Complete fee mapping built from Workers Compensation (Medical Practitioner
      Fees) Order 2026 (effective 1 Feb 2026), SIRA GP rates summary, and Motor
      Accident Guidelines section 4.101. Includes WorkCover consultation rates,
      SIRA-specific payment classification codes, CTP billing rules, telehealth
      items, invoicing requirements, and GST treatment.
---

# Pricing Schedule — SIRA Fee Mapping

**Claims Doctor** · Same-day WorkCover & CTP medical certificates.

---

## 01 Purpose

This document maps every SIRA-gazetted fee and AMA-capped rate relevant to Claims Doctor's service lines. It is the single source of truth for what we can charge, how we invoice, and which payment classification codes to use. Every consultation, certificate, and ancillary service must be billed in accordance with this schedule.

---

## 02 Scope

**Applies to:** All Claims Doctor doctors, billing staff, and operations personnel.

**Covers:**

- Workers Compensation (WorkCover) GP consultation and treatment fees
- Workers Compensation certificate, ancillary, and administrative fees
- CTP (motor accident injury) consultation and treatment fees
- Telehealth billing rules across both schemes
- GST treatment
- Invoicing requirements for both schemes

**Does not cover:**

- Surgeon or orthopaedic surgeon fees (not a Claims Doctor service line)
- Allied health fees (physiotherapy, psychology, etc.)
- Medical examinations and reports ordered in dispute contexts (separate Fees Order)
- Independent medical examination (IME) fees
- Catastrophic injury rates (negotiated directly with insurer — no gazetted cap)

---

## 03 Definitions

| Term | Definition |
|------|-----------|
| AMA Fees List | The *List of Medical Services and Fees* published by the Australian Medical Association, as at the date of service delivery. Used as the fee ceiling for both WorkCover and CTP. |
| Certificate of Capacity | The SIRA-mandated certificate under s44B(3)(a) of the Workers Compensation Act 1987 for WorkCover claims. Completed in the SIRA-approved form. |
| Certificate of Fitness | The SIRA-mandated certificate for CTP (motor accident) claims under the Motor Accident Injuries Act 2017. |
| Insurer | The employer's workers compensation insurer (WorkCover) or the CTP insurer of the at-fault vehicle (CTP). |
| Medical Practitioner | A person registered in the medical profession under the Health Practitioner Regulation National Law (NSW) with AHPRA. |
| Payment Classification Code | SIRA-assigned billing code (e.g. WCO001, WCO002) for items not covered by AMA item numbers. |
| Telehealth Consultation | Delivery of medical practitioner services via videoconference or telephone, in compliance with Part 2 of the SIRA Guidelines for the Provision of Relevant Services. |
| Fees Order | The Workers Compensation (Medical Practitioner Fees) Order 2026, effective 1 February 2026. |

---

## 04 WorkCover — GP Consultation Fees

These are the maximum fees payable for GP consultations under the Workers Compensation scheme. Rates are set by the AMA Fees List and gazetted through the Fees Order. The same fee applies whether the consultation is face-to-face or via telehealth.

| AMA Item | Telehealth Item | Service | Max Fee (excl. GST) | Notes |
|----------|----------------|---------|--------------------:|-------|
| AA010 | AA010T | Level A consultation | $55.00 | Brief consultation. Minimal complexity. |
| AA020 | AA020T | Level B consultation | $112.00 | Standard consultation. Most common Claims Doctor item. |
| AA030 | AA030T | Level C consultation | $205.00 | Prolonged or complex consultation. |
| AA040 | AA040T | Level D consultation | $315.00 | Extended, high-complexity consultation. |
| AA045 | AA045T | Level E consultation | $450.00 | Lengthy, multi-system or highly complex. Rare for Claims Doctor. |

**Consultation level selection:** The level billed must reflect the service actually delivered, as defined by the AMA item descriptor (duration + complexity). You cannot upcode.

**Claims Doctor default service profile:** The vast majority of Claims Doctor WorkCover consultations will be Level B (AA020/AA020T) or Level C (AA030/AA030T). Level A is too brief for a meaningful certificate assessment. Level D and E should be exceptional.

---

## 05 WorkCover — SIRA-Specific Payment Classification Codes

These are fees set directly by SIRA, outside the AMA Fees List. They are invoiced using SIRA payment classification codes.

### 05.1 Certificate of Capacity — WCO001

| Code | Service | Max Fee | GST | Frequency |
|------|---------|--------:|-----|-----------|
| WCO001 | Initial Certificate of Capacity | $58.80 | + GST | **Once per claim only** |

- This fee covers the completion of the *initial* Certificate of Capacity only.
- Subsequent certificates are part of the consultation fee — no additional WCO001 charge.
- The certificate must be the SIRA-approved form (downloadable from sira.nsw.gov.au).

### 05.2 Recovery-at-Work Services — WCO002

| Code | Service | Max Fee | GST | Billing Unit |
|------|---------|--------:|-----|-------------|
| WCO002 | Services in addition to usual medical management | $29.40 per 5 min | + GST | To nearest 5 minutes |

Covers time spent **beyond the consultation** to support recovery at/return to work:

- Discussions with employers
- Case conferences (must include a third party beyond the worker and their support person — see Fees Order definition)
- Workplace visits
- Reviewing injury management or return-to-work plans
- Additional reports (when pre-approved by insurer)

**File notes required:** Date, duration, participants, topics, and outcomes must be documented for each WCO002 charge. This information may be audited.

### 05.3 Medical Records — WCO005

| Code | Service | Max Fee | GST | Notes |
|------|---------|--------:|-----|-------|
| WCO005 | Electronic medical records (all requested records) | $71.30 flat fee | Excl. GST | Must provide electronic if records are maintained electronically |
| WCO005 | Hard copy records (≤33 pages) | $45.30 | Excl. GST | Only if records are NOT maintained electronically |
| WCO005 | Hard copy records (>33 pages) | $45.30 + $1.40/page | Excl. GST | Per additional page beyond 33 |

- Fees are inclusive of postage and handling.
- If a doctor needs to review records to redact non-work-related information prior to provision, that review time is billable under WCO002 at the $29.40/5 min rate, in addition to the WCO005 fee.

### 05.4 Other Medical Items — WCO004

| Code | Service | Max Fee | GST | Notes |
|------|---------|--------:|-----|-------|
| WCO004 | Bandages, dressings, etc. | Cost price | Subject to GST rules | Unlikely to be a material Claims Doctor revenue line |

---

## 06 WorkCover — Nil Fee Items

The following AMA items are set to $0 under the Fees Order and **must not be billed** for WorkCover patients:

- AA007 — GP urgent attendance after hours
- AA220–AA323 — All time-based GP items
- AA501–AA670, AA850 — Enhanced primary care items
- AA340–AA343 — Shared health summary items
- AA170, AA584–AA670, AF070–AF180, AF260–AF370, AJ051–AJ200, AM210–AM240, AP050–AP278 — AMA telehealth and case conference items (SIRA has its own telehealth and case conferencing mechanisms)

**Critical for Claims Doctor:** Out-of-hours fees (AA007) are only payable for emergency attendances when the clinic is not normally open. Because Claims Doctor advertises extended hours as a core value proposition, a consultation conducted during our advertised hours **cannot** attract an out-of-hours fee regardless of the time of day.

---

## 07 CTP — Motor Accident Injury Fees

### 07.1 Fee Structure

SIRA does **not** designate specific fees for doctors treating CTP claimants. The fee ceiling is the applicable AMA Fees List rate at the time of service (Motor Accident Guidelines, section 4.101).

In practice, this means Claims Doctor bills CTP consultations at the same AMA rates as WorkCover:

| Service | Billing Basis | Max Fee |
|---------|--------------|--------:|
| GP consultation (Level A–E) | AMA item number (AA010–AA045) | Same rates as Section 04 |
| Telehealth consultation | AMA item + T suffix | Same rates as Section 04 |

### 07.2 Certificate of Fitness

There is **no** separate gazetted fee for the Certificate of Fitness under CTP. Certificate completion is considered part of the consultation service. This contrasts with WorkCover, where WCO001 pays $58.80 + GST on top of the consultation.

**Revenue implication:** CTP consultations generate less total revenue per encounter than equivalent WorkCover consultations because there is no certificate surcharge.

### 07.3 Early Intervention (Pre-Claim)

Insurers will approve payment for one GP consultation and two allied health treatment sessions once they receive notification of the injury — **before** a formal claim is lodged. This is relevant because Claims Doctor patients may present before their CTP claim is submitted.

### 07.4 Insurer Payment Terms

CTP insurers must pay within **20 calendar days** of receiving an invoice.

---

## 08 Telehealth Billing Rules

Telehealth is a core delivery channel for Claims Doctor. The rules are identical across both schemes:

1. **Item number:** Use the same AMA item as face-to-face, with a "T" suffix (e.g. AA020T for Level B telehealth).
2. **Fee:** Identical to face-to-face. No discount, no surcharge.
3. **No facility fees:** No additional fee may be charged for the telehealth consultation.
4. **Consent:** The patient must consent to telehealth delivery.
5. **Modality priority:** Videoconference preferred. Telephone permitted if video is unavailable.
6. **Email/SMS/app:** Only permitted as a supplement to a video or phone consultation, not as a standalone service.
7. **Compliance:** Must comply with Part 2 of the SIRA Guidelines for the Provision of Relevant Services (Health and Related Services).

---

## 09 Invoicing Requirements

### 09.1 WorkCover Invoicing

Every invoice submitted to a workers compensation insurer must include:

- Patient (worker) name
- Claim number
- Date of service
- Provider's AHPRA number
- Provider's Medicare provider number (if registered with Medicare)
- Provider's SIRA provider number (if applicable)
- ABN
- AMA item number or SIRA payment classification code for each service
- Fee per item
- Service duration (where applicable, e.g. WCO002)
- Date of invoice (must be on or after the last service date on the invoice)
- GST (where applicable)

**Submission deadline:** Invoices must be submitted within **30 calendar days** of the service being provided.

### 09.2 CTP Invoicing

Every invoice submitted to a CTP insurer must include:

- Patient name
- Date of motor vehicle crash
- Insurer's reference/claim number
- ABN
- AMA item number for each service
- Fee per item
- GST (where applicable)

**Payment term:** Insurer must pay within **20 calendar days** of receipt.

---

## 10 GST Treatment

| Item | GST Status |
|------|-----------|
| GP consultations (AA010–AA045, face-to-face and telehealth) | GST-free (medical service) |
| Certificate of Capacity (WCO001) | **Subject to GST** — it is an administrative service, not a medical service |
| Recovery-at-work services (WCO002) | **Subject to GST** |
| Medical records (WCO005) | GST-free |
| Other medical items (WCO004) | Subject to GST rules for the specific item |

**Important:** The consultation fee itself is GST-free. The WCO001 certificate fee and WCO002 services attract GST on top of the stated maximum. Claims Doctor must be registered for GST and issue tax invoices where applicable.

---

## 11 Claims Doctor Revenue Model Summary

This section maps SIRA fees to Claims Doctor's expected revenue per encounter.

### 11.1 WorkCover Encounter — Typical

| Line Item | Code | Amount |
|-----------|------|-------:|
| Level B consultation | AA020 | $112.00 |
| Initial Certificate of Capacity | WCO001 | $58.80 + GST |
| **Total (initial visit)** | | **$176.68 incl. GST on cert** |

For subsequent visits (no WCO001):

| Line Item | Code | Amount |
|-----------|------|-------:|
| Level B consultation | AA020 | $112.00 |
| **Total (follow-up)** | | **$112.00** |

### 11.2 CTP Encounter — Typical

| Line Item | Code | Amount |
|-----------|------|-------:|
| Level B consultation | AA020 | $112.00 |
| Certificate of Fitness | — | Included in consultation |
| **Total** | | **$112.00** |

### 11.3 Revenue Uplift Opportunities (Per Encounter)

| Opportunity | Code | Conditions | Potential Add |
|-------------|------|-----------|-------------:|
| Upgrade to Level C | AA030 | Justified by complexity and duration | +$93.00 |
| RTW support time (15 min) | WCO002 | Pre-approved by insurer; documented | +$88.20 + GST |
| Medical records request | WCO005 | Requested by insurer | +$71.30 |

---

## 12 Fee Indexation and Update Protocol

- WorkCover fees are updated by SIRA annually, typically effective 1 February.
- The AMA Fees List is updated by the AMA independently.
- CTP fees track AMA rates automatically — no separate SIRA action required.

**Process:** When SIRA publishes a new Fees Order (usually gazetted in the NSW Government Gazette in January each year):

1. Compare new rates against this document.
2. Update all fee tables in this document.
3. Bump version (minor bump for indexation-only changes; major bump if structural changes to billing rules).
4. Notify all Claims Doctor doctors and billing staff.
5. Update billing system fee schedules.
6. Review all dependent documents (CD-FIN-001, CD-OPS-007).

**Current rates effective:** 1 February 2026, per the Workers Compensation (Medical Practitioner Fees) Order 2026.

---

## 13 Source Documents

| Document | Authority | Effective Date | URL |
|----------|-----------|---------------|-----|
| Workers Compensation (Medical Practitioner Fees) Order 2026 | SIRA | 1 Feb 2026 | [sira.nsw.gov.au](https://www.sira.nsw.gov.au/__data/assets/pdf_file/0004/1398073/2026-Workers-Compensation-Medical-Practitioner-Fees-Order.pdf) |
| GP Rates Summary — effective 1 Nov 2025 | SIRA | 1 Nov 2025 | [sira.nsw.gov.au](https://www.sira.nsw.gov.au/__data/assets/pdf_file/0007/1392289/General-practitioner-rates-effective-1-Nov-2025.pdf) |
| Motor Accident Guidelines — section 4.101 | SIRA | Current | [sira.nsw.gov.au](https://www.sira.nsw.gov.au/resources-library/motor-accident-resources/publications/for-professionals/motor-accident-guidelines#part4) |
| Fees paid for motor crash health services | SIRA | Current | [sira.nsw.gov.au](https://www.sira.nsw.gov.au/health-providers/fees-paid-for-motor-crash-health-services) |
| Guidelines for the Provision of Relevant Services (Health and Related Services) | SIRA | Current | [sira.nsw.gov.au](https://www.sira.nsw.gov.au/fraud-and-regulation/new-regulation-for-health-and-related-services-in-workers-compensation-and-ctp-schemes/guidelines-for-the-provision-of-relevant-services-health-and-related-services) |

---

## 14 Related Documents

| Doc ID | Title | Relationship |
|--------|-------|-------------|
| CD-FIN-001 | Financial Model | Depends on this document for revenue assumptions |
| CD-FIN-003 | Cash Flow Forecast | Depends on CD-FIN-001 which depends on this |
| CD-OPS-002 | Service Catalogue | Depends on this document for service pricing |
| CD-OPS-007 | Billing & Invoicing SOP | Depends on this document for invoicing rules |
| CD-MKT-005 | Google Ads Playbook | Depends on this document for CPA/ROAS targets |
| CD-GOV-003 | Clinical Protocols / Practice Guidelines | Informs consultation level selection |

---

## 15 Review & Approval

| Role | Name | Date | Signature |
|------|------|------|-----------|
| Author | Claude (AI) + Robert Laidlaw | 2026-03-01 | |
| Reviewer | | | |
| Approver | Robert Laidlaw | | |

---

**Claims Doctor** · claimsdoctor.com.au
ABN 39 674 905 376 · Level 1/457-459 Elizabeth Street, Surry Hills NSW 2010

_This document is the property of Claims Doctor. Unauthorised distribution is prohibited._
_Document ID: CD-FIN-002 · Version 1.0 · Status: ACTIVE · Visibility: INTERNAL_
