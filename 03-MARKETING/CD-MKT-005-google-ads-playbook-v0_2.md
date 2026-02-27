---
doc_id: CD-MKT-005
title: Google Ads Playbook
version: 0.2
status: DRAFT
visibility: INTERNAL
owner: Robert Laidlaw
last_updated: 2026-02-27
approved_date: null
next_review: 2026-08-27
dependencies:
  - CD-MKT-002
  - CD-FIN-002
  - CD-BRD-001
changelog:
  - version: 0.1
    date: 2026-02-27
    summary: Placeholder created
  - version: 0.2
    date: 2026-02-27
    summary: Full playbook drafted — campaign architecture, keyword strategy, ad copy, budget model, compliance framework, and measurement plan
---

# Google Ads Playbook

**Claims Doctor** · Same-day WorkCover & CTP medical certificates.

---

## 01 Purpose

This document is the operational blueprint for Claims Doctor's Google Ads campaigns. It translates the ICPs defined in CD-MKT-002 into campaigns, ad groups, keywords, ad copy, landing page assignments, budget allocations, and performance targets. It also codifies AHPRA and Google Healthcare advertising compliance requirements so every ad we run is defensible.

Google Ads is the primary patient acquisition channel pre-revenue. SEO and GEO take months to compound. Referral partnerships take time to build. Google Ads turns on immediately. This is the channel that gets patients through the door in week one.

---

## 02 Scope

**Applies to:** All paid search activity on Google Ads for Claims Doctor.

**Geographic scope:** New South Wales only. All campaigns geo-target NSW postcodes. No national spend.

**Channels covered:** Google Search Network only at launch. Display Network, YouTube, Performance Max, and Demand Gen are excluded until Search campaigns are profitable and stable (see Section 16 for expansion criteria).

**What this does NOT cover:** Organic SEO strategy (see CD-MKT-003), social media advertising (see CD-MKT-006), or referral partner marketing (see CD-MKT-007).

---

## 03 Definitions

| Term | Definition |
|------|-----------|
| Certificate of Capacity | The SIRA-mandated document for WorkCover injury assessment |
| Certificate of Fitness | The SIRA-mandated document for CTP injury assessment |
| SIRA | State Insurance Regulatory Authority — regulator of NSW workers compensation and CTP schemes |
| CPC | Cost Per Click — the amount paid each time someone clicks an ad |
| CTR | Click-Through Rate — percentage of impressions that result in a click |
| CVR | Conversion Rate — percentage of clicks that result in a conversion (booking) |
| CPA | Cost Per Acquisition — total spend divided by total conversions |
| ROAS | Return on Ad Spend — revenue generated per dollar spent on ads |
| Quality Score | Google's 1–10 rating of ad relevance, landing page quality, and expected CTR |
| AHPRA | Australian Health Practitioner Regulation Agency — regulates health practitioner advertising |
| NTD | Nominated Treating Doctor — the doctor a worker nominates to manage their WorkCover claim |

---

## 04 Market Context & Benchmarks

### 04.1 Healthcare Advertising Benchmarks (Australia, 2025–26)

| Metric | Healthcare Average | Physicians/Surgeons | Claims Doctor Target |
|--------|-------------------|---------------------|---------------------|
| CPC (Search) | $2.50–$4.00 AUD | ~$5.00 AUD | $3.00–$6.00 AUD |
| CTR (Search) | 3.27% | 6.73% | 5.00%+ |
| Conversion Rate | 3.36% | 11.62% | 8.00%+ |
| CPM (Display) | $36.82 | — | N/A (Search only at launch) |

Healthcare has the highest CPM of any industry — roughly double the all-industry average of $17.80. However, physicians and surgeons see strong conversion rates (11.62%), which makes the economics work despite premium CPCs.

The legal services crossover is relevant: personal injury lawyers bid $50–$137+ on WorkCover-adjacent keywords. We are competing for some of the same search intent ("WorkCover claim help", "workers comp doctor") but our CPC ceiling is materially lower because we're a medical service, not a legal one.

### 04.2 Competitive Landscape

**AusRehab** is the dominant paid search competitor in the telehealth WorkCover certificate space. They run on "certificate of capacity", "WorkCover doctor telehealth", and state-by-state variants. Their messaging: 24–48 hour appointments, bulk billing with active claim, telehealth across all states. They have 50+ pages and 30+ blog posts feeding Quality Score through content depth.

**WorkCover Doctor** (workcover.doctor) trades on exact-match brand/keyword domain alignment. 99.7% claim success rate messaging.

**Sydney Injury Doctors** plays local SEO in Western Sydney (Auburn). In-person + telehealth hybrid.

**Claims Doctor's wedge:** Same-day appointments (not 24–48 hours), SIRA-specialist doctors (not generalists), and digital certificate delivery. Speed is the differentiator. Every ad and landing page must hammer "same-day" because no competitor currently owns that position.

### 04.3 Market Education Challenge

