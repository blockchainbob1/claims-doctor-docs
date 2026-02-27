---
doc_id: CD-PAT-004
title: Post-Consultation Summary Template
version: 0.2
status: DRAFT
visibility: EXTERNAL
owner: Robert Laidlaw
last_updated: 2026-02-28
approved_date: null
next_review: 2026-08-28
dependencies:
  - CD-OPS-008
changelog:
  - version: 0.2
    date: 2026-02-28
    summary: Full draft. Patient-facing template with merge fields and conditional logic for WorkCover/CTP. Sections A-G covering patient details, consultation summary, certificate issued, next steps, rights/privacy, and contact. Usage rules and conditional logic reference for tech implementation.
  - version: 0.1
    date: 2026-02-27
    summary: Initial draft created (placeholder)
---

# Post-Consultation Summary Template

**Claims Doctor** · Same-day WorkCover & CTP medical certificates.

---

## 01 Purpose

This template defines the standard format for the summary provided to every patient after their Claims Doctor telehealth consultation. It ensures patients leave with a clear, written record of what was discussed, what certificate was issued, and what happens next.

---

## 02 Scope

**Applies to:** Every completed Claims Doctor consultation (WorkCover and CTP).

**Delivered by:** Automatically generated post-consultation and sent to the patient via their preferred contact method (email or SMS link).

**Does not cover:** Clinical notes retained in the medical record (these are governed by CD-GOV-004). This document is the patient-facing summary only.

---

## 03 Definitions

| Term | Definition |
|------|-----------|
| Certificate of Capacity | The SIRA-mandated document issued following a WorkCover injury assessment, detailing work capacity and restrictions |
| Certificate of Fitness | The SIRA-mandated document issued following a CTP motor accident injury assessment |
| Nominated Treating Doctor (NTD) | The doctor nominated by the patient to manage their ongoing injury claim |
| SIRA | State Insurance Regulatory Authority (NSW) |

---

## 04 Template

> **INSTRUCTIONS FOR USE:** Fields in `[SQUARE BRACKETS]` are dynamic merge fields populated from the consultation record. Fields in `{CURLY BRACES}` are conditional blocks — include only when the condition applies.

---

### HEADER

**Claims Doctor**
Post-Consultation Summary

**Date issued:** [CONSULTATION_DATE]
**Reference:** [CONSULTATION_REFERENCE_ID]

---

### SECTION A — YOUR DETAILS

| | |
|---|---|
| **Name** | [PATIENT_FULL_NAME] |
| **Date of birth** | [PATIENT_DOB] |
| **Claim number** | [CLAIM_NUMBER] |
| **Claim type** | [WorkCover / CTP] |
| **Insurer** | [INSURER_NAME] |

---

### SECTION B — CONSULTATION DETAILS

| | |
|---|---|
| **Consulting doctor** | Dr [DOCTOR_FULL_NAME] |
| **AHPRA registration** | [DOCTOR_AHPRA_NUMBER] |
| **Date & time** | [CONSULTATION_DATETIME] |
| **Consultation type** | Telehealth (video) |
| **Duration** | [CONSULTATION_DURATION] minutes |

---

### SECTION C — SUMMARY OF YOUR CONSULTATION

**Presenting condition(s):**

[PRESENTING_CONDITIONS — plain-language summary of the injury or condition discussed, as documented during the consultation]

**Key points discussed:**

[CONSULTATION_KEY_POINTS — brief summary of what was covered during the consultation, written in plain language the patient can understand]

---

### SECTION D — CERTIFICATE ISSUED

| | |
|---|---|
| **Certificate type** | [Certificate of Capacity / Certificate of Fitness] |
| **Certificate date** | [CERTIFICATE_DATE] |
| **Period covered** | [CERTIFICATE_START_DATE] to [CERTIFICATE_END_DATE] |

{IF WORKCOVER}

| | |
|---|---|
| **Current work capacity** | [FULL CAPACITY / SUITABLE DUTIES / NO CURRENT CAPACITY] |
| **Hours per week (suitable duties)** | [SUITABLE_DUTIES_HOURS — if applicable] |
| **Restrictions** | [WORK_RESTRICTIONS — if applicable] |

{END IF WORKCOVER}

{IF CTP}

| | |
|---|---|
| **Fitness for work** | [FIT / UNFIT / FIT WITH RESTRICTIONS] |
| **Treatment recommended** | [TREATMENT_RECOMMENDATIONS — if applicable] |

{END IF CTP}

**Your certificate has been:** [Sent to your insurer / Provided to you for submission — per patient preference]

---

### SECTION E — WHAT HAPPENS NEXT

{IF REVIEW_REQUIRED}

**Review consultation required**

Your certificate covers you until **[CERTIFICATE_END_DATE]**. If your injury is still affecting your work capacity after this date, you will need a review consultation to extend your certificate.

