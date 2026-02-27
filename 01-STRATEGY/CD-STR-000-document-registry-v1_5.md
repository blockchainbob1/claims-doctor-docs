---
doc_id: CD-STR-000
title: Claims Doctor Document Registry
version: 1.5
status: ACTIVE
visibility: INTERNAL
owner: Robert Laidlaw
last_updated: 2026-02-27
approved_date: 2026-02-27
next_review: 2026-05-27
dependencies: []
changelog:
  - version: 1.5
    date: 2026-02-27
    summary: Updated OPS-001 (Standard Operating Procedures Master) to DRAFT v0.1. Full draft with three-stage operating model (Pilot/Consolidate/Scale), stage gate criteria, workflow ownership matrix, automation triggers, escalation framework, and metrics.
  - version: 1.4
    date: 2026-02-27
    summary: Updated MKT-005 (Google Ads Playbook) to DRAFT v0.2. Full playbook drafted with campaign architecture, keyword strategy, ad copy, budget model, AHPRA compliance framework. Added CD-BRD-001 as dependency.
  - version: 1.3
    date: 2026-02-27
    summary: Full repo audit. Updated GOV-001 to DRAFT v0.1, MKT-002 to DRAFT v0.2, STR-000 self-reference corrected to v1.3. FIN-002 already tracked at DRAFT v0.1. Statistics corrected.
  - version: 1.2
    date: 2026-02-27
    summary: Updated LEG-011 (Informed Consent Template) to DRAFT v0.1. Consolidates telehealth consent, informed consent, and third-party disclosure into single patient-facing form. Replaces Appendix A of LEG-008.
  - version: 1.1
    date: 2026-02-27
    summary: Updated LEG-004 and LEG-008 to DRAFT status. Moved LEG-008 to correct folder. Added DRAFT count to statistics.
  - version: 1.0
    date: 2026-02-27
    summary: Initial registry created with full document inventory
---

# Claims Doctor Document Registry

**Claims Doctor** · Same-day WorkCover & CTP medical certificates.

---

## 01 Purpose

This is the master index of all Claims Doctor business documents. Every document created must be registered here. This registry is the single source of truth for document IDs, versions, statuses, and dependencies.

---

## 02 Naming Convention

All filenames follow: `CD-[CAT]-[###]-[short-name]-v[MAJOR].[MINOR].md`

### Category Codes

| Code | Domain | Folder |
|------|--------|--------|
| STR | Strategy & Planning | 01-STRATEGY |
| FIN | Financial | 02-FINANCIAL |
| MKT | Marketing & Growth | 03-MARKETING |
| SAL | Sales & Partnerships | 04-SALES |
| OPS | Operations & Service Delivery | 05-OPERATIONS |
| GOV | Clinical Governance | 06-GOVERNANCE |
| LEG | Compliance & Legal | 07-LEGAL |
| HR | HR & Team | 08-HR |
| PAT | Patient-Facing | 09-PATIENT-FACING |
| RPT | Reporting & Measurement | 10-REPORTING |
| BRD | Brand | 11-BRAND |

### Versioning Rules

- **v0.x** — Draft. Not approved for operational use.
- **v1.0** — First approved version. Live and operational.
- **Major bump (v1.0 → v2.0)** — Material change to scope, policy, or requirements.
- **Minor bump (v1.0 → v1.1)** — Clarifications, formatting, typos. No substantive change.

### Status Values

| Status | Meaning |
|--------|---------|
| DRAFT | Work in progress. Not approved for use. |
| ACTIVE | Approved and currently operational. |
| UNDER REVIEW | Approved but undergoing revision. Current version still valid. |
| SUPERSEDED | Replaced by a newer document. Reference the replacement. |
| RETIRED | No longer applicable. Retained for records only. |

### Visibility Values

| Visibility | Meaning |
|------------|---------|
| INTERNAL | For Claims Doctor team use only. Not to be shared externally. |
| EXTERNAL | Approved for publication or sharing with patients, partners, or the public. |

---

## 03 Dependency Rules

When a document is bumped to a new **major** version, every document that lists it as a dependency MUST be reviewed and updated if affected. This is non-negotiable.

---

## 04 Document Register

### STR — Strategy & Planning

