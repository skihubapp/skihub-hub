# Contribution paths

**All four tasks are Ready to claim.** Baran Bayran reviews external documentation contributions under the [published licenses](../LICENSE.md). SkiHub Tech coordinates the accepted Flow & QA technical review role for HUB-02 and the Architecture, Evidence & Security role for HUB-04. These are two independent review agents, not separate GitHub accounts or submitted PR approvals. The contributor tasks remain open and unclaimed. All four use public documentation; none requires product source, personal data, or production access.

Start with a Ready task that matches your skill. Read [CONTRIBUTING.md](../CONTRIBUTING.md), then comment on the task's issue to request ownership and describe your intended change. Written communication is the default. The maintainer confirms task ownership, scope, and reviewer before a contributor begins; do not duplicate a claimed task.

## Shared prerequisites and execution

- Contributions must follow the license for each destination path in [LICENSE.md](../LICENSE.md).
- Baran Bayran confirms scope, the contributor who will own the task, and an independent reviewer in the issue. A technical second reviewer is required where technical claims are involved; another authorized reviewer is required if Baran authors the PR.
- Use a local checkout and Python 3.10 or later. No service account, product credentials, database, paid tool, or new dependency is needed.
- From the repository root, run `python tools/check_hub.py`. Read the files in GitHub's rendered view or an available Markdown preview. Do not install a documentation framework for these tasks.
- Record the command, result, and manual review in the PR. A clean check does not replace semantic review.

Sizes below are planning estimates, not a promise about contributor time. `XS` means roughly 1–2 hours; `S` means roughly half a day. Time may change after the initial review.

### Technical review and shared-file order

The two technical reviewers have accepted their bounded review roles. They will review a future contribution against its actual base, head, diff, and evidence; this readiness decision does not approve an unseen PR. Baran Bayran remains the real GitHub reviewer for external contributions where he is not the author. GitHub's required independent approvals and CODEOWNERS rules remain in force.

Run shared-file work in this order: **HUB-02, then HUB-04**. Only one confirmed contributor may actively edit `docs/product.md` and `docs/status-and-roadmap.md` at a time. Freeze HUB-02's accepted commit and file hashes, then confirm HUB-04's claim and handoff against the current accepted base, preserving the previous delta. A Ready-to-claim label invites a request; it is not an assignment or permission to bypass that schedule.

## HUB-01 — Review readability, navigation, and language parity

| Field | Task definition |
| --- | --- |
| Problem and impact | A first-time reader must find the correct starting route and understand the status of contribution acceptance. Review these properties; do not assume a defect already exists. |
| Scope | Review the four start routes, descriptive link text, heading order, narrow-screen table readability, and English/Turkish meaning. Fix only confirmed documentation issues. |
| Out of scope | Product UI, new visual branding, translating all documentation, product-code changes, external site claims |
| Skills | Clear English and Turkish writing; basic Markdown and accessibility review |
| Exact files | `README.md`, `README.tr.md`; local links to the existing `docs/` files |
| Run path | `python tools/check_hub.py`; render both README files and inspect desktop and narrow-width presentation |
| Acceptance | Four routes remain reachable; both languages have equivalent meaning and status; every edit is paired; no link relies on “click here”; confirmed issues and manual checks are listed in the PR. |
| Test evidence | Passing checker output plus a written keyboard/navigation and narrow-screen review; no sensitive screenshots |
| Priority / size | P1 / XS |
| Dependencies | Published terms and checker available; maintainer confirms the contributor's claim and scope before work starts |
| Reviewer | Baran Bayran; another authorized reviewer required if he authors the PR |
| Owner | Contributor whose claim is confirmed in the issue; unclaimed work is available to request |
| Access / state | Public files only / Ready to claim |
| Labels | `documentation`, `good first issue` |

## HUB-02 — Make flow-state review criteria unambiguous