There is active misinformation in the market that WorkCover certificates "can't be issued via telehealth." This is factually wrong per SIRA guidelines, but it influences searcher behaviour. Our ads and landing pages must address this objection proactively — not defensively, but with authority. Cite SIRA directly. The content strategy (see claims-doctor-content-strategy.md, Page 19: "WorkCover Telehealth: What You Need to Know") builds the educational landing page for this.

---

## 05 Campaign Architecture

### 05.1 Account Structure Overview

The account follows a tiered architecture: two audience groups (B2C injured workers searching for themselves, and B2B referral partners searching for a service to recommend) with campaigns segmented by service line and intent level.

| Campaign | Audience | Intent | Priority |
|----------|----------|--------|----------|
| WC-Search-High-Intent | B2C — Injured workers | Transactional — need a doctor now | 1 (Launch) |
| CTP-Search-High-Intent | B2C — CTP claimants | Transactional — need a doctor now | 2 (Launch) |
| WC-Search-Informational | B2C — Injured workers | Research — learning about certificates/claims | 3 (Week 4) |
| B2B-Search-Referral | B2B — Lawyers, rehab, physios, labour hire, GPs | Looking for a service to refer patients to | 4 (Week 6) |
| Brand-Defence | Both | Searching for "Claims Doctor" by name | 5 (When brand volume emerges) |

Launch with Campaigns 1 and 2 only. Add campaigns 3–5 as budget and landing pages allow.

### 05.2 Campaign Settings (All Campaigns)

| Setting | Value | Rationale |
|---------|-------|-----------|
| Network | Search only | No Search Partners, no Display opt-in |
| Location | New South Wales, Australia | Geo-target NSW only. Exclude all other states. |
| Location option | "Presence: People in or regularly in your targeted locations" | Exclude "Interest in" to avoid interstate waste |
| Language | English | — |
| Bid strategy | Manual CPC (launch) → Target CPA (once 30+ conversions) | Manual for control during learning phase |
| Ad rotation | Optimise for clicks (launch) → Optimise for conversions (post-learning) | — |
| Ad schedule | Mon–Fri 7am–9pm, Sat 8am–2pm AEST | Match booking availability; no spend when no one can answer |
| Device | All devices, no bid adjustments initially | Review device performance at Week 4 |

---

## 06 Campaign 1 — WC-Search-High-Intent

This is the money campaign. It targets injured workers (or their family/advocates) actively searching for a WorkCover doctor, certificate of capacity, or same-day medical consultation for a workplace injury.

### 06.1 Ad Groups & Keywords

**Ad Group 1A: WorkCover Doctor**

| Match Type | Keywords |
|------------|----------|
| Phrase | "workcover doctor" |
| Phrase | "workcover doctor telehealth" |
| Phrase | "workcover doctor online" |
| Phrase | "workcover doctor near me" |
| Phrase | "workcover doctor Sydney" |
| Phrase | "workcover doctor NSW" |
| Phrase | "workers comp doctor" |
| Phrase | "workers comp doctor telehealth" |
| Exact | [workcover doctor same day] |
| Exact | [workers compensation doctor telehealth NSW] |

**Ad Group 1B: Certificate of Capacity**

| Match Type | Keywords |
|------------|----------|
| Phrase | "certificate of capacity" |
| Phrase | "certificate of capacity doctor" |
| Phrase | "certificate of capacity telehealth" |
| Phrase | "certificate of capacity renewal" |
| Phrase | "workcover medical certificate" |
| Phrase | "workers comp medical certificate" |
| Exact | [certificate of capacity same day] |
| Exact | [certificate of capacity online] |
| Exact | [SIRA certificate of capacity] |

**Ad Group 1C: Same-Day / Urgent**

| Match Type | Keywords |
|------------|----------|
| Phrase | "same day workcover doctor" |
| Phrase | "urgent workcover appointment" |
| Phrase | "workcover doctor today" |
| Phrase | "quick workcover certificate" |
| Exact | [same day certificate of capacity] |
| Exact | [workcover appointment today] |
| Exact | [emergency workcover doctor] |

**Ad Group 1D: Nominated Treating Doctor**

| Match Type | Keywords |
|------------|----------|
| Phrase | "nominated treating doctor" |
| Phrase | "change workcover doctor" |
| Phrase | "choose workcover doctor" |
| Phrase | "nominated treating doctor telehealth" |
| Exact | [can I change my workcover doctor] |
| Exact | [how to change nominated treating doctor NSW] |

### 06.2 Negative Keywords (Campaign Level)

These are critical to prevent waste. Apply to all WC campaigns.

| Category | Negative Keywords |
|----------|-------------------|
| Academic/Career | workcover doctor jobs, workcover doctor salary, workcover doctor career, how to become a workcover doctor, workcover doctor training |
| DIY/Forms | certificate of capacity form download, certificate of capacity PDF, certificate of capacity template, blank certificate of capacity |
| Insurance/Employer | workcover premium, workcover insurance quote, workcover employer registration, workcover insurance cost |
| Legal (competing intent) | workcover lawyer, workers comp lawyer, workcover claim lawyer, personal injury lawyer |
| Other states | workcover doctor Victoria, workcover doctor Queensland, workcover doctor Melbourne, workcover doctor Brisbane, WorkSafe |
| Competitor names | AusRehab, Sydney Injury Doctors, WorkCover Doctor (brand term) |
| Irrelevant medical | workcover dentist, workcover psychologist, workcover physio, workcover chiropractor |

