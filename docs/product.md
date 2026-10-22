# Product

SkiHub is a venture focused on connecting people who want to ski with instructors and equipment rental providers, with reservations and trust at the center of the experience. This document describes the intended product and the founder-supplied brand context. It is not a claim that the flows below are live.

## People and problems

| Person | Need | Product responsibility |
| --- | --- | --- |
| Skier or family | Find a suitable instructor and understand the next step | Clear eligibility, availability, prices when confirmed, and reservation states |
| Instructor | Apply, complete required checks, and offer lessons where eligible | Protected documents, explicit approval states, and current availability |
| Rental provider | Present available equipment and handle a reliable rental request | Accurate availability and a clear reservation process |
| Operations reviewer | Make consistent eligibility and service decisions | Authorized access, traceable decisions, and limited personal-data exposure |

## Product flows and evidence boundary

| Area | Intended flow | Current public status |
| --- | --- | --- |
| Instructor application | Submit required information, complete identity/document checks, receive a decision | **Verification pending** for a live end-to-end flow |
| Sign-in and session | Use the established identity and retain appropriate access | **Verification pending** for live sign-in and authorization |
| Instructor approval | Approve only after required checks; show pending, expired, rejected, and suspended states clearly | **Verification pending** for live enforcement |
| AI Match | Filter for verified identity/documents, resort eligibility, and current availability before matching | **Verification pending** for live enforcement |
| Reservation and payment | Confirm availability, preserve a consistent reservation state, reconcile payment evidence | **Verification pending** for a live end-to-end transaction |
| Rental | Connect a customer with a suitable rental provider and a dependable request process | **Verification pending** for live availability and fulfillment |
| Camp | Support a defined camp experience and its participation process | **Verification pending**; public scope and operating evidence are not yet established |

These are review subjects, not assertions of present defects. No real transaction, payment acceptance, or service availability should be inferred from this hub.

## Trust rules

SkiHub Core must remain the source of truth for identities, eligibility, reservations, payments, availability, rentals, and reviews. Brand frontends must use an authorized Core API layer rather than create duplicate transaction databases or parallel login identities.

AI Match and booking must exclude an instructor who is unverified, in review, ineligible for the selected resort, expired, suspended, or unavailable. Sponsorship or paid visibility must never bypass those filters. This is a required design boundary, not a completed security or live-flow certification.

## Brands

| Brand | Positioning | Verification boundary |
| --- | --- | --- |
| SkiHub | Main product and brand | Live capabilities are listed separately above. |
| KayakHocam.com | Instructor-oriented customer and provider entry point | Technical connection, shared identity, and live flow require verification. |
| KiralıkKayak.com | Equipment-rental customer and provider entry point | Technical connection, shared identity, and live flow require verification. |

Founder Baran Bayran has experience in ski-room operations, equipment rental, and mountain operations in Uludağ.

## What this hub helps you do

Read the [architecture](architecture.md), distinguish evidence in the [status register](status-and-roadmap.md), choose a [bounded documentation task](contribution-paths.md), or send a [written business enquiry](partners.md). Product-code access and private onboarding are approved separately.
