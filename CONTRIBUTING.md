# Contributing

**Documentation contribution acceptance is open for Ready tasks.** [LICENSE.md](LICENSE.md) defines the applicable licenses. Claim a task and receive maintainer confirmation of its scope and reviewer before starting. A template or PR alone does not assign a task, grant product access, or transfer ownership.

## Public contributor route

1. Read the [product context](docs/product.md), [status](docs/status-and-roadmap.md), [code of conduct](CODE_OF_CONDUCT.md), and [security guide](SECURITY.md).
2. Choose a Ready [task](docs/contribution-paths.md). Comment on its issue to request ownership, describing the intended change. Wait for the maintainer to confirm the owner, scope, dependencies, and independent reviewer in the issue before starting. Do not duplicate an already claimed task.
3. Work from a fork or a local copy appropriate to the approved repository. Create one short-lived branch: `docs/<topic>` for documentation, `fix/<issue>-<topic>` for an approved defect, or `feature/<issue>-<topic>` for an approved feature. Do not create branches for unassigned future work.
4. Make the smallest change that meets the acceptance criteria. Do not add product code, new dependencies, a framework, or a new source mirror to a documentation task.
5. Run the check below, perform the task's manual review, and submit a PR using the supplied template. Explain the observed problem, the change, evidence, limitations, and any paired translation update. Confirm that you can license your contribution under the terms for each changed path.
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

Baran Bayran is the initial maintainer and reviews external documentation PRs. Product-code integration and technical-claim tasks require an authorized technical reviewer, to be assigned. Authors cannot approve their own PRs in GitHub; a self-authored contribution requires another authorized reviewer.

CODEOWNERS routes review requests. It does not make approval mandatory by itself, confer access, or establish that branch protections are enabled. A passing check is one input to acceptance; maintainers also review accuracy, scope, privacy, terms, and task criteria. No hub PR automatically merges to product source or deploys a release.

Do not run untrusted contribution code with privileged tokens, production secrets, or a production-connected runner. The documentation route does not require those capabilities.

## Rights, recognition, and communication

The original hub text uses **CC BY 4.0**. The checker, CI, CODEOWNERS, and issue/PR templates use **MIT**. The exact path table and full license texts are linked in [LICENSE.md](LICENSE.md); the table takes precedence over filename extensions. Both licenses permit commercial use subject to their terms. For CC BY 4.0 material, retain appropriate attribution and notices, link the license, and indicate changes. For MIT material, retain the copyright and permission notices in copies or substantial portions.

By submitting a contribution for acceptance, you confirm that it is your original work or that you hold the rights needed to license it under the same license assigned to the destination path. Do not copy third-party material without a compatible license and clear provenance; ask the maintainer before including any such material. Preserve existing notices. Contributors retain ownership of their work: this contribution rule grants a license, not a copyright assignment. It creates no separate contributor agreement or promise of compensation.

The grants cover only the specified hub material. Product source, SkiHub and related brand names, logos and trademark rights, private materials, and separately identified third-party material are excluded. A contribution does not change product licensing or authorize product integration, access, deployment, or use of a brand to imply endorsement. Do not change licensing in an unrelated PR.

Participation is voluntary and carries no guarantee of payment, equity, employment, partnership, or future work. Accepted contributions are credited through the accepted PR history and existing attribution notices must be preserved. Public PR history may remain visible. Keep communication written by default and respect a contributor's choice not to join a call.

For a sensitive concern, use [SECURITY.md](SECURITY.md) or the private conduct route in [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md), rather than a public issue.
