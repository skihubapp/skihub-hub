# Contributing

**Contribution acceptance is closed.** This is a publication candidate. The founder must approve publication and the applicable license/contribution terms before maintainers invite submissions or accept contributions. Do not interpret a visible template, an issue, or a PR as acceptance of terms or a transfer of rights.

## Public contributor route

1. Read the [product context](docs/product.md), [status](docs/status-and-roadmap.md), [code of conduct](CODE_OF_CONDUCT.md), and [security guide](SECURITY.md).
2. After acceptance opens, choose an approved [task](docs/contribution-paths.md). Confirm its owner, scope, dependencies, and independent reviewer in the issue before starting.
3. Work from a fork or a local copy appropriate to the approved repository. Create one short-lived branch: `docs/<topic>` for documentation, `fix/<issue>-<topic>` for an approved defect, or `feature/<issue>-<topic>` for an approved feature. Do not create branches for unassigned future work.
4. Make the smallest change that meets the acceptance criteria. Do not add product code, new dependencies, a framework, or a new source mirror to a documentation task.
5. Run the check below, perform the task's manual review, and submit a PR using the supplied template. Explain the observed problem, the change, evidence, limitations, and any paired translation update.
6. Wait for substantive independent review. Address comments in the same PR. Merge and any downstream product integration remain separate authorized maintainer actions.

## Local documentation check

Prerequisites: Git or an extracted local copy, Python 3.10 or later, and a Markdown preview if available. The checker uses the Python standard library and runs offline. It requires no product accounts, `.env`, database, or service credentials.

From the repository root:

```sh
python tools/check_hub.py
```

Report the command and exit result in the PR. Also review Markdown rendering, descriptive links, heading order, relevant narrow-screen presentation, and the meaning of any English/Turkish edit. The checker covers local links, README structure parity, and public-scope rules; it does not verify external services, complete translation accuracy, live product behavior, or every accessibility criterion.

## Changes to product facts or both READMEs

Name the claim and the kind of evidence that supports it. Keep private evidence in its authorized private location and propose only a shareable summary here. No private source address, private commit identifier, operational path, personal record, or private conversation belongs in this hub or its PR/issue history.

When editing `README.md`, edit `README.tr.md` in the same PR. Preserve equivalent meaning, section order, status, contacts, links, and matching `content-version` markers. Review the translation manually; structural parity is not semantic proof.

## Invited developers

Contact [info@skihub.com.tr](mailto:info@skihub.com.tr) in writing with the invitation context and assigned task, without attaching private documents or credentials. The maintainer confirms your identity, required scope, access approval, and an appropriate private onboarding route individually.

Before starting product work, obtain an assigned module and baseline, real-stack setup instructions, approved test environment, synthetic fixtures where needed, acceptance criteria, and an independent reviewer. Keep existing identities and Core contracts. Do not create a parallel product, duplicate authoritative database, or replacement login system.

This hub does not supply a runnable product environment or automatic source access. A mock may help validate presentation or a narrow state, but session, authorization, payment, and reservation-integrity work needs the relevant backend and controlled integration evidence. If prerequisites are unavailable, record the work as blocked rather than replacing it with a demonstration app.

## Review and acceptance

Baran Bayran is the initial reviewer. A technical second reviewer is to be assigned before accepting technical changes. If Baran authors a PR while he is the only available reviewer, assign another authorized reviewer; the PR waits until then. Authors cannot approve their own PRs.

CODEOWNERS routes review requests. It does not make approval mandatory by itself, confer access, or establish that branch protections are enabled. A passing check is one input to acceptance; maintainers also review accuracy, scope, privacy, terms, and task criteria. No hub PR automatically merges to product source or deploys a release.

Do not run untrusted contribution code with privileged tokens, production secrets, or a production-connected runner. The documentation route does not require those capabilities.

## Rights, recognition, and communication

No license has been selected for this candidate. Existing applicable notices must be preserved; do not add or change a license without the founder's explicit decision. Applicable contribution and commercial-use terms must be understandable before acceptance opens. Sending a PR or making material public does not by itself settle those rights.

Participation is voluntary and carries no guarantee of payment, equity, employment, partnership, or future work. Accepted contributions are credited through the accepted PR history unless the contributor requests otherwise. Keep communication written by default and respect a contributor's choice not to join a call.

For a sensitive concern, use [SECURITY.md](SECURITY.md) or the private conduct route in [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md), rather than a public issue.
