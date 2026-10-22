# Instructions for this hub

## Scope

This repository is a knowledge and contribution hub. Keep it documentation-first. Do not turn it into a product fork, automatic mirror, application prototype, or replacement source of transaction data. The prepared content is a publication candidate; publication and contribution terms require the founder's decision. Contribution acceptance remains closed until that decision is recorded and the notices are updated consistently.

Before editing, read `README.md`, `README.tr.md`, `CONTRIBUTING.md`, the relevant `docs/` file, and the existing checker. Inspect existing files and the requested delta. Preserve another contributor's changes. State a short plan, make the smallest reversible edit, check it, and report evidence and limitations.

## Sources and claims

- Distinguish founder-supplied context, intended design, source evidence, local test evidence, controlled integration, and live evidence.
- Use the explicit status vocabulary in `docs/status-and-roadmap.md`. Do not label a flow Verified from a note, a mock, or a local documentation check.
- Live application, sign-in, instructor approval, AI Match, reservation, payment, rental, and Camp behavior remains pending verification unless approved current evidence supports a narrower update.
- Do not invent statistics, partners, source filenames, operating features, security certifications, ownership, usernames, plan support, or enabled protections.
- Historical defects need reproduction before they become current bug claims.

## Public information boundary

Only approved shareable content belongs here, including in branches, commit messages, PRs, issues, logs, artifacts, releases, and wiki content. Do not add private repository addresses, source commit identifiers, private paths, network access details, credentials, personal data, contracts, confidential commercial conditions, or private conversation excerpts. Use synthetic descriptions when an example is necessary and keep it within the assigned documentation scope.

Branches, folders, CODEOWNERS, and branch protections do not create a confidentiality boundary within a repository. Do not copy product history or source into this hub. Do not add privileged tokens, a source-reading workflow, production secrets, or a production-connected runner. Never run untrusted PR code in a privileged `pull_request_target` context.

## Product architecture rules

SkiHub Core must remain the authoritative source for identities, eligibility, availability, reservations, payments, rentals, and reviews. Keep existing user identities and contracts. Brand frontends must use an authorized Core API layer; do not create a parallel authoritative database.

Instructor identity/document verification, eligibility for the selected resort, and current availability are mandatory AI Match and reservation filters. Unverified, pending, expired, suspended, or otherwise ineligible instructors must not pass. Commercial visibility cannot override those rules. Treat these as required design boundaries until enforcement is verified.

## Editing and validation

- Keep the two READMEs equivalent in meaning, section order, links, status, contacts, and `content-version`. Edit both in the same change.
- Prefer descriptive link text, semantic heading order, concise prose, and tables that remain understandable on a narrow screen. Do not add a documentation framework or a new dependency for an editorial task.
- Run `python tools/check_hub.py` from the repository root using Python 3.10 or later. It is an offline standard-library check of local links, README structure parity, and public-scope rules.
- Manually review translation meaning and rendered Markdown; review Mermaid when changed. The checker is not full accessibility, language, security, or product verification.
- Report `PASS`, `FAIL`, or `NOT_RUN` with the command and scope. Do not call a task complete while a required check is failing or not run; state the remaining blocker.

## Review and authority

Baran Bayran is the verified initial CODEOWNER and reviewer. A technical second reviewer is to be assigned. PR authors cannot approve their own PRs; assign another authorized reviewer before acceptance when the sole reviewer is the author. CODEOWNERS does not itself enforce review or prove repository protection.

Do not merge, deploy, change visibility, grant access, select a license, accept new terms, buy a plan, or contact third parties as a side effect of an editing task. Follow the specific human authorization for those actions. No license is selected for this candidate, and contribution acceptance must not open before applicable terms are approved.

In the delivery, state what changed, why, the checks and their results, remaining risks or unknowns, and the single next action. Keep user-facing delivery in Turkish unless the user requests otherwise.