| Doc ID | Title | Version | Status | Visibility | Owner | Dependencies |
|--------|-------|---------|--------|------------|-------|-------------|
| CD-STR-000 | Document Registry | 1.3 | ACTIVE | INTERNAL | Robert Laidlaw | — |
| CD-STR-001 | Business Plan | — | NOT STARTED | INTERNAL | Robert Laidlaw | CD-FIN-001, CD-MKT-001 |
| CD-STR-002 | Lean Canvas / Strategic Summary | — | NOT STARTED | INTERNAL | Robert Laidlaw | CD-STR-001 |
| CD-STR-003 | Competitive Landscape Analysis | — | NOT STARTED | INTERNAL | Robert Laidlaw | — |
| CD-STR-004 | SWOT / Risk Register | — | NOT STARTED | INTERNAL | Robert Laidlaw | CD-STR-003 |

### FIN — Financial

| Doc ID | Title | Version | Status | Visibility | Owner | Dependencies |
|--------|-------|---------|--------|------------|-------|-------------|
| CD-FIN-001 | Financial Model | — | NOT STARTED | INTERNAL | Robert Laidlaw | CD-FIN-002 |
| CD-FIN-002 | Pricing Schedule (SIRA Fee Mapping) | 0.1 | DRAFT | INTERNAL | Robert Laidlaw | — |
| CD-FIN-003 | Cash Flow Forecast | — | NOT STARTED | INTERNAL | Robert Laidlaw | CD-FIN-001 |
| CD-FIN-004 | Startup Cost Register / Budget | — | NOT STARTED | INTERNAL | Robert Laidlaw | — |

### MKT — Marketing & Growth

| Doc ID | Title | Version | Status | Visibility | Owner | Dependencies |
|--------|-------|---------|--------|------------|-------|-------------|
| CD-MKT-001 | Marketing Plan | — | NOT STARTED | INTERNAL | Robert Laidlaw | CD-MKT-002, CD-MKT-003, CD-BRD-001 |
| CD-MKT-002 | ICP & Persona Profiles | 0.2 | DRAFT | INTERNAL | Robert Laidlaw | — |
| CD-MKT-003 | SEO/GEO Strategy | — | NOT STARTED | INTERNAL | Robert Laidlaw | CD-MKT-002 |
| CD-MKT-004 | Content Calendar / Editorial Plan | — | NOT STARTED | INTERNAL | Robert Laidlaw | CD-MKT-001, CD-MKT-003 |
| CD-MKT-005 | Google Ads Playbook | 0.2 | DRAFT | INTERNAL | Robert Laidlaw | CD-MKT-002, CD-FIN-002, CD-BRD-001 |
| CD-MKT-006 | Social Media Strategy | — | NOT STARTED | INTERNAL | Robert Laidlaw | CD-MKT-002, CD-BRD-001 |
| CD-MKT-007 | Referral Partner Strategy | — | NOT STARTED | INTERNAL | Robert Laidlaw | CD-SAL-001 |
| CD-MKT-008 | Email/SMS Nurture Sequences | — | NOT STARTED | INTERNAL | Robert Laidlaw | CD-MKT-002, CD-BRD-001 |

### SAL — Sales & Partnerships

| Doc ID | Title | Version | Status | Visibility | Owner | Dependencies |
|--------|-------|---------|--------|------------|-------|-------------|
| CD-SAL-001 | B2B Sales Playbook | — | NOT STARTED | INTERNAL | Robert Laidlaw | CD-MKT-002 |
| CD-SAL-002 | Partner Information Pack / One-Pager | — | NOT STARTED | EXTERNAL | Robert Laidlaw | CD-BRD-001 |
| CD-SAL-003 | Referral Agreement Template | — | NOT STARTED | EXTERNAL | Robert Laidlaw | CD-LEG-001 |
| CD-SAL-004 | Case for Partnership Deck | — | NOT STARTED | EXTERNAL | Robert Laidlaw | CD-SAL-001, CD-BRD-001 |

### OPS — Operations & Service Delivery

