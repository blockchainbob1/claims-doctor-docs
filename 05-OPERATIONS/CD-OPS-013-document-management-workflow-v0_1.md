---
doc_id: CD-OPS-013
title: "Document Management Workflow"
version: 0.1
status: DRAFT
visibility: INTERNAL
owner: Robert Laidlaw
last_updated: 2026-03-01
approved_date: null
next_review: 2026-06-01
dependencies: [CD-STR-000]
changelog:
  - version: 0.1
    date: 2026-03-01
    summary: Initial draft. Establishes GitHub as single source of truth, documents commit conventions, branching strategy, document lifecycle workflow, Claude-assisted authoring process, and file retention policy.
---

# Document Management Workflow

**Claims Doctor** · Same-day WorkCover & CTP medical certificates.

---

## 01 Purpose

This document defines how Claims Doctor creates, edits, versions, and stores business documentation using GitHub as the single source of truth. It governs the end-to-end lifecycle from document creation through to retirement.

---

## 02 Scope

Applies to all Claims Doctor business documents registered in CD-STR-000 (Document Registry). Covers the GitHub repository `claims-doctor-docs`, all document authoring workflows, commit conventions, version management, and file retention.

Does not cover clinical records, patient health information, or any data stored in the electronic medical record system. Those are governed by CD-GOV-004 (Medical Records Management Policy).

---

## 03 Definitions

| Term | Definition |
|------|-----------|
| Repository | The GitHub repository `blockchainbob1/claims-doctor-docs` containing all business documentation |
| Single source of truth | The authoritative location for all current business documents — GitHub main branch |
| Commit | A discrete, versioned change to one or more files in the repository |
| Main branch | The primary branch; all current documents live here |
| YAML frontmatter | The metadata block at the top of each document enclosed in `---` delimiters |
| Document Registry | CD-STR-000, the master index of all documents, their versions, statuses, and dependencies |

---

## 04 Repository as Single Source of Truth

GitHub is the sole authoritative store for all Claims Doctor business documentation. No other location (Google Drive, local files, email attachments, shared folders) is authoritative. If a document exists outside the repository, it is either a working draft not yet committed, or it is stale and should not be relied upon.

The repository URL is: `https://github.com/blockchainbob1/claims-doctor-docs`

### 04.1 What belongs in the repository

All documents registered in CD-STR-000, stored as Markdown files with YAML frontmatter. This includes strategy, financial, marketing, sales, operations, governance, legal, HR, patient-facing, reporting, and brand documents.

### 04.2 What does not belong in the repository

Patient health information, clinical records, financial transaction data, credentials or API keys, large binary files (images, PDFs, spreadsheets), and any file containing personally identifiable information.

---

## 05 Branching Strategy

### 05.1 Pre-revenue phase (current)

All commits go directly to the `main` branch. There is no branching, no pull requests, and no formal code review. This is appropriate while Robert is the sole operator and all documents are either in DRAFT or early ACTIVE status.

### 05.2 Post-revenue phase (planned)

After 30 days of live operations, the branching strategy will be reviewed. The expected transition is to a simple branch-per-document model where substantive changes (major version bumps) are drafted on a feature branch and merged to main after review. Minor version bumps (typos, formatting) may continue to go direct to main.

The trigger for this transition is either: (a) a second team member contributing to documentation, or (b) the 30-day operational review, whichever comes first.

---

## 06 Commit Conventions

### 06.1 Commit message format

```
[CAT-###] Action — brief description (vX.Y)
```

**Examples:**

```
[OPS-013] Create — document management workflow (v0.1)
[GOV-001] Promote — clinical governance framework to ACTIVE (v1.0)
[PAT-001] Edit — update eligibility criteria wording (v1.1)
[STR-000] Update — registry statistics after GOV-007 retirement (v2.1)
[LEG-008] Rename — align filename to v1_0 convention
```

### 06.2 Commit scope

One commit should represent one logical unit of work. Acceptable patterns:

- **Single document creation or edit** — one document changed, one commit.
- **Document + registry update** — when creating or promoting a document, the registry update (CD-STR-000) should be included in the same commit.
- **Batch housekeeping** — renaming files, fixing formatting across multiple docs, or repo-wide audits may be a single commit with a descriptive message.

Avoid combining unrelated document changes in a single commit.

### 06.3 What not to commit

Do not commit incomplete fragments, placeholder files with no content beyond the template, or temporary working files. If a document is in early ideation, keep it local until it has at least a complete Purpose and Scope section.

---

## 07 Document Lifecycle Workflow

### 07.1 Creating a new document

1. **Reserve the ID.** Check CD-STR-000 for the next available number in the relevant category.
2. **Create the file.** Use the template (`CD-TEMPLATE-document-template.md`). Name it following the convention: `CD-[CAT]-[###]-[short-name]-v0_1.md`.
3. **Write the content.** Complete at minimum: Purpose, Scope, and the primary content section.
4. **Update frontmatter.** Set `version: 0.1`, `status: DRAFT`, `last_updated` to today's date, and populate `dependencies`.
5. **Update the registry.** Add the document to CD-STR-000 with status DRAFT and version 0.1. Increment the registry's minor version.
6. **Commit.** Single commit containing the new document and the updated registry.

