# Status and roadmap

Public editorial review date: **22 October 2026**. This date identifies the preparation of this document, not the date of a successful live-product test. Baran Bayran owns publication decisions. SkiHub Tech coordinates the accepted technical review roles for HUB-02 and HUB-04; this does not appoint a product integration owner or establish live acceptance.

## Status vocabulary

| Label | Use it only when… |
| --- | --- |
| **Verified / Doğrulandı** | Current evidence supports a specific claim in a named environment. State whether that is documentation, source, local test, controlled integration, or live evidence. |
| **In development / Geliştirme aşamasında** | A current assigned change and its scope can be identified. This does not mean that the feature is usable. |
| **Planned / Planlanıyor** | The work is proposed or approved for a future step; implementation evidence is not claimed. |
| **Verification pending / Doğrulama bekliyor** | A product intention or previous claim exists without sufficient current evidence for the asserted behavior. |

Do not promote one kind of evidence into another. A local check is not a live test; a successful mock is not a provider transaction; a code finding is not a completed security audit.

## Current public picture

| Area | Status | What can be said safely | What remains to be established |
| --- | --- | --- | --- |
| Knowledge and contribution hub | **Verified — documentation only** | Public documentation and path-specific licenses provide a bounded contribution route; all four tasks are Ready to claim, with two accepted technical review roles. | Maintainer confirmation is required before work. HUB-04 execution is queued after HUB-02's accepted source handoff; agent findings do not replace GitHub approval. |
| Instructor application and sign-in | **In development**; live **Verification pending** | Application code is present; a bounded presentation module was checked in isolation. | Controlled end-to-end evidence, authorization behavior, and useful error states |
| Instructor approval and AI Match | **In development**; live **Verification pending** | Source and scoped test evidence exist. Identity/document checks, resort eligibility, and current availability remain mandatory filters. | Evidence that each relevant live path enforces every filter |
| Reservations and payments | **Verification pending** | Core must own consistent reservation and payment state. | Availability contention, duplicate requests, failure recovery, and reconciled payment evidence |
| Equipment rental | Live **Verification pending** | Catalog and request source surfaces are present. | Current inventory/availability behavior and a verified fulfillment flow |
| Camp | **In development**; live **Verification pending** | Camp request and controlled management work has source evidence. | Complete current flow, publication, booking and operating evidence |
| Brand connections | Live **Verification pending** | Separate branded landing preparations exist. SkiHub is the main brand; KayakHocam.com and KiralıkKayak.com are entry points. | Current deployment, technical connections and shared identity behavior |

No live capability in this table is marked Verified. Detailed evidence and access-sensitive findings belong in an authorized private record; this public file receives only an approved summary.

## First three priorities

1. **Reliable customer flow.** Establish a controlled acceptance path for application, sign-in, approval, and reservation before making stronger public claims. Owner: technical maintainer, to be assigned. Completion measure: the named flow has reviewed evidence for success and failure states. Risk: backend and test access may be unavailable.
2. **Customer trust.** Verify that eligibility, resort, availability, and transaction rules hold in the relevant environment. Owner: technical maintainer with Baran Bayran's product review. Completion measure: each mandatory filter has a reviewed acceptance result and any limitation remains explicit. Risk: a partial test can be mistaken for full-flow acceptance.
3. **Developer productivity.** Use the Ready documentation tasks to validate a small, reviewable contribution path. Owner: Baran Bayran; SkiHub Tech coordinates accepted Flow & QA and Architecture, Evidence & Security technical review roles for the two technical documentation tasks. Completion measure: one newcomer can reproduce the documented check and deliver a scoped PR. Risk: reviewer capacity and the shared-file work order can delay acceptance.

## Contribution readiness

Four public-file documentation tasks are listed in [contribution paths](contribution-paths.md). **HUB-01, HUB-02, HUB-03, and HUB-04 are Ready to claim**, with Baran Bayran reviewing external documentation PRs. SkiHub Tech coordinates two independent technical review agents: Flow & QA for HUB-02 and Architecture, Evidence & Security for HUB-04. Their accepted scopes resolve the technical-reviewer prerequisite; agent findings do not constitute a GitHub account or PR approval, and they do not approve an unseen future contribution.

A Ready task is available to request, not an automatic assignment. The maintainer confirms ownership, source, and scope in the issue before work starts. Shared-file edits run **HUB-02 first, then HUB-04** from the current accepted base after handoff, with one writer at a time. An accepted HUB-02 change must be preserved. Contributor completion, technical review, required independent GitHub approval, merge, and live product acceptance remain separate states.

Product-code tasks are not offered as public starter issues. A suitable source scope, runnable environment, terms, owner, and reviewer must exist before such a task is considered ready. Historical bug reports must be reproduced before they become current bug claims.

## Proposed outcome checkpoints

These are targets after a contributor's claim and relevant access are confirmed, not calendar commitments.

| Horizon | Outcome and KPI | Responsible role | Main risk |
| --- | --- | --- | --- |
| 24 hours | Confirm a contributor's claim for a Ready task and its independent reviewer. KPI: one owned starter task with explicit scope and acceptance criteria. | Baran Bayran | A contributor or reviewer is unavailable. |
| 7 days | A newcomer completes onboarding and submits one scoped documentation PR. KPI: the check runs from a clean checkout and the PR receives a substantive review. | Contributor and reviewer | Instructions omit a prerequisite or review capacity is limited. |
| 30 days | Accept one appropriate contribution; if it affects product code, separately verify its controlled integration. KPI: one traceable acceptance record with relevant test evidence. | Authorized maintainer | Product-code access and test environment are not yet available. |

Update this file when evidence changes, not merely when time passes. Keep public claims narrower than the supporting evidence.
