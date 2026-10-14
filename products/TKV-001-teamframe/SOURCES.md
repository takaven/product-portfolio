# Source Assets

This file records safe source metadata only. Do not copy source code, real records, uploads, secrets or raw audit exports into this repository.

| Source | Role | Type | Locator Status | Branch | Pinned Revision | Confidence | Remarks |
| ------ | ---- | ---- | -------------- | ------ | --------------- | ---------- | ------- |
| teamframe | `PRIMARY` | `GITHUB_REPOSITORY` | `VERIFIED` | main | e53d9ecee1fd53ccbcfa0e24ea8a6871c2a761cc | `VERIFIED` | Current authoritative TeamFrame HR application source (protected main). The final behaviour-changing correction baseline is 3865ec2ea9ee37bfdefbb95d45214e48038ce784; later main commits are documentation reconciliation only. Production app.takaven.com is deployed for pre-revenue/synthetic operation; the final correction release passed protected checks and public root/health smoke. Real-customer data remains gated by the application operational documents. |
| takaven-web | `COMPONENT` | `GITHUB_REPOSITORY` | `VERIFIED` | main | 2835dafe1abe97578dd7b2733cba47d1c061ad83 | `VERIFIED` | Live canonical TeamFrame public marketing site under teamframe/ on takaven/takaven-web. www.takaven.com is Vercel-verified, HTTPS is active and the www root redirects to /teamframe/. Vercel Production was re-verified READY on 2026-10-14. The online form endpoint remains unset, with admin@takaven.com as the supported contact fallback. The predecessor takaven/teamframe-site repository was deleted after source reconciliation. |

## Repository Links

- https://github.com/takaven/teamframe
- https://github.com/takaven/takaven-web
