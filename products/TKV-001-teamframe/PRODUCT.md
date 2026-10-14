# Product Definition

Canonical state lives in `../../PORTFOLIO.yaml`.

## Promise

A focused HR system for organisations where everyday HR administration has become real work but there is not necessarily a dedicated HR team.

## Buyer

Founder, operator or HR owner at a growing organisation that needs a controlled internal HR system without committing to a heavy HR suite.

## Problem

Growing organisations need employee records, leave, documents, policies and setup support handled cleanly without turning HR administration into scattered spreadsheets and messages.

## Product Boundary

- employee records
- leave and absence workflows
- documents and policies
- organisation structure
- HR administration dashboard
- setup and installation support
- commercial walkthrough website

## Explicit Exclusions

- payroll engine
- enterprise HRIS replacement
- broad workforce-management suite
- recruitment workflow before employment
- TeamFrame integration with other Takaven products without a separate decision

## Relationship To TeamFrame

self; established Takaven commercial product

## Remarks

TeamFrame is an active TAKAVEN-owned UAE-focused HR product, not a discovery item. Canonical application source is takaven/teamframe protected main at e53d9ecee1fd53ccbcfa0e24ea8a6871c2a761cc (2026-10-14 audit-preparation checkpoint); the final behaviour-changing correction baseline is 3865ec2ea9ee37bfdefbb95d45214e48038ce784, with PR #30 and PR #31 closed and protected checks passing. Production app.takaven.com is deployed for pre-revenue/synthetic operation; real customer data remains unauthorised until the application's manual activation gates are completed. Canonical marketing source is takaven/takaven-web main at 2835dafe1abe97578dd7b2733cba47d1c061ad83; https://www.takaven.com/teamframe/ is live, www.takaven.com is Vercel-verified, the www root redirects to /teamframe/, and the privacy/assessment journeys are published. The online form endpoint remains intentionally unset; admin@takaven.com is the contact fallback. The superseded takaven/teamframe-site repository was deleted after website/application/portfolio reconciliation and must not be recreated or used as current authority. Current controlling commercial/product scope is in takaven/teamframe/TEAMFRAME_MANAGED_PEOPLE_OPS_SCOPE.md and docs/launch/DECISIONS.md: TeamFrame tool/implementation plus optional separately scoped TeamFrame HR Foundation Setup/HR Support. The 2026-09-06 approved internal commercial pricing reference remains US$1,950 software-only one-off and from US$3,450 with setup; these prices are intentionally not published on the current website and no price/contract change is approved here. Customer infrastructure is customer-paid/customer-controlled where applicable. Post-handover HR support and future change requests are optional and separately quoted; no monthly software subscription, mandatory maintenance or annual licence is approved. No central customer-data platform or payroll/WPS engine is within product scope. Customer onboarding/use of real customer data and integration with other TAKAVEN products remain separately approved.

## Product Principles

No additional canonical product principles recorded.

