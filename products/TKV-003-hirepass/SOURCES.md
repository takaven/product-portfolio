# Source Assets

This file records safe source metadata only. Do not copy source code, real records, uploads, secrets or raw audit exports into this repository.

| Source | Role | Type | Locator Status | Branch | Pinned Revision | Confidence | Remarks |
| ------ | ---- | ---- | -------------- | ------ | --------------- | ---------- | ------- |
| hirepass | `PRIMARY` | `GITHUB_REPOSITORY` | `VERIFIED` | main | 50b7704b732e3309ad5ce3a361b69eb83b2a5777 | `VERIFIED` | Founder-authorised public temporary repository containing the sanitised Talent-Flow working tree as fresh one-commit history. Sanitisation complete; old Git history intentionally not preserved. Known baseline execution debt: typecheck fails in client/src/pages/manager-form.tsx and no automated test script exists. |
| Talent-Flow | `REFERENCE` | `REPLIT_EXPORT_OR_LOCAL_ASSET` | `VERIFIED` | main | 11411f3566e39760bb50d4936a45450b814b8554 | `VERIFIED` | Original local/Replit-export source used to prepare the sanitised HirePass baseline. Historical Git history is contaminated with previous-company/candidate material and must not be used for Builder access or future repository history. |
| BaynunahPass-1 | `COMPONENT` | `REPLIT_EXPORT_OR_LOCAL_ASSET` | `UNVERIFIED` | - | - | `VERIFIED` | Use auth, roles, audit and security patterns only. |
| HiringStreamline | `COMPONENT` | `REPLIT_EXPORT_OR_LOCAL_ASSET` | `UNVERIFIED` | - | - | `VERIFIED` | Use simplified V1 workflow reference. |
| PremiumHRPass | `COMPONENT` | `REPLIT_EXPORT_OR_LOCAL_ASSET` | `UNVERIFIED` | - | - | `VERIFIED` | Use candidate timeline, interview slot and notification concepts where useful. |
| BaynunahCareersPortal | `COMPONENT` | `REPLIT_EXPORT_OR_LOCAL_ASSET` | `UNVERIFIED` | - | - | `VERIFIED` | Use candidate journey and manager review concepts where useful. |
| HRPWAPass | `REFERENCE` | `REPLIT_EXPORT_OR_LOCAL_ASSET` | `UNVERIFIED` | - | - | `VERIFIED` | Reference only; not a production foundation. |
| pass UI shells | `REFERENCE` | `REFERENCE_ASSET` | `UNVERIFIED` | - | - | `INFERRED` | Visual/reference material only. |

## Repository Links

- https://github.com/takaven/hirepass
