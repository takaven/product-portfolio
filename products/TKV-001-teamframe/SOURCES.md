# Source Assets

This file records safe source metadata only. Do not copy source code, real records, uploads, secrets or raw audit exports into this repository.

| Source | Role | Type | Locator Status | Branch | Pinned Revision | Confidence | Remarks |
| ------ | ---- | ---- | -------------- | ------ | --------------- | ---------- | ------- |
| teamframe | `PRIMARY` | `GITHUB_REPOSITORY` | `VERIFIED` | main | ee46c9dac3de5c1f9d427b6024372a628b9a322e | `VERIFIED` | Current authoritative TeamFrame HR application source (protected main). Production app.takaven.com is reported healthy for synthetic pre-revenue operation; real-customer data remains gated by application operations documents. Dated 2026-10-13 source checkpoint; verify live before operational writes. |
| takaven-web | `COMPONENT` | `GITHUB_REPOSITORY` | `VERIFIED` | main | f42496f1f6ff243bca729c3b434b03bd0b8b907f | `VERIFIED` | Canonical TeamFrame public marketing site in teamframe/; Vercel takaven-web (Takaven team, admin@takaven.com). Vercel-generated /teamframe/ and privacy pages verified in Chrome 2026-10-13; custom www.takaven.com domain verification/DNS cutover was pending. Online enquiry form endpoint remains unset; admin@takaven.com email fallback active. Old teamframe-site repo is predecessor awaiting explicit retirement. |

## Repository Links

- https://github.com/takaven/teamframe
- https://github.com/takaven/takaven-web