| Field | Task definition |
| --- | --- |
| Problem and impact | Future validation needs clear expected states so a source or mock result cannot be mistaken for a working customer flow. |
| Scope | Review application, sign-in, approval, and reservation descriptions; add a concise documentation checklist for loading, empty, error, success, disabled, and offline states where each is meaningful. Record unknown behavior as pending verification. |
| Out of scope | Claiming a current bug, implementing forms or APIs, running live transactions, asserting that a state is implemented |
| Skills | Product QA, technical writing, understanding accessible forms |
| Exact files | `docs/product.md`, `docs/status-and-roadmap.md` |
| Run path | `python tools/check_hub.py`; manually compare each new expected state with the evidence labels |
| Acceptance | Cover application, sign-in/session, approval, and reservation against loading, empty, error, success, disabled, and offline states; a state may be not applicable with a reason. Distinguish expected outcomes from observed behavior; preserve mandatory eligibility filters; add no runtime claim without approved evidence. |
| Test evidence | Passing checker output from the proposed source, a flow/state table mapping expectations to documentation locations, and rendered-Markdown meaning review; no live test is required for this documentation task |
| Priority / size | P1 / S |
| Dependencies | Technical review role and two-file scope accepted; maintainer confirms the contributor claim, current base, and exclusive shared-file slot before work |
| Reviewer | Flow & QA technical review agent coordinated by SkiHub Tech; Baran Bayran for product meaning and independent GitHub review of external PRs |
| Owner | Unclaimed; contributor assigned only after maintainer confirmation |
| Access / state | Public files only / Ready to claim; first in the shared-file sequence |
| Labels | `documentation`, `help wanted` |

## HUB-03 — Dry-run contributor onboarding

| Field | Task definition |
| --- | --- |
| Problem and impact | A newcomer needs to know how to choose a task, run the available check, and prepare a reviewable PR without requesting product access. |
| Scope | Follow the public contributor route from a clean local copy. Clarify only reproducible ambiguities in prerequisites, commands, branch names, and evidence requested by the PR template. |
| Out of scope | Account creation, private repository access, changing permissions, opening acceptance, adding dependencies, rewriting the checker |
| Skills | Basic Git and Python; technical writing |
| Exact files | `CONTRIBUTING.md`, `AGENTS.md`, `.github/PULL_REQUEST_TEMPLATE.md`, `docs/contribution-paths.md` |
| Run path | `python tools/check_hub.py`; follow the documented steps without production credentials |
| Acceptance | A new contributor can identify a task and its scope, run the check, name a short-lived branch, and prepare a PR with meaningful evidence. Any ambiguity must include a reproduction and a focused fix. |
| Test evidence | Passing checker output and a brief first-run log containing no personal paths or credentials |
| Priority / size | P2 / S |
| Dependencies | Published terms and checker available; maintainer confirms the contributor's claim and scope before work starts |
| Reviewer | Baran Bayran; another authorized reviewer required if he authors the PR |
| Owner | Contributor whose claim is confirmed in the issue; unclaimed work is available to request |
| Access / state | Public files only / Ready to claim |
| Labels | `documentation`, `good first issue` |

## HUB-04 — Review evidence labels and architectural boundaries

| Field | Task definition |
| --- | --- |
| Problem and impact | Readers need to distinguish product intent, architectural rules, and tested behavior before making technical or commercial decisions. |
| Scope | Review claim wording across the named documents. Propose precise edits when a statement could imply unverified live operation, automatic access, or an independent data authority. |
| Out of scope | Security testing, source-code review, disclosing internal topology, introducing statistics, selecting a license, or changing the product architecture |
| Skills | Software architecture literacy and careful technical editing |
| Exact files | `docs/architecture.md`, `docs/product.md`, `docs/status-and-roadmap.md`, `README.md`, `README.tr.md` |
| Run path | `python tools/check_hub.py`; render the Mermaid diagram and compare its labels with the component table |
| Acceptance | The diagram is readable; Core remains the required authority; every runtime claim retains an evidence boundary; README edits stay bilingual; no private detail is introduced. |
| Test evidence | Passing checker output, diagram render review, and a short claim-review checklist |
| Priority / size | P2 / S |
| Dependencies | Technical review role and five-file scope accepted; shared-file edits follow HUB-02's accepted handoff and current base; maintainer confirms the contributor claim before work |
| Reviewer | Architecture, Evidence & Security technical review agent coordinated by SkiHub Tech; Baran Bayran for independent GitHub review of external PRs |
| Owner | Unclaimed; contributor assigned only after maintainer confirmation and source handoff |
| Access / state | Public files only / Ready to claim; execution queued after HUB-02's accepted source handoff |
| Labels | `documentation`, `help wanted` |

## Product-code work

The preferred first product-code scope will support instructor application/sign-in/approval or reservation reliability. It is **not ready for public assignment**. The authorized maintainer must first identify the real module, current source, reproducible behavior, approved access, runnable tests, contribution terms, and independent reviewer. Do not build a substitute application merely to make a starter issue appear executable.