Review search terms weekly for the first 8 weeks. Add negatives aggressively. Budget burned on irrelevant clicks in the first month is the most common failure mode.

### 06.3 Ad Copy — Ad Group 1A: WorkCover Doctor

All ad copy must comply with AHPRA advertising restrictions (Section 13). No superlatives, no guaranteed outcomes, no comparative claims.

**Responsive Search Ad 1:**

| Element | Variants |
|---------|----------|
| Headline 1 | WorkCover Doctor — Same-Day Consult |
| Headline 2 | Telehealth WorkCover Appointments |
| Headline 3 | No Cost With Active Claim |
| Headline 4 | SIRA-Compliant Certificates |
| Headline 5 | Same-Day Digital Certificates |
| Headline 6 | NSW WorkCover Doctor — Book Online |
| Headline 7 | Video Consult — 20 Minutes |
| Headline 8 | Certificate of Capacity Issued Today |
| Headline 9 | Skip the Wait — See a Doctor Today |
| Headline 10 | Experienced WorkCover Doctors |
| Headline 11 | No Travel Required — Telehealth |
| Headline 12 | Open Mon–Sat — Book Now |
| Headline 13 | Digital Certificate Sent Same Day |
| Headline 14 | Surry Hills Clinic + Telehealth |
| Headline 15 | Claims Doctor — WorkCover Consults |
| Description 1 | Same-day telehealth consultations with doctors who specialise in WorkCover assessments. Certificate of Capacity issued digitally. No cost to you with an active claim. Book online now. |
| Description 2 | Need a Certificate of Capacity? Our SIRA-experienced doctors assess your injury and issue certificates via telehealth. Same-day appointments available Mon–Sat. |
| Description 3 | Skip the 2-week GP wait. Claims Doctor provides same-day WorkCover telehealth consultations in NSW. Digital certificates. No out-of-pocket cost with active claim. |
| Description 4 | WorkCover telehealth doctor appointments in NSW. Certificate of Capacity issued on the day of your consultation. Billed directly to your insurer — no cost to you. |

Pin Headline 1 to Position 1. Pin Description 1 to Position 1. Let Google optimise the rest.

**Responsive Search Ad 2:**

| Element | Variants |
|---------|----------|
| Headline 1 | Certificate of Capacity — Today |
| Headline 2 | WorkCover Doctor via Telehealth |
| Headline 3 | No GP? No Problem — We Can Help |
| Headline 4 | SIRA Certificates Issued Same Day |
| Headline 5 | 20-Min Video Consultation |
| Headline 6 | Billed to Your Insurer — No Cost |
| Headline 7 | Experienced Work Injury Doctors |
| Headline 8 | NSW-Wide Telehealth Appointments |
| Headline 9 | Book Online in 60 Seconds |
| Headline 10 | Your Claim Shouldn't Wait |
| Headline 11 | Claims Doctor — SIRA Specialists |
| Headline 12 | Same-Day WorkCover Consults NSW |
| Headline 13 | No Referral Needed |
| Headline 14 | Digital Certificate Delivered Fast |
| Headline 15 | Open Saturdays — Book Now |
| Description 1 | Your GP won't do WorkCover? We specialise in it. Same-day telehealth consultations with SIRA-experienced doctors. Certificate of Capacity issued digitally on the day. |
| Description 2 | Claims Doctor provides WorkCover telehealth appointments across NSW. See a doctor today, get your Certificate of Capacity today. Billed directly to your insurer. |
| Description 3 | Injured at work? Don't wait weeks for a GP appointment. Claims Doctor offers same-day video consultations for WorkCover assessments. No out-of-pocket costs with an active claim. |
| Description 4 | Fast, professional WorkCover medical assessments via telehealth. SIRA-compliant certificates issued digitally. Appointments available Mon–Sat across NSW. |

### 06.4 Ad Extensions

| Extension | Content |
|-----------|---------|
| Sitelinks | "How It Works" → /how-it-works · "Certificate of Capacity" → /services/certificate-of-capacity · "WorkCover FAQ" → /faq · "About Our Doctors" → /about |
| Callouts | Same-Day Appointments · No Cost With Active Claim · Telehealth Across NSW · Digital Certificates · SIRA-Experienced Doctors · Open Saturdays |
| Structured Snippets | Services: Certificate of Capacity, Return to Work Plans, Specialist Referrals, CTP Certificates |
| Call Extension | Main booking number · Mon–Fri 7am–9pm, Sat 8am–2pm |
| Location Extension | Level 1/457-459 Elizabeth Street, Surry Hills NSW 2010 |
| Image Extension | Claims Doctor branded image (compliant — no before/after, no patient images without consent) |

### 06.5 Landing Pages

