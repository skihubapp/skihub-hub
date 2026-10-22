[Türkçe](README.tr.md) · English

<!-- content-version: 2026-10-22.4 -->

# SkiHub

SkiHub is a venture connecting people who want to ski with instructors and equipment rental providers, with a focus on reservations and trust. This hub is the starting point for learning about the product, contributing, joining as an invited developer, and requesting written business information.

**Contribution status:** public documentation contributions are open for the **Ready** tasks below under the [published licenses](LICENSE.md). Claim a task and receive maintainer confirmation before starting. Publishing this hub does not verify a live product flow.

<!-- section: start -->
## Choose your starting point

| I want to… | Start here | What happens next |
| --- | --- | --- |
| Understand SkiHub | [Product](docs/product.md), [current status](docs/status-and-roadmap.md) | Read the product scope and the limits of current evidence. |
| Make a technical contribution | [Contribution paths](docs/contribution-paths.md), [contribution guide](CONTRIBUTING.md) | Choose a Ready documentation task, confirm its scope with the maintainer, then submit a focused PR. |
| Start as an invited developer | [Invited developer route](CONTRIBUTING.md#invited-developers) | Request the assigned scope and onboarding details through the company contact. Access is approved individually. |
| Explore a partnership, sponsorship, or investment | [Business enquiries](docs/partners.md) | Send a short written enquiry to [info@skihub.com.tr](mailto:info@skihub.com.tr). |

<!-- section: product -->
## Product and brands

SkiHub is the main brand. KayakHocam.com and KiralıkKayak.com are positioned as customer and provider entry points. Their technical integration and live behavior require verification. Founder Baran Bayran brings experience in ski-room operations, equipment rental, and mountain operations in Uludağ.

SkiHub Core is the required source of truth for identities, eligibility, availability, reservations, payments, rentals, and reviews. This is an architectural rule; this hub does not establish that every integration currently follows it. See the [public architecture](docs/architecture.md).

<!-- section: status -->
## What is verified today?

Current source review confirms that instructor application and transaction-related code exists. This preparation also checked a small application presentation module with isolated tests. Live end-to-end verification remains pending for instructor applications, sign-in, instructor approval, AI Match, reservations, payments, rentals, and Camp. No user, revenue, partner, security-audit, or operating-scale claim is made here.

We use four explicit labels: **Verified**, **In development**, **Planned**, and **Verification pending**. A note or code review alone does not prove a working live flow. See the [status and roadmap](docs/status-and-roadmap.md) for the scope of each label.

<!-- section: contribute -->
## Contribute with a clear scope

The [initial task list](docs/contribution-paths.md) contains four documentation tasks using public files. **HUB-01** (readability and language parity) and **HUB-03** (contributor onboarding) are Ready to claim, with Baran Bayran reviewing external contributions. HUB-02 and HUB-04 remain Prepared until a technical reviewer is assigned. Product-code work requires a separately approved scope and suitable access.

Original hub text is licensed under **CC BY 4.0**; the checker, CI, and contribution templates use **MIT**, with exact paths in [LICENSE.md](LICENSE.md). Commercial reuse is allowed under the applicable license, including its notice and attribution requirements. Product code, trademarks, logos, and third-party material are outside these grants. Contributors retain their rights and submit original material they can license under the same terms for its path; this is not a transfer of ownership.

Contributions are voluntary. There is no promise of pay, equity, employment, partnership, or future work. Accepted contributions are credited in the PR history.

Read [CONTRIBUTING.md](CONTRIBUTING.md), the [code of conduct](CODE_OF_CONDUCT.md), and the [security reporting guide](SECURITY.md) before participating. Communication is written by default; calls are optional.

<!-- section: boundaries -->
## Information and review boundaries

This hub contains shareable documentation. It does not contain the commercial product source, customer records, credentials, or private onboarding details. A branch, folder, or CODEOWNERS entry does not restrict who can read a repository.

Baran Bayran is the initial maintainer and reviews external documentation PRs. A PR author needs another authorized reviewer. Product-code changes require an authorized technical reviewer, to be assigned. CODEOWNERS routes review; it does not itself enforce approval or branch protection.

<!-- section: maintain -->
## Keep both languages aligned

Every change to this README must update [README.tr.md](README.tr.md) in the same PR. Keep section order, meaning, status labels, contact details, links, and the `content-version` marker aligned. The version marker records editorial parity, not a product release.

Run `python tools/check_hub.py` from the repository root. This offline check covers local links, English/Turkish structure parity, and public-scope rules. A passing check does not prove product behavior, full translation accuracy, or publication readiness; a reviewer checks those separately.

<!-- section: contact -->
## Contact

Use [info@skihub.com.tr](mailto:info@skihub.com.tr) for written enquiries, invited-developer access requests, and private security reports. Do not send passwords, tokens, identity documents, customer data, or exploit details in an initial message. Follow [SECURITY.md](SECURITY.md) for a minimal security report.
