# Status and roadmap

Public editorial review date: **22 October 2026**. This date identifies the preparation of this document, not the date of a successful live-product test. Baran Bayran owns publication decisions; the technical reviewer is to be assigned.

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
| Knowledge and contribution hub | **Verified — documentation only** | Public documentation and path-specific licenses provide a bounded contribution route; HUB-01 and HUB-03 are Ready to claim. | A contributor must claim a task and receive scope/reviewer confirmation; technical tasks still need a technical reviewer. |
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
3. **Developer productivity.** Use the Ready documentation tasks to validate a small, reviewable contribution path. Owner: Baran Bayran; technical second reviewer to be assigned for technical work. Completion measure: one newcomer can reproduce the documented check and deliver a scoped PR. Risk: reviewer capacity can delay acceptance.

## Contribution readiness

Four public-file documentation tasks are listed in [contribution paths](contribution-paths.md). **HUB-01 and HUB-03 are Ready to claim**, with Baran Bayran reviewing external documentation PRs. A Ready task is available to request, not an automatic assignment. The maintainer confirms ownership and scope in the issue before work starts. **HUB-02 and HUB-04 remain Prepared** until an authorized technical reviewer is assigned.

Product-code tasks are not offered as public starter issues. A suitable source scope, runnable environment, terms, owner, and reviewer must exist before such a task is considered ready. Historical bug reports must be reproduced before they become current bug claims.

## Proposed outcome checkpoints

These are targets after a contributor's claim and relevant access are confirmed, not calendar commitments.

| Horizon | Outcome and KPI | Responsible role | Main risk |
| --- | --- | --- | --- |
| 24 hours | Confirm a contributor's claim for a Ready task and its independent reviewer. KPI: one owned starter task with explicit scope and acceptance criteria. | Baran Bayran | A contributor or reviewer is unavailable. |
| 7 days | A newcomer completes onboarding and submits one scoped documentation PR. KPI: the check runs from a clean checkout and the PR receives a substantive review. | Contributor and reviewer | Instructions omit a prerequisite or review capacity is limited. |
| 30 days | Accept one appropriate contribution; if it affects product code, separately verify its controlled integration. KPI: one traceable acceptance record with relevant test evidence. | Authorized maintainer | Product-code access and test environment are not yet available. |

Update this file when evidence changes, not merely when time passes. Keep public claims narrower than the supporting evidence.