| Ad Group | Landing Page | URL |
|----------|-------------|-----|
| 1A: WorkCover Doctor | WorkCover Doctor Telehealth | /services/workcover-doctor-telehealth |
| 1B: Certificate of Capacity | Certificate of Capacity Service Page | /services/certificate-of-capacity |
| 1C: Same-Day / Urgent | How It Works | /how-it-works |
| 1D: Nominated Treating Doctor | Nominated Treating Doctor Guide | /guides/nominated-treating-doctor-nsw |

Every landing page must include: a clear headline matching ad copy, a booking CTA above the fold, the "How It Works" 3-step process, a "No cost with active claim" trust signal, and Dr Laidlaw's credentials.

---

## 07 Campaign 2 — CTP-Search-High-Intent

### 07.1 Ad Groups & Keywords

**Ad Group 2A: CTP Doctor**

| Match Type | Keywords |
|------------|----------|
| Phrase | "CTP doctor" |
| Phrase | "CTP doctor telehealth" |
| Phrase | "motor vehicle accident doctor" |
| Phrase | "car accident doctor NSW" |
| Phrase | "CTP doctor Sydney" |
| Exact | [CTP doctor telehealth NSW] |
| Exact | [motor vehicle accident doctor telehealth] |

**Ad Group 2B: Certificate of Fitness**

| Match Type | Keywords |
|------------|----------|
| Phrase | "certificate of fitness" |
| Phrase | "certificate of fitness CTP" |
| Phrase | "CTP medical certificate" |
| Exact | [certificate of fitness NSW] |
| Exact | [certificate of fitness doctor] |

**Ad Group 2C: CTP Claim Help**

| Match Type | Keywords |
|------------|----------|
| Phrase | "CTP claim doctor" |
| Phrase | "car accident injury doctor" |
| Phrase | "CTP injury assessment" |
| Exact | [CTP claim medical assessment NSW] |

### 07.2 Negative Keywords (Campaign Level)

Same base list as Campaign 1, plus:

| Category | Negative Keywords |
|----------|-------------------|
| Insurance-side | CTP insurance quote, CTP green slip, CTP calculator, CTP insurer, green slip comparison |
| Legal (competing) | CTP lawyer, car accident lawyer, motor vehicle accident lawyer, personal injury lawyer CTP |
| Panel beating | car accident repair, car damage, panel beater, car insurance claim |

### 07.3 Ad Copy — Ad Group 2A: CTP Doctor

**Responsive Search Ad 1:**

| Element | Variants |
|---------|----------|
| Headline 1 | CTP Doctor — Same-Day Telehealth |
| Headline 2 | Motor Vehicle Accident Assessment |
| Headline 3 | Certificate of Fitness — Today |
| Headline 4 | No Cost With Active CTP Claim |
| Headline 5 | Video Consult — 20 Minutes |
| Headline 6 | NSW CTP Doctor — Book Online |
| Headline 7 | SIRA-Compliant CTP Certificates |
| Headline 8 | Injured in a Car Accident? |
| Headline 9 | Same-Day CTP Medical Assessment |
| Headline 10 | Digital Certificate Sent Same Day |
| Headline 11 | No Referral Required |
| Headline 12 | Claims Doctor — CTP Consults |
| Headline 13 | Skip the GP Wait |
| Headline 14 | Open Mon–Sat |
| Headline 15 | Experienced CTP Doctors |
| Description 1 | Injured in a motor vehicle accident? Claims Doctor provides same-day telehealth CTP assessments. Certificate of Fitness issued digitally. No cost with an active CTP claim. |
| Description 2 | Need a Certificate of Fitness for your CTP claim? Our SIRA-experienced doctors provide telehealth consultations across NSW. Same-day appointments, digital certificates. |
| Description 3 | Don't wait weeks for a GP after a car accident. Claims Doctor offers same-day video consultations for CTP injury assessments. Billed directly to your CTP insurer. |
| Description 4 | Fast CTP medical assessments via telehealth. SIRA-compliant Certificate of Fitness issued on the day. Appointments available Mon–Sat across NSW. Book online now. |

### 07.4 Landing Pages

| Ad Group | Landing Page | URL |
|----------|-------------|-----|
| 2A: CTP Doctor | CTP / Motor Vehicle Accident Doctor | /services/ctp-motor-vehicle-accident-doctor |
| 2B: Certificate of Fitness | Certificate of Fitness (to be built — redirect to CTP service page until live) | /services/ctp-motor-vehicle-accident-doctor |
| 2C: CTP Claim Help | CTP Claims Guide | /guides/ctp-claims-nsw |

---

## 08 Campaign 3 — WC-Search-Informational

Launch at Week 4 once educational landing pages (Priority 3 from content strategy) are live. This campaign targets people researching WorkCover processes who haven't yet decided they need a doctor.

### 08.1 Ad Groups & Keywords

**Ad Group 3A: WorkCover Claims Process**

| Match Type | Keywords |
|------------|----------|
| Phrase | "how to make a workcover claim" |
| Phrase | "lodge workcover claim NSW" |
| Phrase | "workcover claim process" |
| Phrase | "workcover entitlements NSW" |
| Exact | [how to lodge a workcover claim in NSW] |

