[Türkçe](README.tr.md) · English

<!-- content-version: 2026-10-22.1 -->

# SkiHub

SkiHub is a venture connecting people who want to ski with instructors and equipment rental providers, with a focus on reservations and trust. This hub is the starting point for learning about the product, contributing, joining as an invited developer, and requesting written business information.

**Preparation status:** this is a candidate for public publication. Publication and contribution terms require the founder's approval. Contribution acceptance is closed until those decisions are recorded. Preparing these documents does not verify a live product flow.

<!-- section: start -->
## Choose your starting point

| I want to… | Start here | What happens next |
| --- | --- | --- |
| Understand SkiHub | [Product](docs/product.md), [current status](docs/status-and-roadmap.md) | Read the product scope and the limits of current evidence. |
| Make a technical contribution | [Contribution paths](docs/contribution-paths.md), [contribution guide](CONTRIBUTING.md) | Review a bounded task; wait for contribution acceptance to open before submitting work. |
| Start as an invited developer | [Invited developer route](CONTRIBUTING.md#invited-developers) | Request the assigned scope and onboarding details through the company contact. Access is approved individually. |
| Explore a partnership, sponsorship, or investment | [Business enquiries](docs/partners.md) | Send a short written enquiry to [info@skihub.com.tr](mailto:info@skihub.com.tr). |

<!-- section: product -->
## Product and brands

SkiHub is the main brand. KayakHocam.com and KiralıkKayak.com are positioned as customer and provider entry points. Their technical integration and live behavior require verification. Founder Baran Bayran brings experience in ski-room operations, equipment rental, and mountain operations in Uludağ.

SkiHub Core is the required source of truth for identities, eligibility, availability, reservations, payments, rentals, and reviews. This is an architectural rule; this hub does not establish that every integration currently follows it. See the [public architecture](docs/architecture.md).

<!-- section: status -->
## What is verified today?

This package describes the founder-supplied product context and proposed working rules. Live verification is pending for instructor applications, sign-in, instructor approval, AI Match, reservations, payments, rentals, and Camp. No user, revenue, partner, security-audit, or operating-scale claim is made here.

We use four explicit labels: **Verified**, **In development**, **Planned**, and **Verification pending**. A note or code review alone does not prove a working live flow. See the [status and roadmap](docs/status-and-roadmap.md) for the scope of each label.

<!-- section: contribute -->
## Contribute with a clear scope

The [initial task list](docs/contribution-paths.md) contains four documentation tasks that can be completed using public files after publication and contribution terms are approved. They are prepared candidates; they are not open assignments yet. Product-code work requires a separately approved scope and suitable access.

Contributions are voluntary. There is no promise of pay, equity, employment, or partnership. Publication and sending a PR do not by themselves settle rights or commercial-use terms. No license has been selected for this candidate; the founder must approve the applicable terms before contribution acceptance opens. Authors receive attribution in the accepted PR history unless they request otherwise.

Read [CONTRIBUTING.md](CONTRIBUTING.md), the [code of conduct](CODE_OF_CONDUCT.md), and the [security reporting guide](SECURITY.md) before participating. Communication is written by default; calls are optional.

<!-- section: boundaries -->
## Information and review boundaries

This hub contains shareable documentation. It does not contain the commercial product source, customer records, credentials, or private onboarding details. A branch, folder, or CODEOWNERS entry does not restrict who can read a repository.

Baran Bayran is the initial reviewer. A second technical reviewer must be assigned for technical changes or a PR authored by the sole available reviewer. Authors cannot approve their own PRs. CODEOWNERS is a review-routing file; it does not by itself enforce approval or branch protection.

<!-- section: maintain -->
## Keep both languages aligned

Every change to this README must update [README.tr.md](README.tr.md) in the same PR. Keep section order, meaning, status labels, contact details, links, and the `content-version` marker aligned. The version marker records editorial parity, not a product release.

Run `python tools/check_hub.py` from the repository root. This offline check covers local links, English/Turkish structure parity, and public-scope rules. A passing check does not prove product behavior, full translation accuracy, or publication readiness; a reviewer checks those separately.

<!-- section: contact -->
## Contact

Use [info@skihub.com.tr](mailto:info@skihub.com.tr) for written enquiries, invited-developer access requests, and private security reports. Do not send passwords, tokens, identity documents, customer data, or exploit details in an initial message. Follow [SECURITY.md](SECURITY.md) for a minimal security report.