### 07.2 Editing an existing document

1. **Determine version impact.** Is this a minor change (clarification, typo, formatting) or a major change (scope, policy, requirements)?
2. **Edit the file.** Make changes in the existing file.
3. **Update frontmatter.** Bump the version number, update `last_updated`, and add a changelog entry summarising the change.
4. **Rename the file** if the version number in the filename has changed (e.g., `v0_1.md` → `v0_2.md`). Delete the old filename.
5. **Update the registry** if the version number changed. Increment the registry's minor version.
6. **Commit.**

### 07.3 Promoting a document to ACTIVE

1. **Confirm readiness.** The document must be complete, reviewed, and fit for operational use.
2. **Update frontmatter.** Set `version: 1.0`, `status: ACTIVE`, `approved_date` to today, and `next_review` to 3 months from today.
3. **Rename the file** to reflect v1_0.
4. **Update the registry.** Change status to ACTIVE and version to 1.0. Increment the registry's minor version.
5. **Check dependencies.** If this document is a dependency for other documents, verify those documents are still consistent.
6. **Commit.**

### 07.4 Major version bump on an ACTIVE document

1. **Follow the editing workflow** (07.2) with a major version bump.
2. **Trigger dependency cascade.** Per CD-STR-000 dependency rules, every document that lists this document as a dependency MUST be reviewed. Log which documents were reviewed and whether they required updates.
3. **Commit** the updated document, registry, and any dependent documents that changed.

### 07.5 Retiring a document

1. **Update frontmatter.** Set `status: RETIRED`. Add a changelog entry explaining why.
2. **Update the registry.** Change status to RETIRED.
3. **Do not delete the file.** Retired documents remain in the repository for reference. Git history preserves all prior versions.
4. **Commit.**

---

## 08 File Retention Policy

### 08.1 Current version only on disk

Only the current version of each document is kept as a file in the repository. When a document is bumped from v0.1 to v0.2, the v0_1 file is deleted and replaced by v0_2. Previous versions are preserved in git history and can be recovered at any time using `git log` and `git checkout`.

### 08.2 Retired documents

Retired documents remain on disk with their last version number and RETIRED status in frontmatter. They are not deleted from the working tree.

### 08.3 Recovery

To recover a previous version of any document:

```bash
# View file history
git log --oneline -- path/to/file.md

# View a specific historical version
git show <commit-hash>:path/to/file.md

# Restore a previous version
git checkout <commit-hash> -- path/to/file.md
```

---

## 09 Claude-Assisted Authoring

### 09.1 Workflow

Most Claims Doctor documents are drafted or edited in collaboration with Claude (Anthropic). The typical workflow is:

1. Robert identifies the document to create or edit.
2. Claude reads the current repository state, relevant dependencies, and the document template.
3. Claude drafts or edits the document content.
4. Robert reviews the output, requests revisions if needed, and approves.
5. Robert commits the final version to GitHub.

### 09.2 Claude's access model

Claude reads the repository contents during sessions but does not have persistent write access. All commits are made by Robert. Claude may prepare commit-ready files, but the act of committing is a human action.

### 09.3 Context management

At the start of a session involving documentation work, Claude should:

- Clone or read the current state of the repository.
- Check CD-STR-000 for current document statuses and dependencies.
- Verify the target document's frontmatter is consistent with the registry before making changes.

### 09.4 Quality checks before handoff

Before presenting a document for commit, Claude should verify:

- YAML frontmatter is complete and consistent (version, status, dates, dependencies, changelog).
- Filename matches the version in frontmatter.
- The registry entry matches the document's current state.
- Any dependency cascade impacts have been identified.

---

## 10 Repository Structure

The repository follows a numbered folder structure aligned with document categories:

```
claims-doctor-docs/
├── 01-STRATEGY/
├── 02-FINANCIAL/
├── 03-MARKETING/
├── 04-SALES/
├── 05-OPERATIONS/
├── 06-GOVERNANCE/
├── 07-LEGAL/
├── 08-HR/
├── 09-PATIENT-FACING/
├── 10-REPORTING/
├── 11-BRAND/
├── CD-TEMPLATE-document-template.md
└── README.md
```

Documents are placed in the folder matching their category code. No nested subfolders within category folders.

---

## 11 Related Documents

| Doc ID | Title | Relationship |
|--------|-------|-------------|
| CD-STR-000 | Document Registry | Depends on — this workflow implements the registry's rules |
| CD-OPS-011 | Technology Stack Documentation | Informs — GitHub is part of the tech stack |
| CD-OPS-012 | Business Continuity / Disaster Recovery Plan | Informs — repository backup and recovery |

---

## 12 Review & Approval

| Role | Name | Date | Signature |
|------|------|------|-----------|
| Author | Claude / Robert Laidlaw | 2026-03-01 | |
| Reviewer | | | |
| Approver | Robert Laidlaw | | |

---

**Claims Doctor** · claimsdoctor.com.au
ABN 39 674 905 376 · Level 1/457-459 Elizabeth Street, Surry Hills NSW 2010

_This document is the property of Claims Doctor. Unauthorised distribution is prohibited._
_Document ID: CD-OPS-013 · Version 0.1 · Status: DRAFT · Visibility: INTERNAL_