**Ad Group 3B: WorkCover Rights & Payments**

| Match Type | Keywords |
|------------|----------|
| Phrase | "workcover weekly payments" |
| Phrase | "injured worker rights NSW" |
| Phrase | "workcover claim denied" |
| Phrase | "workcover benefits NSW" |
| Exact | [what happens if workcover claim denied] |
| Exact | [workcover weekly payments explained] |

**Ad Group 3C: WorkCover Telehealth Legitimacy**

This ad group directly addresses the Rose Medical misinformation.

| Match Type | Keywords |
|------------|----------|
| Phrase | "workcover telehealth" |
| Phrase | "can workcover be done via telehealth" |
| Phrase | "workcover video consultation" |
| Phrase | "telehealth workers compensation" |
| Exact | [can a workcover doctor do telehealth] |

### 08.2 Landing Pages

| Ad Group | Landing Page | URL |
|----------|-------------|-----|
| 3A | How to Lodge a WorkCover Claim in NSW | /guides/how-to-lodge-workcover-claim-nsw |
| 3B | WorkCover Weekly Payments Explained | /guides/workcover-weekly-payments-nsw |
| 3C | WorkCover Telehealth: What You Need to Know | /guides/workcover-telehealth-explained |

These are top-of-funnel. CPA will be higher. The purpose is to capture email addresses (via guide download or newsletter) and retarget later. Bid conservatively — max CPC 50% of Campaign 1 bids.

---

## 09 Campaign 4 — B2B-Search-Referral

Launch at Week 6. Targets B2B referral partners (lawyers, rehab providers, physios, labour hire, GPs) searching for a WorkCover doctor to refer patients to. These are low-volume, high-value searches.

### 09.1 Ad Groups & Keywords

**Ad Group 4A: Lawyer Referrals**

| Match Type | Keywords |
|------------|----------|
| Phrase | "workcover doctor for clients" |
| Phrase | "refer patient workcover doctor" |
| Phrase | "workcover medical evidence" |
| Phrase | "certificate of capacity for lawyers" |
| Exact | [workcover doctor referral for law firm] |

**Ad Group 4B: Employer / Labour Hire**

| Match Type | Keywords |
|------------|----------|
| Phrase | "workcover doctor for employees" |
| Phrase | "same day workcover assessment employer" |
| Phrase | "workplace injury doctor for employers" |
| Exact | [workcover doctor for labour hire company] |

**Ad Group 4C: Allied Health / Physio**

| Match Type | Keywords |
|------------|----------|
| Phrase | "refer patient for certificate of capacity" |
| Phrase | "workcover doctor referral for physio" |
| Phrase | "allied health workcover referral" |

### 09.2 Landing Pages

| Ad Group | Landing Page | URL |
|----------|-------------|-----|
| 4A | WorkCover Doctor for Lawyers | /for-lawyers |
| 4B | WorkCover Doctor for Employers | /for-employers |
| 4C | How It Works (general — build a /for-allied-health page if volume justifies) | /how-it-works |

### 09.3 Ad Copy — B2B Angle

The B2B ads speak to the referrer, not the patient. Different pain points, different language.

**Responsive Search Ad — Lawyers:**

| Element | Key Variants |
|---------|-------------|
| Headlines | Refer Clients for Same-Day Certificates · Certificate of Capacity — Same Day · WorkCover Medical Evidence, Fast · SIRA-Compliant Certificates for Your Clients · Stop Chasing GPs for Certificates · Claims Doctor — Referral Partner |
| Descriptions | Your clients need Certificates of Capacity and their GP won't do it. Claims Doctor provides same-day telehealth assessments with SIRA-experienced doctors. Digital certificates. No cost to your client with active claim. · Law firms across NSW refer their WorkCover clients to Claims Doctor. Same-day appointments. SIRA-compliant certificates. No bottleneck, no chasing. |

---

## 10 Campaign 5 — Brand Defence

Launch when brand search volume emerges (check Google Trends and Search Console). This prevents competitors from bidding on "Claims Doctor" and controls the SERP for brand queries.

### 10.1 Keywords

| Match Type | Keywords |
|------------|----------|
| Exact | [claims doctor] |
| Exact | [claimsdoctor] |
| Exact | [claims doctor workcover] |
| Exact | [claims doctor telehealth] |
| Phrase | "claims doctor" |

### 10.2 Budget

Minimal. Brand CPCs are typically $0.30–$0.80. Cap at $5/day initially. Scale only if a competitor begins bidding on "Claims Doctor."

---

## 11 Budget Model

### 11.1 Launch Budget (Month 1–3)

| Campaign | Daily Budget | Monthly Budget | % of Total |
|----------|-------------|---------------|------------|
| WC-Search-High-Intent | $50 | $1,500 | 60% |
| CTP-Search-High-Intent | $25 | $750 | 30% |
| WC-Search-Informational | $8 | $250 | 10% |
| **Total** | **$83** | **$2,500** | **100%** |

Campaigns 4 (B2B) and 5 (Brand) added from Month 2 with incremental budget of $250–$500/month.

### 11.2 Unit Economics

