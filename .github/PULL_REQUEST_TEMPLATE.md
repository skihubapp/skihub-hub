## Problem and resulting behavior

Link the approved task and describe the observed documentation need. Do not include private addresses, source identifiers, personal data, or confidential evidence.

## Scope

List the changed public files, why this solution fits, and anything deliberately outside the task.

## Validation

- Command: `python tools/check_hub.py`
- Result: `PASS / FAIL / NOT_RUN` with a brief output summary
- Manual review: Markdown rendering, relevant narrow-screen readability, descriptive links, language meaning, and Mermaid if changed
- Evidence limit: these checks concern hub content, not live product behavior

## Review checklist

- [ ] Publication and applicable contribution terms are approved, and contribution acceptance is open.
- [ ] The task has an owner, clear acceptance criteria, and an independent reviewer.
- [ ] The change contains only approved public information, including its commit messages and attachments.
- [ ] Product intentions and architecture rules remain distinct from verified runtime behavior.
- [ ] Both READMEs are updated together where needed, with matching meaning, sections, links, and `content-version`.
- [ ] Required checks pass, and any limitation or `NOT_RUN` is explained.
- [ ] No license, access, visibility, dependency, or deployment change is hidden in this PR.
- [ ] The PR author is not the approving reviewer.

## Risks, unknowns, and follow-up

State any remaining blocker and the single next action. A passing check does not automatically authorize merge, product integration, publication, or release.