We will contact you **[REVIEW_CONTACT_DATE]** to arrange your next appointment. You can also book your review at any time by contacting us.

{END IF REVIEW_REQUIRED}

{IF NO_REVIEW_REQUIRED}

**No further action required from you**

Based on today's consultation, no follow-up is currently needed. If your condition changes or you need a new certificate in the future, you can contact us at any time.

{END IF NO_REVIEW_REQUIRED}

**Ongoing care:** This consultation does not replace your regular GP or treating doctor. For ongoing treatment, prescriptions, or referrals, please continue to see your nominated treating doctor or GP.

---

### SECTION F — IMPORTANT INFORMATION

**About your certificate**

Your medical certificate is a legal document. It has been completed based on the clinical information you provided during your consultation. If any of the information on your certificate is incorrect, contact us within 24 hours so we can review and correct it.

**Your rights**

- You have the right to access your medical records held by Claims Doctor. To request access, email privacy@claimsdoctor.com.au.
- If you are unhappy with any aspect of your consultation or certificate, you can lodge a complaint by emailing complaints@claimsdoctor.com.au or calling us on [PHONE_NUMBER]. See our Complaints & Feedback Policy for more information.
- You can change your nominated treating doctor at any time by notifying your insurer.

**Privacy**

Your personal and health information is handled in accordance with the *Privacy Act 1988* (Cth), the *Health Records and Information Privacy Act 2002* (NSW), and our Privacy Policy at claimsdoctor.com.au/privacy.

---

### SECTION G — CONTACT US

| | |
|---|---|
| **Phone** | [PHONE_NUMBER] |
| **Email** | hello@claimsdoctor.com.au |
| **Website** | claimsdoctor.com.au |
| **Hours** | Monday–Friday, [OPERATING_HOURS] |

If you need urgent medical attention, call **000** or go to your nearest emergency department. Claims Doctor does not provide emergency medical services.

---

### FOOTER

_This summary is provided for your records. It does not constitute a clinical record and should not be used as a substitute for medical advice from your treating doctor._

_Claims Doctor · ABN 39 674 905 376 · Level 1/457-459 Elizabeth Street, Surry Hills NSW 2010_

---

## 05 Template Usage Rules

1. **Every completed consultation** must generate a post-consultation summary. No exceptions.
2. **Sent within 1 hour** of consultation completion. Target: immediate (automated).
3. **Plain language only.** No medical jargon without explanation. Aim for reading level of Year 8 or below.
4. **Accuracy check.** The consulting doctor must verify the certificate details (Section D) match the issued certificate before the summary is released.
5. **No clinical advice.** This summary records what happened — it does not provide new medical advice or recommendations beyond what was discussed in the consultation.
6. **Delivery method.** Email by default. SMS link to secure portal as fallback. Patient preference recorded at intake.
7. **Retention.** A copy of every issued summary is retained in the patient record for the period required under NSW health records legislation (minimum 7 years from last consultation for adults; until age 25 for minors).

---

## 06 Conditional Logic Reference

For implementation in the technology stack (see CD-OPS-011):

| Condition | Field | Trigger |
|-----------|-------|---------|
| WorkCover block | `claim_type = "WorkCover"` | Show Section D WorkCover fields |
| CTP block | `claim_type = "CTP"` | Show Section D CTP fields |
| Review required | `review_required = true` | Show "Review consultation required" in Section E |
| No review required | `review_required = false` | Show "No further action required" in Section E |

---

## 07 Related Documents

| Doc ID | Title | Relationship |
|--------|-------|-------------|
| CD-OPS-008 | Post-Consult Follow-Up SOP | Depends on — governs when and how this template is triggered |
| CD-GOV-004 | Medical Records Management Policy | Informs — governs retention of clinical records (this template is patient-facing, not the clinical record) |
| CD-BRD-001 | Brand & Style Guide | Informs — visual formatting and tone of patient communications |
| CD-LEG-004 | Privacy Policy | Referenced — linked in Section F |
| CD-LEG-009 | Complaints & Feedback Policy | Referenced — linked in Section F |
| CD-PAT-005 | Certificate Explanation Guide | Related — can be linked alongside this summary for patients wanting more detail |

---

## 08 Review & Approval

| Role | Name | Date | Signature |
|------|------|------|-----------|
| Author | Claude (AI) / Robert Laidlaw | 2026-02-28 | |
| Reviewer | | | |
| Approver | Robert Laidlaw | | |

---

**Claims Doctor** · claimsdoctor.com.au
ABN 39 674 905 376 · Level 1/457-459 Elizabeth Street, Surry Hills NSW 2010

_This document is the property of Claims Doctor. Unauthorised distribution is prohibited._
_Document ID: CD-PAT-004 · Version 0.2 · Status: DRAFT · Visibility: EXTERNAL_