These are the numbers that determine whether Google Ads is viable. All figures in AUD.

| Metric | Conservative | Target | Optimistic |
|--------|-------------|--------|-----------|
| Average CPC | $5.00 | $3.50 | $2.50 |
| Conversion Rate (click → booking) | 5% | 8% | 12% |
| CPA (cost per booking) | $100.00 | $43.75 | $20.83 |
| Revenue per initial consultation (AA045T) | $450 | $450 | $450 |
| ROAS (first visit only) | 4.5x | 10.3x | 21.6x |

At the target scenario ($3.50 CPC, 8% CVR), every $43.75 spent acquires a patient worth $450 in initial consultation revenue alone. Follow-up consultations at $205 (AA030T) and certificate fees at $64.68 (WCO001) add lifetime value on top.

**Break-even CPA:** Even at the conservative scenario ($100 CPA), the first consultation ($450) delivers 4.5x ROAS before follow-ups. Google Ads is viable at any realistic CPA below $200.

### 11.3 Monthly Volume Projections (Target Scenario)

| Metric | Month 1 | Month 2 | Month 3 |
|--------|---------|---------|---------|
| Total spend | $2,500 | $2,500 | $3,000 |
| Clicks (at $3.50 CPC) | 714 | 714 | 857 |
| Bookings (at 8% CVR) | 57 | 57 | 69 |
| Show rate (est. 70%) | 40 | 40 | 48 |
| Revenue (at $450/initial) | $18,000 | $18,000 | $21,600 |
| ROAS | 7.2x | 7.2x | 7.2x |

These projections assume a 70% show rate (30% no-show/cancellation), which is typical for telehealth bookings. Optimisation focus should include SMS/email appointment reminders to push show rate toward 85%.

### 11.4 Scaling Criteria

Increase budget when ALL of the following are true:

1. CPA is stable and below $75 for 14 consecutive days
2. Show rate is above 70%
3. Booking capacity is not saturated (doctors have open slots)
4. Quality Score is 7+ on primary keywords

Scale by 20% per week maximum. Do not double budgets overnight — it resets the learning phase and destabilises bids.

---

## 12 Conversion Tracking

### 12.1 Primary Conversion

| Conversion | Method | Value |
|------------|--------|-------|
| Booking completed | HubSpot booking link click → confirmation page load | $450 (dynamic if possible; static as fallback) |

The booking link on the website triggers a HubSpot scheduling workflow. The confirmation page (post-booking) fires the Google Ads conversion tag.

### 12.2 Secondary Conversions (Micro-Conversions)

| Conversion | Method | Value |
|------------|--------|-------|
| Phone call (30+ seconds) | Google call tracking on call extension and landing page number | $50 (estimated) |
| WhatsApp click | Event tracking on WhatsApp CTA | $20 (estimated) |
| SMS click | Event tracking on SMS CTA | $20 (estimated) |
| Guide download (email capture) | Form submission on educational pages | $5 |

### 12.3 Attribution Model

Use Google Ads data-driven attribution (default). For internal reporting, also track first-click attribution to understand which campaigns generate initial awareness.

### 12.4 Technical Implementation

1. Google Ads conversion tag on booking confirmation page
2. Google Tag Manager container on all pages
3. GA4 linked to Google Ads account
4. HubSpot UTM parameter passthrough on all booking links
5. Offline conversion import from HubSpot (booking → consultation completed) for true CPA optimisation

The offline conversion import is critical. Google needs to know which bookings actually turned into consultations so it can optimise toward real patients, not just form fills.

---

## 13 AHPRA & Google Compliance Framework

### 13.1 AHPRA Advertising Restrictions

AHPRA's advertising guidelines for regulated health services are non-negotiable. Every ad, every headline, every description, every landing page must comply. The penalties for breach include prosecution under the National Law.

**Prohibited in all ad copy and landing pages:**

| Rule | What It Means | Example of Violation |
|------|--------------|---------------------|
| No unsubstantiated health benefit claims | Cannot claim treatment will produce a specific outcome unless supported by robust clinical evidence | "We guarantee your WorkCover claim will be approved" |
| No superlatives without evidence | Cannot use "best", "leading", "top", "number one" unless independently verifiable | "Sydney's best WorkCover doctor" |
| No comparative claims | Cannot claim superiority over other practitioners or services | "Better than your GP at WorkCover certificates" |
| No testimonials about clinical outcomes | Patient testimonials cannot describe health outcomes or treatment results | "Thanks to Claims Doctor my claim was approved in 3 days" |
| No before/after imagery | Cannot show images suggesting treatment outcomes | Before/after injury photos |
| No misleading credentials | Practitioner qualifications must be accurate and currently held | Listing a lapsed fellowship |
| No inducements | Cannot offer gifts, discounts, or inducements to attract patients | "Book today and get a free follow-up" |

**Permitted:**

- Factual descriptions of services offered
- Practitioner qualifications that are current and verifiable
- Process descriptions ("same-day telehealth consultations")
- Pricing information (when accurate)
- Patient testimonials about service experience (not clinical outcomes) — e.g., "The booking process was easy and the doctor was thorough"
- Citing SIRA, legislation, and government sources