| Doc ID | Title | Version | Status | Visibility | Owner | Dependencies |
|--------|-------|---------|--------|------------|-------|-------------|
| CD-OPS-001 | Standard Operating Procedures (Master) | 0.1 | DRAFT | INTERNAL | Robert Laidlaw | CD-GOV-001, CD-OPS-002 |
| CD-OPS-002 | Service Catalogue | — | NOT STARTED | INTERNAL | Robert Laidlaw | CD-FIN-002 |
| CD-OPS-003 | Patient Intake & Triage SOP | — | NOT STARTED | INTERNAL | Robert Laidlaw | CD-OPS-001 |
| CD-OPS-004 | Consultation Booking SOP | — | NOT STARTED | INTERNAL | Robert Laidlaw | CD-OPS-001 |
| CD-OPS-005 | Doctor Onboarding & Credentialing SOP | — | NOT STARTED | INTERNAL | Robert Laidlaw | CD-GOV-002, CD-OPS-001 |
| CD-OPS-006 | Certificate Issuance SOP | — | NOT STARTED | INTERNAL | Robert Laidlaw | CD-OPS-001, CD-GOV-003 |
| CD-OPS-007 | Billing & Invoicing SOP | — | NOT STARTED | INTERNAL | Robert Laidlaw | CD-FIN-002, CD-OPS-001 |
| CD-OPS-008 | Post-Consult Follow-Up SOP | — | NOT STARTED | INTERNAL | Robert Laidlaw | CD-OPS-001 |
| CD-OPS-009 | Complaint Handling SOP | — | NOT STARTED | INTERNAL | Robert Laidlaw | CD-LEG-008, CD-OPS-001 |
| CD-OPS-010 | Adverse Event Management SOP | — | NOT STARTED | INTERNAL | Robert Laidlaw | CD-GOV-005, CD-OPS-001 |
| CD-OPS-011 | Technology Stack Documentation | — | NOT STARTED | INTERNAL | Robert Laidlaw | — |
| CD-OPS-012 | Business Continuity / Disaster Recovery Plan | — | NOT STARTED | INTERNAL | Robert Laidlaw | CD-OPS-011 |

### GOV — Clinical Governance

| Doc ID | Title | Version | Status | Visibility | Owner | Dependencies |
|--------|-------|---------|--------|------------|-------|-------------|
| CD-GOV-001 | Clinical Governance Framework | 0.1 | DRAFT | INTERNAL | Robert Laidlaw | — |
| CD-GOV-002 | Credentialing & Privileging Policy | — | NOT STARTED | INTERNAL | Robert Laidlaw | CD-GOV-001 |
| CD-GOV-003 | Clinical Protocols / Practice Guidelines | — | NOT STARTED | INTERNAL | Robert Laidlaw | CD-GOV-001 |
| CD-GOV-004 | Medical Records Management Policy | — | NOT STARTED | INTERNAL | Robert Laidlaw | CD-GOV-001, CD-LEG-004 |
| CD-GOV-005 | Incident Reporting & Management Policy | — | NOT STARTED | INTERNAL | Robert Laidlaw | CD-GOV-001 |
| CD-GOV-006 | Medication Management Policy | — | NOT STARTED | INTERNAL | Robert Laidlaw | CD-GOV-001 |
| CD-GOV-007 | Infection Control Policy | — | NOT STARTED | INTERNAL | Robert Laidlaw | CD-GOV-001 |

### LEG — Compliance & Legal

| Doc ID | Title | Version | Status | Visibility | Owner | Dependencies |
|--------|-------|---------|--------|------------|-------|-------------|
| CD-LEG-001 | AHPRA Advertising Compliance Checklist | — | NOT STARTED | INTERNAL | Robert Laidlaw | CD-BRD-001 |
| CD-LEG-002 | SIRA Compliance Manual | — | NOT STARTED | INTERNAL | Robert Laidlaw | CD-GOV-003 |
| CD-LEG-003 | TGA Compliance Checklist | — | NOT STARTED | INTERNAL | Robert Laidlaw | CD-BRD-001 |
| CD-LEG-004 | Privacy Policy (Website) | 0.1 | DRAFT | EXTERNAL | Robert Laidlaw | — |
| CD-LEG-005 | Patient Privacy & Data Handling Policy | — | NOT STARTED | INTERNAL | Robert Laidlaw | CD-LEG-004 |
| CD-LEG-006 | Terms of Service / Patient Agreement | — | NOT STARTED | EXTERNAL | Robert Laidlaw | — |
| CD-LEG-007 | Website Terms & Conditions | — | NOT STARTED | EXTERNAL | Robert Laidlaw | — |
| CD-LEG-008 | Telehealth Consent Policy | 0.1 | DRAFT | INTERNAL | Robert Laidlaw | CD-GOV-001 |
| CD-LEG-009 | Complaints & Feedback Policy | — | NOT STARTED | INTERNAL | Robert Laidlaw | CD-GOV-001 |
| CD-LEG-010 | Whistleblower Policy | — | NOT STARTED | INTERNAL | Robert Laidlaw | — |
| CD-LEG-011 | Informed Consent Template | 0.1 | DRAFT | EXTERNAL | Robert Laidlaw | CD-LEG-008, CD-GOV-001 |

