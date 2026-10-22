# Security reporting

Report a suspected security problem privately to [info@skihub.com.tr](mailto:info@skihub.com.tr), with the subject **SkiHub security report**. This company contact is the initial reporting route; no response deadline, bug bounty, or completed security certification is promised.

## Initial report

Include the affected public component or page, a short non-sensitive description, the potential impact, and how the maintainer can reach you. State whether the finding is observed or suspected. For an initial message, describe the evidence you have without attaching exploit code, credentials, personal data, or a full request/response containing sensitive values. Ask for an appropriate private evidence-transfer route if necessary.

Do not open a public issue or PR containing a secret, customer or instructor data, identity documents, internal access details, or undisclosed exploit instructions. Do not test against live payments, other people's accounts, production data, or service availability without separate explicit authorization. This reporting policy does not grant testing authorization.

If a secret may be exposed, identify its type and location without reproducing the value. Deleting a visible file does not establish that the credential or repository history is safe. An authorized owner must assess exposure and decide on revocation or rotation.

## Handling and disclosure

The maintainer should acknowledge a report when reviewed, arrange secure follow-up when needed, and coordinate any public summary after assessment. Keep sensitive evidence private while assessment and remediation are unresolved. Do not claim a finding is fixed, a flow is secure, or a security review is complete without appropriate verification.

For ordinary documentation errors with no sensitive content, use the bug template after contribution acceptance opens. See [CONTRIBUTING.md](CONTRIBUTING.md) for current acceptance status.