### 13.2 Google Healthcare & Medicines Policy (Australia)

Google requires healthcare advertisers in Australia to comply with additional policies:

1. **Healthcare certification** may be required. Apply via Google Ads account under "Verification" if prompted. Claims Doctor qualifies as a legitimate telehealth medical service.
2. **No restricted pharmaceutical terms** in ad copy. We don't prescribe medications as a primary service, so this is low risk, but ensure no ad copy mentions specific drugs.
3. **TGA compliance** for any therapeutic claims. Since we issue certificates (not treatments), TGA risk is minimal. But landing pages must not make therapeutic claims about injury recovery.

### 13.3 Ad Copy Review Checklist

Before any ad goes live, it must pass every item:

- [ ] No superlatives (best, leading, top, number one) unless independently verified
- [ ] No guaranteed outcomes (approval, success, recovery)
- [ ] No comparative claims against competitors or GPs
- [ ] No patient testimonials about clinical outcomes
- [ ] No inducements or free offers (except stating "no cost with active claim" which is a factual billing statement, not an inducement)
- [ ] All practitioner credentials are current and verifiable
- [ ] Landing page matches ad copy (no bait-and-switch)
- [ ] SIRA/legislative citations are accurate and current
- [ ] No restricted pharmaceutical terms
- [ ] "No cost" messaging clarifies it's insurer-billed, not "free healthcare"

---

## 14 Landing Page Requirements

### 14.1 Mandatory Elements (All Landing Pages Receiving Paid Traffic)

Every landing page must include:

1. **Headline matching the ad group's primary keyword** — if the ad says "Certificate of Capacity", the landing page H1 must include "Certificate of Capacity"
2. **Booking CTA above the fold** — button, not a text link
3. **"How It Works" 3-step process** — Book → Consult → Certificate issued digitally
4. **"No cost with active claim" trust signal** — explain insurer-direct billing
5. **Dr Laidlaw's credentials** — abbreviated on page, linked to full bio
6. **SIRA compliance callout** — "Our certificates comply with SIRA requirements under the Workers Compensation Act 1987"
7. **Mobile-responsive design** — 60%+ of traffic will be mobile
8. **Page load under 3 seconds** — Google penalises slow pages with lower Quality Score
9. **No navigation distractions** — strip main site nav on paid landing pages; keep the user on a single conversion path
10. **Schema markup** — MedicalBusiness, Physician, FAQPage as applicable

### 14.2 Landing Page Build Priority

Aligned with campaign launch sequence:

| Priority | Page | URL | Campaign |
|----------|------|-----|----------|
| 1 | WorkCover Doctor Telehealth | /services/workcover-doctor-telehealth | Campaign 1 |
| 2 | Certificate of Capacity | /services/certificate-of-capacity | Campaign 1 |
| 3 | How It Works | /how-it-works | Campaign 1 |
| 4 | CTP / Motor Vehicle Accident Doctor | /services/ctp-motor-vehicle-accident-doctor | Campaign 2 |
| 5 | WorkCover Telehealth Guide | /guides/workcover-telehealth-explained | Campaign 3 |
| 6 | For Lawyers | /for-lawyers | Campaign 4 |
| 7 | For Employers | /for-employers | Campaign 4 |

Do not launch a campaign until its landing pages are live, loaded, and tested.

---

## 15 Optimisation Cadence

### 15.1 Weekly (Every Monday)

| Task | Action |
|------|--------|
| Search term review | Add negatives for irrelevant queries. Promote high-performing search terms to exact match. |
| CPC review | Adjust bids on keywords with CPA above target. Increase bids on keywords with CPA below target and room to scale. |
| Ad performance | Pause any ad variant with CTR below 3% after 1,000 impressions. Replace with new variant. |
| Budget pacing | Check that daily budget is being fully consumed. If underspending, broaden match types or increase bids. If overspending early in the day, add ad scheduling restrictions. |

### 15.2 Fortnightly (Every Second Friday)

| Task | Action |
|------|--------|
| Quality Score audit | Check QS for all keywords. Any keyword below 5 needs landing page or ad relevance improvement. |
| Landing page conversion rate | Compare CVR across landing pages. A/B test CTAs, headlines, social proof. |
| Device performance | Review CPA by device (desktop, mobile, tablet). Apply bid adjustments if one device is materially worse. |
| Geographic performance | Review CPA by region within NSW. Consider bid adjustments for high-performing areas (e.g., Western Sydney for labour hire ICP). |

### 15.3 Monthly

| Task | Action |
|------|--------|
| Campaign-level CPA and ROAS | Calculate true CPA including no-shows. Report against unit economics in Section 11.2. |
| Competitive review | Check what competitors are bidding on using Google Ads Auction Insights. Note impression share changes. |
| New keyword research | Use Google Ads Keyword Planner and Search Console data to identify new keyword opportunities. |
| Budget reallocation | Shift budget from underperforming campaigns to outperforming ones. |
| Ad copy refresh | Write new ad variants for the next month. Retire underperformers. |

### 15.4 Quarterly