### HR — HR & Team

| Doc ID | Title | Version | Status | Visibility | Owner | Dependencies |
|--------|-------|---------|--------|------------|-------|-------------|
| CD-HR-001 | Doctor Engagement / Contractor Agreement | — | NOT STARTED | INTERNAL | Robert Laidlaw | CD-GOV-002 |
| CD-HR-002 | Position Descriptions | — | NOT STARTED | INTERNAL | Robert Laidlaw | — |
| CD-HR-003 | Onboarding Checklist (Doctors) | — | NOT STARTED | INTERNAL | Robert Laidlaw | CD-OPS-005, CD-GOV-002 |
| CD-HR-004 | Code of Conduct | — | NOT STARTED | INTERNAL | Robert Laidlaw | — |
| CD-HR-005 | Work Health & Safety Policy | — | NOT STARTED | INTERNAL | Robert Laidlaw | — |

### PAT — Patient-Facing

| Doc ID | Title | Version | Status | Visibility | Owner | Dependencies |
|--------|-------|---------|--------|------------|-------|-------------|
| CD-PAT-001 | Patient Information Sheet — WorkCover | — | NOT STARTED | EXTERNAL | Robert Laidlaw | CD-OPS-003, CD-BRD-001 |
| CD-PAT-002 | Patient Information Sheet — CTP | — | NOT STARTED | EXTERNAL | Robert Laidlaw | CD-OPS-003, CD-BRD-001 |
| CD-PAT-003 | FAQ Document | — | NOT STARTED | EXTERNAL | Robert Laidlaw | CD-OPS-002 |
| CD-PAT-004 | Post-Consultation Summary Template | — | NOT STARTED | EXTERNAL | Robert Laidlaw | CD-OPS-008 |
| CD-PAT-005 | Certificate Explanation Guide | — | NOT STARTED | EXTERNAL | Robert Laidlaw | CD-BRD-001 |

### RPT — Reporting & Measurement

| Doc ID | Title | Version | Status | Visibility | Owner | Dependencies |
|--------|-------|---------|--------|------------|-------|-------------|
| CD-RPT-001 | KPI Dashboard Specification | — | NOT STARTED | INTERNAL | Robert Laidlaw | CD-STR-001 |
| CD-RPT-002 | Monthly Business Review Template | — | NOT STARTED | INTERNAL | Robert Laidlaw | CD-RPT-001 |
| CD-RPT-003 | Marketing Attribution Model | — | NOT STARTED | INTERNAL | Robert Laidlaw | CD-MKT-001, CD-OPS-011 |

### BRD — Brand

| Doc ID | Title | Version | Status | Visibility | Owner | Dependencies |
|--------|-------|---------|--------|------------|-------|-------------|
| CD-BRD-001 | Brand & Style Guide | 1.0 | ACTIVE | INTERNAL | Robert Laidlaw | — |

---

## 05 Statistics

| Metric | Count |
|--------|-------|
| Total documents registered | 56 |
| ACTIVE | 2 |
| DRAFT | 8 |
| NOT STARTED | 46 |
| EXTERNAL visibility | 10 |
| INTERNAL visibility | 46 |

---

**Claims Doctor** · claimsdoctor.com.au
ABN 39 674 905 376 · Level 1/457-459 Elizabeth Street, Surry Hills NSW 2010

_This document is the property of Claims Doctor. Unauthorised distribution is prohibited._
_Document ID: CD-STR-000 · Version 1.5 · Status: ACTIVE · Visibility: INTERNAL_