| Task | Action |
|------|--------|
| Full account audit | Review all campaigns, ad groups, keywords, negatives, extensions, landing pages. |
| Strategy review | Reassess campaign architecture against business goals. Add/remove campaigns. |
| Bid strategy evaluation | Assess readiness to move from Manual CPC to Target CPA or Maximise Conversions. Requires 30+ conversions in 30 days. |
| AHPRA compliance re-check | Review all active ads against current AHPRA advertising guidelines for any regulatory updates. |

---

## 16 Expansion Criteria

Do not expand to new channels or campaign types until the Search foundation is profitable and stable.

### 16.1 Prerequisites for Display Network

- Search campaigns achieving CPA below $50 for 30 consecutive days
- Remarketing audience of 1,000+ users on the website
- Display-specific creative assets (banner images) approved for AHPRA compliance

### 16.2 Prerequisites for YouTube

- At least one professional video asset (Dr Laidlaw explainer or patient journey — no clinical outcome claims)
- Search campaigns achieving CPA below $50 for 30 consecutive days
- Monthly ad budget of $5,000+ to support a separate YouTube campaign

### 16.3 Prerequisites for Performance Max

- 50+ conversions per month across Search campaigns
- Offline conversion import from HubSpot functioning correctly
- Willingness to cede keyword-level control (Performance Max is a black box)

---

## 17 Risk Register

| Risk | Impact | Likelihood | Mitigation |
|------|--------|-----------|------------|
| AHPRA breach in ad copy | High — prosecution, reputational damage | Low (with checklist) | Every ad reviewed against Section 13 checklist before going live |
| Google ad disapproval | Medium — campaigns paused | Medium | Pre-check all ads against Google Healthcare policy. Appeal disapprovals within 24 hours. |
| Competitor bidding war on "workcover doctor" | Medium — CPC inflation | Medium | Maintain Quality Score above 7 to keep CPC competitive. Diversify to long-tail keywords. |
| Low show rate (<60%) | High — CPA blows out | Medium | SMS + email reminders at booking, 24hr, and 1hr before. WhatsApp confirmation option. |
| Landing pages not ready at campaign launch | High — wasted spend, low QS | Low (with planning) | Do not activate any campaign until its landing pages are live and tested. |
| Budget exhaustion before business hours end | Low — missed afternoon conversions | Medium | Use ad scheduling. Review hourly performance data in Week 1. |
| Rose Medical telehealth misinformation affecting CVR | Medium — searchers hesitate to book telehealth | Medium | Landing pages cite SIRA telehealth guidelines directly. Build /guides/workcover-telehealth-explained as authority page. |

---

## 18 KPI Targets (First 90 Days)

| KPI | Month 1 | Month 2 | Month 3 |
|-----|---------|---------|---------|
| Total spend | $2,500 | $2,500 | $3,000 |
| Clicks | 500+ | 600+ | 750+ |
| CTR | 4%+ | 5%+ | 5%+ |
| Bookings | 30+ | 40+ | 50+ |
| CPA (booking) | <$85 | <$65 | <$55 |
| Show rate | 65%+ | 70%+ | 75%+ |
| Consultations delivered | 20+ | 28+ | 38+ |
| Revenue (initial consults) | $9,000+ | $12,600+ | $17,100+ |
| ROAS (first visit only) | 3.6x+ | 5.0x+ | 5.7x+ |
| Quality Score (primary keywords) | 5+ | 6+ | 7+ |

Month 1 targets are deliberately conservative. The learning phase eats budget. Don't panic. Optimise aggressively from Week 2.

---

## 19 Related Documents

| Doc ID | Title | Relationship |
|--------|-------|-------------|
| CD-MKT-002 | ICP & Persona Profiles | Depends on — audience targeting and ad copy angles derived from ICPs |
| CD-FIN-002 | Pricing Schedule (SIRA Fee Mapping) | Depends on — unit economics model uses SIRA fee codes |
| CD-BRD-001 | Brand & Style Guide | Depends on — visual assets, tone of voice for ad copy |
| CD-MKT-003 | SEO/GEO Strategy | Informs — keyword overlap, landing page content alignment |
| CD-MKT-001 | Marketing Plan | Informs — Google Ads is a channel within the broader marketing plan |
| CD-LEG-001 | AHPRA Advertising Compliance Checklist | Informs — compliance requirements codified in Section 13 |
| CD-OPS-011 | Technology Stack Documentation | Informs — conversion tracking implementation details |

---

## 20 Review & Approval

| Role | Name | Date | Signature |
|------|------|------|-----------|
| Author | Claude (AI) / Robert Laidlaw | 2026-02-27 | |
| Reviewer | | | |
| Approver | Robert Laidlaw | | |

---

**Claims Doctor** · claimsdoctor.com.au
ABN 39 674 905 376 · Level 1/457-459 Elizabeth Street, Surry Hills NSW 2010

_This document is the property of Claims Doctor. Unauthorised distribution is prohibited._
_Document ID: CD-MKT-005 · Version 0.2 · Status: DRAFT · Visibility: INTERNAL_
